# Document & Audio Processing Service

A comprehensive web-based application that provides three powerful features:
- **Audio Transcription**: Convert audio files to text using OpenAI's Whisper AI
- **Document Conversion**: Convert documents between various formats (DOCX, PDF, TXT, Excel)
- **OCR (Optical Character Recognition)**: Extract text from images and PDF files

## 🚀 Features

### 🎤 Audio Transcription
- **Multiple Audio Format Support**: MP3, WAV, M4A, FLAC, OGG, OPUS, AAC, WMA, MP4, WebM, 3GP, AMR, AIFF, AU
- **Automatic Language Detection**: Automatically detects the language in your audio
- **High-Quality Transcription**: Powered by OpenAI's Whisper model (base model by default)
- **Real-time Progress Tracking**: Visual feedback with elapsed time and processing steps
- **Sentence Formatting**: Automatically formats transcriptions with sentences on separate lines

### 📄 Document Conversion
- **DOCX Conversions**: DOCX ↔ TXT, DOCX ↔ PDF
- **PDF Conversions**: PDF ↔ TXT, PDF ↔ DOCX
- **TXT Conversions**: TXT ↔ PDF, TXT ↔ DOCX
- **Excel Conversions**: XLSX/XLS → TXT
- **Format Detection**: Automatically detects available conversion options based on file type

### 👁️ OCR (Text Extraction)
- **Image Support**: PNG, JPG, JPEG, GIF, BMP, TIFF, WEBP
- **PDF Support**: Extract text from PDF files (multi-page support)
- **Formatted Output**: Extracted text formatted with sentences on separate lines
- **Page Separation**: PDF pages are clearly marked in the output

### 🎨 User Interface
- **Modern Tabbed Interface**: Easy navigation between features
- **Drag & Drop Support**: Intuitive file upload
- **Real-time Progress**: Live timers and progress bars
- **Processing Time Display**: See exactly how long operations take
- **Download Results**: Download all processed files

## 📋 Prerequisites

### System Requirements
- **Python**: 3.8 or higher
- **FFmpeg**: Required for audio transcription
- **Tesseract OCR**: Required for OCR functionality (optional but recommended)

### Installing FFmpeg

**Windows:**
```powershell
# Using winget (recommended)
winget install ffmpeg

# Or using Chocolatey
choco install ffmpeg

# Or download from: https://ffmpeg.org/download.html
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

### Installing Tesseract OCR (for OCR feature)

**Windows:**
```powershell
# Using winget (recommended)
winget install --id UB-Mannheim.TesseractOCR --accept-package-agreements --accept-source-agreements
```

**macOS:**
```bash
brew install tesseract
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install tesseract-ocr
```

## 🛠️ Installation

### Option 1: Local Installation

1. **Clone or navigate to the project directory:**
```bash
cd audiotranscribe
```

2. **Create a virtual environment (recommended):**
```bash
python -m venv venv
```

3. **Activate the virtual environment:**

   **Windows:**
   ```bash
   venv\Scripts\activate
   ```

   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

5. **Download Whisper model (automatic on first use):**
   The application will automatically download the Whisper model on first transcription. The "base" model is used by default.

### Option 2: Docker Installation (Recommended)

See [DOCKER.md](DOCKER.md) for detailed Docker installation instructions.

Quick start:
```bash
docker-compose up -d
```

## 🚀 Usage

### Starting the Server

**Windows:**
```bash
python app.py
# Or double-click start.bat
```

**macOS/Linux:**
```bash
python app.py
# Or
bash start.sh
```

**Docker:**
```bash
docker-compose up -d
```

### Accessing the Application

Open your web browser and navigate to:
```
http://localhost:5012
```

### Using Audio Transcription

1. Click the **"🎤 Audio Transcription"** tab
2. Drag and drop an audio file or click to browse
3. Click **"Transcribe Audio"**
4. Wait for processing (you'll see real-time progress)
5. View and download the transcription

### Using Document Conversion

1. Click the **"📄 Document Conversion"** tab
2. Upload a document (DOCX, PDF, TXT, or Excel file)
3. Select the target format from the dropdown
4. Click **"Convert Document"**
5. Download the converted file

### Using OCR

1. Click the **"👁️ OCR (Text Extraction)"** tab
2. Upload an image or PDF file
3. Click **"Extract Text (OCR)"**
4. View and download the extracted text

## 📁 Supported Formats

### Audio Formats (Transcription)
- MP3, WAV, M4A, FLAC, OGG, OPUS, AAC
- WMA, MP4 (audio track), WebM (audio track)
- 3GP, AMR, AIFF, AU

### Document Formats (Conversion)
- **Input**: DOCX, PDF, TXT, XLSX, XLS
- **Output**: DOCX, PDF, TXT

### Image Formats (OCR)
- PNG, JPG, JPEG, GIF, BMP, TIFF, WEBP
- PDF (for text extraction)

## ⚙️ Configuration

### Changing the Whisper Model

Edit `app.py`:
```python
model = whisper.load_model("base")  # Options: tiny, base, small, medium, large
```

**Model Options:**
- **tiny**: Fastest, least accurate (~39M parameters)
- **base**: Good balance (default, ~74M parameters)
- **small**: Better accuracy (~244M parameters)
- **medium**: High accuracy (~769M parameters)
- **large**: Best accuracy (~1550M parameters)

### File Size Limit

Default maximum file size is 100MB. To change it, modify `MAX_FILE_SIZE` in `app.py`:
```python
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB
```

### Server Port

Default port is 5012. To change it, modify the last line in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5012)
```

