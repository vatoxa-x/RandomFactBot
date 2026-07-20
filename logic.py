import requests
import pyttsx3
def get_fact() -> str:
    base_url = 'https://uselessfacts.jsph.pl/random.json'
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.json().get("text", "Не удалось получить факт.")
    else:
        return "Не удалось получить факт. Пожалуйста, повторите попытку позже."
def speak(fact: str)-> None:
    engine = pyttsx3.init()
    engine.setProperty("voice", voices[1].id)
    engine.say(fact)
    engine.runAndWait()
