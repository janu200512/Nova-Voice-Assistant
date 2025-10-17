import pyttsx3
from config import TTS_RATE

engine = pyttsx3.init()
engine.setProperty('rate', TTS_RATE)

def say(text, block=True):
    """Speak `text`. Blocking by default for simpler behavior."""
    engine.say(text)
    if block:
        engine.runAndWait()
