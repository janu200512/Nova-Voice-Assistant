# Nova Voice Assistant (Python)

Complete Python desktop voice assistant — speech-to-text, text-to-speech, basic commands, web search, Wikipedia, weather (OpenWeatherMap), and optional ChatGPT integration.

## Files in this repo
- `main.py` — entry point (wake-word loop + command handling)
- `assistant.py` — parser and high-level logic
- `stt.py` — speech-to-text wrapper (`speech_recognition`)
- `tts.py` — text-to-speech helper (`pyttsx3`)
- `commands.py` — concrete command implementations (time, web search, wiki, weather)
- `config.py` — configuration and API key loader (`python-dotenv`)
- `.env.example` — example environment variables
- `requirements.txt` — Python dependencies
- `.gitignore` — files to ignore for Git

## Quick setup
1. Clone the repo and create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\Scripts\activate    # Windows
   pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env` and add your OPENWEATHER_API_KEY (and OPENAI_API_KEY if using ChatGPT features).
3. Run `python main.py` and speak the wake word (default: "nova").

## Notes
- On Linux you may need `portaudio19-dev` for `pyaudio`.
- For offline STT consider `VOSK` instead of Google STT.
- For robust wake-word detection consider `porcupine` or `snowboy` (platform-specific).
