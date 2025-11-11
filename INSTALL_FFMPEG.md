# Installing FFmpeg on Windows

FFmpeg is required for audio file processing. Here are the easiest ways to install it:

## Option 1: Using Chocolatey (Recommended)

1. If you have Chocolatey installed, run:
```powershell
choco install ffmpeg
```

2. If you don't have Chocolatey, install it first from: https://chocolatey.org/install

## Option 2: Using Winget (Windows Package Manager)

```powershell
winget install ffmpeg
```

## Option 3: Manual Installation

1. Download FFmpeg from: https://www.gyan.dev/ffmpeg/builds/
2. Download the "ffmpeg-release-essentials.zip"
3. Extract the ZIP file to a location like `C:\ffmpeg`
4. Add `C:\ffmpeg\bin` to your system PATH:
   - Press Win + X and select "System"
   - Click "Advanced system settings"
   - Click "Environment Variables"
   - Under "System variables", find and select "Path"
   - Click "Edit"
   - Click "New"
   - Add `C:\ffmpeg\bin`
   - Click OK on all windows
5. Restart your terminal/PowerShell

## Verify Installation

After installation, verify FFmpeg is working:
```powershell
ffmpeg -version
```

You should see FFmpeg version information.

## Once FFmpeg is installed

Simply restart the application:
```powershell
python app.py
```

The application will then be able to process audio files.

