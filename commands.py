import webbrowser
import datetime
import requests
import wikipedia
from config import OPENWEATHER_API_KEY

def tell_time():
    now = datetime.datetime.now()
    return now.strftime("It's %I:%M %p on %A, %d %B %Y")

def search_web(query):
    if not query:
        return "No query provided."
    url = f'https://www.google.com/search?q={query.replace(" ", "+")}'
    webbrowser.open(url)
    return f"I searched the web for {query}."

def wiki_summary(query, sentences=2):
    try:
        summary = wikipedia.summary(query, sentences=sentences)
        return summary
    except Exception:
        return "I couldn't find a good Wikipedia result."

def weather_for(city):
    if not OPENWEATHER_API_KEY:
        return "Weather API key not set."
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={OPENWEATHER_API_KEY}'
    try:
        r = requests.get(url, timeout=6)
        data = r.json()
        if data.get('cod') != 200:
            return "City not found."
        desc = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"Current weather in {city} is {desc} with temperature {temp}°C."
    except Exception:
        return "Failed to fetch weather."
