from dotenv import load_dotenv
import os

load_dotenv()

OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
WAKE_WORDS = ['nova', 'hey nova', 'ok nova']

# TTS settings
TTS_RATE = 160
