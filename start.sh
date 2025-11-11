#!/bin/bash

echo "Starting Audio Transcription Service..."
echo ""
echo "Make sure you have:"
echo "1. Python 3.8+ installed"
echo "2. FFmpeg installed"
echo "3. Dependencies installed (run: pip install -r requirements.txt)"
echo ""
echo "Starting server on http://localhost:5012"
echo "Press Ctrl+C to stop the server"
echo ""

python app.py
