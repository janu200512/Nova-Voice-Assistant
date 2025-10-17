import speech_recognition as sr

r = sr.Recognizer()

def listen(timeout=None, phrase_time_limit=7):
    """Listen from default microphone and return recognized text in lowercase, or None."""
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.6)
        try:
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        except Exception:
            return None
    try:
        text = r.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return None
