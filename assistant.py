from stt import listen
from tts import say
import commands
from config import WAKE_WORDS

def is_wake(text: str):
    if not text:
        return False
    for w in WAKE_WORDS:
        if w in text:
            return True
    return False

def process_command(text: str):
    if not text:
        return "I didn't catch that."
    # Basic command parsing
    if 'time' in text or 'date' in text:
        return commands.tell_time()
    if text.startswith('search') or text.startswith('google') or 'search for' in text:
        q = text.replace('search', '').replace('google', '').replace('for', '').strip()
        return commands.search_web(q)
    if 'wikipedia' in text or 'who is' in text or 'what is' in text:
        q = text.replace('wikipedia', '').replace('who is', '').replace('what is', '').strip()
        return commands.wiki_summary(q)
    if 'weather' in text:
        parts = text.split()
        if 'in' in parts:
            idx = parts.index('in')
            city = ' '.join(parts[idx+1:])
        else:
            city = 'Delhi'
        return commands.weather_for(city)
    if 'open' in text:
        return commands.search_web(text.replace('open', '').strip())
    return "Sorry, I don't know that. I can search the web, tell time, weather, or wiki."