## 📂 Project Structure

```
audiotranscribe/
├── app.py                    # Flask backend server
├── transcribe_file.py        # Command-line transcription script
├── requirements.txt          # Python dependencies
├── Dockerfile               # Docker container configuration
├── docker-compose.yml       # Docker Compose configuration
├── .dockerignore           # Docker ignore patterns
├── templates/
│   └── index.html          # Frontend web interface
├── uploads/                # Temporary upload directory (auto-created)
├── transcriptions/          # Saved transcription files (auto-created)
├── conversions/             # Converted document files (auto-created)
├── ocr_results/            # OCR extracted text files (auto-created)
├── start.bat               # Windows startup script
├── start.sh                # Linux/macOS startup script
├── README.md               # This file
├── DOCKER.md               # Docker documentation
└── INSTALL_FFMPEG.md       # FFmpeg installation guide
```

## 🔌 API Endpoints

### Audio Transcription
- `GET /` - Main web interface
- `POST /upload` - Upload and transcribe audio file
- `GET /download/<filename>` - Download transcription file
- `GET /supported-formats` - Get list of supported audio formats
- `GET /check-ffmpeg` - Check FFmpeg installation status

### Document Conversion
- `POST /convert-document` - Convert document between formats
- `GET /download-conversion/<filename>` - Download converted document
- `GET /supported-conversions` - Get supported conversion formats

### OCR
- `POST /ocr` - Perform OCR on image or PDF
- `GET /download-ocr/<filename>` - Download OCR result
- `GET /ocr-capabilities` - Get OCR capabilities and status

### System
- `GET /health` - Health check endpoint

## 🐳 Docker Deployment

See [DOCKER.md](DOCKER.md) for complete Docker deployment instructions.

### Quick Docker Start

```bash
# Build and start
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

## 🔧 Troubleshooting

### "FFmpeg not found" error
- Ensure FFmpeg is installed and available in your system PATH
- Verify installation: `ffmpeg -version`
- See [INSTALL_FFMPEG.md](INSTALL_FFMPEG.md) for detailed instructions

### "Tesseract is not installed" error (OCR)
- Install Tesseract OCR (see Prerequisites section)
- On Windows, the app will auto-detect Tesseract in common locations
- Verify installation: `tesseract --version`
- Restart the server after installation

### "Required libraries not available" error
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Restart the server after installing new packages
- Check that Python version is 3.8 or higher

### Slow transcription
- Use a smaller Whisper model (tiny or base) for faster processing
- Consider using GPU acceleration if available (requires CUDA-enabled PyTorch)
- Processing time is roughly 0.2-0.5x the audio duration

### Out of memory errors
- Use a smaller Whisper model
- Process shorter audio files
- Close other applications to free up memory
- Reduce MAX_FILE_SIZE if processing large files

### Model download issues
- Ensure you have a stable internet connection for the first run
- Models are cached after first download
- First transcription may take longer as the model downloads

### Document conversion not working
- Verify that required libraries are installed (python-docx, pypdf, reportlab, etc.)
- Check server logs for specific error messages
- Ensure file format is supported (see Supported Formats section)

## ⚡ Performance Tips

1. **GPU Acceleration**: For faster transcription, install PyTorch with CUDA support:
   ```bash
   pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```

2. **Model Selection**: Choose the appropriate model size based on your needs:
   - Quick transcriptions: `tiny` or `base`
   - High accuracy: `medium` or `large`

3. **File Preparation**: For best results:
   - Use clear audio with minimal background noise
   - Ensure good audio quality
   - Consider splitting very long files
   - For OCR, use high-resolution images

4. **Docker Performance**: 
   - Use Docker volumes for persistent storage
   - Allocate sufficient memory (recommended: 4GB+)
   - Consider using GPU support in Docker for faster processing

## 🔒 Privacy & Security

- **Local Processing**: All processing happens locally - no data is sent to external services
- **Automatic Cleanup**: Uploaded files are automatically deleted after processing
- **No Data Storage**: Processed files are saved only if you download them
- **Secure**: All operations run on your local machine or Docker container

## 📝 Notes

- First transcription may take longer as the Whisper model downloads (~150MB for base model)
- Transcription time depends on audio length and model size (roughly 0.2-0.5x audio duration)
- Model loading time: 10-30 seconds on first use, then cached in memory
- Document conversions are typically very fast (< 5 seconds for most files)
- OCR processing time depends on image/PDF size and complexity

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### Third-Party Components

This software uses the following open-source components:

- **OpenAI Whisper**: MIT License - Copyright (c) 2022 OpenAI
- **Tesseract OCR**: Apache License 2.0 - Copyright (c) Google Inc.
- **Other dependencies**: See `requirements.txt` for individual licenses

All third-party components maintain their original licenses. Please refer to the [LICENSE](LICENSE) file for complete license information and third-party attributions.

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section above
2. Review the documentation files (DOCKER.md, INSTALL_FFMPEG.md)
3. Check server logs for detailed error messages
4. Open an issue on the repository

## 🎯 Use Cases

- **Content Creators**: Transcribe podcasts, videos, and interviews
- **Students**: Convert lecture recordings to text notes
- **Business**: Extract text from scanned documents and PDFs
- **Accessibility**: Make audio content accessible through text
- **Document Management**: Convert documents between formats
- **Data Entry**: Extract text from images and forms
