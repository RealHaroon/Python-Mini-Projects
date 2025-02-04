import requests
import pyjokes
from datetime import datetime


API_KEY = "bce58c060085d7b85f02650eb1ea9143"
CITY = "Karachi"

def currTime():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def currDate():
    now = datetime.now()
    return now.strftime("%Y-%m-%d")


def currWeather():
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={"bce58c060085d7b85f02650eb1ea9143"}&units=metric"
    response = requests.get(URL)
    data = response.json()
    if response.status_code == 200:
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        return f"Current Temperature in {CITY}: {temp}°C, Condition: {weather_desc}"
    else:
        return "Error fetching weather data."
def joke():
    return pyjokes.get_joke()+" 😂"

responses = {
    "hi": "Hello! I'm Levi, a simple ChatBot. How can I assist you?",
    "hello": "Hi! I'm Levi, a simple ChatBot. How can I assist you?",
    "yo":"Yo! What's up?",
    "what is your name?":"I'm Levi, a simple ChatBot created by Haroon.",
    "who are you?":"I'm Levi, a simple ChatBot created by Haroon.",
    "how are you?":"Im fine,What about you?",
    "time":currTime,  # Store function reference (without parentheses)
    "date":currDate,
    "weather":currWeather,
    "who created you?":"Haroon",
    "what is your favorite color":"red",
    "what language is used in you creation?" : "Python Programming Language 🐍",
    "tell me a joke":joke,
    "do you like Python?": "Of course! Python is my favorite programming language. 🐍",
    "what can you do?":"I can tell you the time, date, weather, and have a friendly chat with you!",
    "will haroon get a girlfriend?":"well its complicated 💀",
    "who is the greatest fighter of all time?": "Jon Jones is the GOAT 🐐",
    "who is the goat?": "Muhammad Ali 🐐 "
    
}


def chat():
    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("Levi: Goodbye! Have a great day! 😊")
            break
        response = responses.get(user_input, "I'm sorry, I don't understand that.")
        if callable(response):  # Check if response is a function
            print("Levi:", response())
        else:
            print("Levi:", response)

print("Hi 👋🏼Im Levi a simple chatBot created by Haroon The Goat ")
chat()
