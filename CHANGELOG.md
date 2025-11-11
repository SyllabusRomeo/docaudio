# Changelog

All notable changes to the Document & Audio Processing Service will be documented in this file.

## [2.0.0] - 2025-01-XX

### Added
- **Document Conversion Feature**
  - DOCX to TXT conversion
  - DOCX to PDF conversion
  - PDF to TXT conversion
  - PDF to DOCX conversion
  - TXT to PDF conversion
  - TXT to DOCX conversion
  - Excel (XLSX/XLS) to TXT conversion

- **OCR (Optical Character Recognition) Feature**
  - Extract text from images (PNG, JPG, JPEG, GIF, BMP, TIFF, WEBP)
  - Extract text from PDF files with multi-page support
  - Automatic sentence formatting for OCR results

- **Enhanced UI**
  - Tabbed interface for easy navigation between features
  - Real-time progress tracking with elapsed timers
  - Processing time display for all operations
  - Step-by-step progress indicators

- **Docker Support**
  - Dockerfile for containerization
  - docker-compose.yml for easy deployment
  - Complete Docker documentation (DOCKER.md)
  - Health checks and resource limits

- **Improved Documentation**
  - Comprehensive README.md with all features
  - Docker deployment guide
  - Updated installation instructions
  - Troubleshooting guides

### Changed
- **Audio Transcription**
  - Enhanced progress tracking with real-time timers
  - Sentence formatting for better readability
  - Model loading time tracking
  - More detailed processing time breakdown

- **Server Configuration**
  - Default port changed to 5012
  - Auto-detection of Tesseract OCR in common locations
  - Better error messages and library availability checks

### Fixed
- Fixed sentence formatting to properly separate sentences
- Improved error handling for missing dependencies
- Better file cleanup after processing

## [1.0.0] - Initial Release

### Added
- Audio transcription using OpenAI Whisper
- Support for multiple audio formats
- Web-based user interface
- Real-time transcription progress
- Download transcriptions as text files
- Automatic language detection
- FFmpeg integration for audio processing

