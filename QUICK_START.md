# Quick Start Guide

Get up and running with the Document & Audio Processing Service in minutes!

## 🚀 Fastest Way: Docker (Recommended)

```bash
# 1. Navigate to project directory
cd audiotranscribe

# 2. Start the service
docker-compose up -d

# 3. Open in browser
# http://localhost:5012
```

That's it! The Docker setup includes everything (FFmpeg, Tesseract OCR, all dependencies).

## 📦 Local Installation

### Windows

```powershell
# 1. Install FFmpeg
winget install ffmpeg

# 2. Install Tesseract OCR (optional, for OCR feature)
winget install --id UB-Mannheim.TesseractOCR

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Start server
python app.py
```

### macOS/Linux

```bash
# 1. Install system dependencies
brew install ffmpeg tesseract  # macOS
# OR
sudo apt install ffmpeg tesseract-ocr  # Linux

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Start server
python app.py
```

## 🎯 What You Can Do

### 1. Transcribe Audio
- Upload any audio file
- Get text transcription with sentence formatting
- Download as TXT file

### 2. Convert Documents
- Convert between DOCX, PDF, and TXT
- Excel to TXT conversion
- Fast and reliable

### 3. Extract Text from Images
- Upload images or PDFs
- Extract text using OCR
- Formatted output ready to use

## 📚 Need More Help?

- **Full Documentation**: See [README.md](README.md)
- **Docker Setup**: See [DOCKER.md](DOCKER.md)
- **FFmpeg Installation**: See [INSTALL_FFMPEG.md](INSTALL_FFMPEG.md)
- **Troubleshooting**: Check README.md troubleshooting section

## 🔧 Common Commands

```bash
# Docker
docker-compose up -d          # Start
docker-compose logs -f        # View logs
docker-compose down           # Stop

# Local
python app.py                 # Start server
python transcribe_file.py "file.m4a"  # CLI transcription
```

## ✅ Verify Installation

1. **Check server**: http://localhost:5012/health
2. **Check FFmpeg**: `ffmpeg -version`
3. **Check Tesseract**: `tesseract --version`
4. **Check libraries**: Server will show status on startup

## 🎉 You're Ready!

Open http://localhost:5012 and start processing!

