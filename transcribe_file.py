#!/usr/bin/env python3
"""
Quick script to transcribe an audio file directly without the web interface.
Usage: python transcribe_file.py "path/to/audio/file.m4a"
"""

import sys
import os
import time
import re
import whisper
from pathlib import Path

def format_transcription_with_sentences(text):
    """
    Format transcription text with sentences on separate lines.
    Splits on sentence endings (. ! ?) followed by space and capital letter.
    """
    if not text:
        return text
    
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text.strip())
    
    # Split on sentence endings: . ! ? followed by space and capital letter
    # This pattern captures: sentence ending + space + capital letter
    pattern = r'([.!?])\s+([A-Z])'
    
    # Split and keep delimiters
    parts = re.split(pattern, text)
    
    if len(parts) == 1:
        # No sentence endings found, return as is
        return text
    
    # Reconstruct sentences
    formatted_lines = []
    i = 0
    
    while i < len(parts):
        if i == 0:
            # First sentence (before any split)
            if parts[i].strip():
                formatted_lines.append(parts[i].strip())
        elif i + 1 < len(parts):
            # We have: punctuation, space, next sentence start
            punctuation = parts[i]  # . ! or ?
            next_sentence_start = parts[i + 1]  # Capital letter + rest
            
            # Complete previous sentence with punctuation
            if formatted_lines:
                formatted_lines[-1] += punctuation
            else:
                formatted_lines.append(punctuation)
            
            # Start new sentence
            if next_sentence_start.strip():
                formatted_lines.append(next_sentence_start.strip())
            
            i += 1  # Skip next part as we processed it
        else:
            # Remaining text
            if parts[i].strip():
                if formatted_lines:
                    formatted_lines[-1] += " " + parts[i].strip()
                else:
                    formatted_lines.append(parts[i].strip())
        
        i += 1
    
    # Join with newlines
    result = '\n'.join(line.strip() for line in formatted_lines if line.strip())
    
    # Clean up excessive newlines
    result = re.sub(r'\n{3,}', '\n\n', result)
    
    return result

def transcribe_file(file_path):
    """Transcribe an audio file using Whisper"""
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"ERROR: File not found: {file_path}")
        return False
    
    file_size = os.path.getsize(file_path) / (1024 * 1024)  # Size in MB
    print(f"File: {os.path.basename(file_path)}")
    print(f"Size: {file_size:.2f} MB")
    print()
    
    # Load model
    print("Loading Whisper model (base)...")
    print("   This may take 10-30 seconds on first run...")
    load_start = time.time()
    model = whisper.load_model("base")
    load_time = time.time() - load_start
    print(f"Model loaded in {load_time:.2f} seconds")
    print()
    
    # Transcribe
    print("Starting transcription...")
    print("   This may take several minutes for long audio files...")
    print("   (Processing time is roughly 0.2-0.5x the audio duration)")
    print()
    
    transcription_start = time.time()
    result = model.transcribe(
        file_path,
        language=None,  # Auto-detect language
        task="transcribe"
    )
    transcription_time = time.time() - transcription_start
    
    # Get transcription text
    transcription_text = result["text"]
    detected_language = result.get('language', 'unknown')
    
    # Format transcription with sentences on separate lines
    formatted_text = format_transcription_with_sentences(transcription_text)
    
    # Save transcription
    output_dir = Path("transcriptions")
    output_dir.mkdir(exist_ok=True)
    
    input_filename = Path(file_path).stem
    output_file = output_dir / f"{input_filename}_transcription.txt"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(formatted_text)
    
    # Print results
    print()
    print("=" * 60)
    print("TRANSCRIPTION COMPLETE!")
    print("=" * 60)
    print(f"Total time: {transcription_time:.2f} seconds ({transcription_time/60:.2f} minutes)")
    print(f"Detected language: {detected_language}")
    print(f"Saved to: {output_file}")
    print()
    print("Transcription preview (first 500 characters):")
    print("-" * 60)
    preview = formatted_text[:500] + ("..." if len(formatted_text) > 500 else "")
    print(preview)
    print("-" * 60)
    print()
    print(f"Full transcription saved to: {output_file}")
    
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transcribe_file.py <path_to_audio_file>")
        print()
        print("Example:")
        print('  python transcribe_file.py "C:\\Users\\romeo.fredson\\Downloads\\2 Farmer using DAF Ghana.m4a"')
        sys.exit(1)
    
    file_path = sys.argv[1]
    success = transcribe_file(file_path)
    
    if not success:
        sys.exit(1)

