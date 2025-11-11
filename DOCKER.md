# Docker Deployment Guide

This guide explains how to deploy the Document & Audio Processing Service using Docker.

## Prerequisites

- **Docker**: Version 20.10 or higher
- **Docker Compose**: Version 2.0 or higher (optional, but recommended)
- **Minimum 4GB RAM** (8GB recommended for better performance)
- **At least 10GB free disk space** (for Docker images and models)

## Quick Start

### Using Docker Compose (Recommended)

1. **Clone or navigate to the project directory:**
```bash
cd audiotranscribe
```

2. **Start the service:**
```bash
docker-compose up -d
```

3. **Check logs:**
```bash
docker-compose logs -f
```

4. **Access the application:**
Open your browser and navigate to: `http://localhost:5012`

5. **Stop the service:**
```bash
docker-compose down
```

### Using Docker directly

1. **Build the image:**
```bash
docker build -t audiotranscribe:latest .
```

2. **Run the container:**
```bash
docker run -d \
  --name audiotranscribe-app \
  -p 5012:5012 \
  -v $(pwd)/transcriptions:/app/transcriptions \
  -v $(pwd)/conversions:/app/conversions \
  -v $(pwd)/ocr_results:/app/ocr_results \
  audiotranscribe:latest
```

3. **View logs:**
```bash
docker logs -f audiotranscribe-app
```

4. **Stop the container:**
```bash
docker stop audiotranscribe-app
docker rm audiotranscribe-app
```

## Configuration

### Port Configuration

To change the port, modify `docker-compose.yml`:

```yaml
ports:
  - "8080:5012"  # Change 8080 to your desired port
```

Or when using Docker directly:
```bash
docker run -d -p 8080:5012 ...
```

### Resource Limits

Adjust resource limits in `docker-compose.yml`:

```yaml
deploy:
  resources:
    limits:
      cpus: '4.0'      # Increase for better performance
      memory: 8G       # Increase for larger models
    reservations:
      cpus: '2.0'
      memory: 4G
```

### Environment Variables

Add environment variables in `docker-compose.yml`:

```yaml
environment:
  - PYTHONUNBUFFERED=1
  - FLASK_ENV=production
  - MAX_FILE_SIZE=200000000  # 200MB
```

## Volume Management

### Persistent Storage

The following directories are mounted as volumes to persist data:

- `./transcriptions` - Audio transcription results
- `./conversions` - Document conversion results
- `./ocr_results` - OCR extraction results

### Backup Data

To backup your data:
```bash
# Create backup
tar -czf backup-$(date +%Y%m%d).tar.gz transcriptions/ conversions/ ocr_results/

# Restore backup
tar -xzf backup-YYYYMMDD.tar.gz
```

## Advanced Configuration

### GPU Support (for faster transcription)

If you have an NVIDIA GPU, you can use GPU acceleration:

1. **Install NVIDIA Container Toolkit:**
```bash
# Ubuntu/Debian
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
```

2. **Modify docker-compose.yml:**
```yaml
services:
  app:
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
```

3. **Rebuild with GPU support:**
```yaml
# In Dockerfile, change PyTorch installation to CUDA version
RUN pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Custom Whisper Model

To use a different Whisper model, modify `app.py` before building:

```python
model = whisper.load_model("large")  # Instead of "base"
```

Or set it via environment variable (requires code modification).

### Network Configuration

For production, consider using a reverse proxy:

```yaml
# docker-compose.yml
services:
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - app
```

## Troubleshooting

### Container won't start

1. **Check logs:**
```bash
docker-compose logs app
```

2. **Check resource availability:**
```bash
docker stats
```

3. **Verify Docker is running:**
```bash
docker ps
```

### Out of memory errors

1. **Increase memory limits** in docker-compose.yml
2. **Use a smaller Whisper model** (tiny or base)
3. **Reduce MAX_FILE_SIZE** in app.py

### Port already in use

1. **Find process using the port:**
```bash
# Linux/macOS
lsof -i :5012

# Windows
netstat -ano | findstr :5012
```

2. **Change port** in docker-compose.yml or stop the conflicting service

### FFmpeg or Tesseract not found

These are installed in the Docker image. If you see errors:

1. **Rebuild the image:**
```bash
docker-compose build --no-cache
```

2. **Check if they're installed in container:**
```bash
docker-compose exec app ffmpeg -version
docker-compose exec app tesseract --version
```

### Slow performance

1. **Allocate more resources** (CPU/memory)
2. **Use GPU acceleration** if available
3. **Use smaller Whisper model** for faster transcription
4. **Check system resources:**
```bash
docker stats
```

### Data not persisting

1. **Verify volumes are mounted:**
```bash
docker-compose exec app ls -la /app/transcriptions
```

2. **Check volume permissions:**
```bash
# Fix permissions if needed
sudo chown -R $USER:$USER transcriptions/ conversions/ ocr_results/
```

## Production Deployment

### Security Considerations

1. **Use environment variables** for sensitive configuration
2. **Implement rate limiting** (add to app.py or use nginx)
3. **Use HTTPS** with a reverse proxy
4. **Set proper file permissions** for volumes
5. **Regularly update** Docker images and dependencies

### Monitoring

1. **Health checks** are built-in (check `/health` endpoint)
2. **Log aggregation** - consider using Docker logging drivers
3. **Resource monitoring** - use `docker stats` or monitoring tools

### Updates

1. **Pull latest code:**
```bash
git pull
```

2. **Rebuild and restart:**
```bash
docker-compose build
docker-compose up -d
```

3. **Verify:**
```bash
docker-compose logs -f
```

## Docker Commands Reference

```bash
# Build image
docker-compose build

# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f

# Restart service
docker-compose restart

# Execute command in container
docker-compose exec app bash

# View resource usage
docker stats

# Remove everything (including volumes)
docker-compose down -v

# Rebuild without cache
docker-compose build --no-cache
```

## Multi-Container Setup

For production, you might want to separate services:

```yaml
version: '3.8'

services:
  app:
    build: .
    # ... app configuration

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - app

  redis:
    image: redis:alpine
    # For caching or queue management (future enhancement)
```

## Support

For Docker-specific issues:
1. Check Docker logs: `docker-compose logs`
2. Verify Docker version: `docker --version`
3. Check system resources: `docker system df`
4. Review this documentation

For application issues, see the main [README.md](README.md) troubleshooting section.

