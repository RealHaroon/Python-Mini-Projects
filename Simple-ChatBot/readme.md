

```md
# Levi ChatBot 🤖💬  

Levi is a simple Python-based chatbot that can respond to various inputs, tell jokes, check the weather, and provide the current time and date.  

## 📌 Features  
- Responds to basic greetings and questions  
- Tells jokes 😂  
- Fetches real-time weather updates 🌦  
- Provides the current time and date ⏰📅  
- Engages in friendly chat  

## 🚀 How to Use  
1. Clone or download the script.  
2. Ensure Python is installed on your system.  
3. Install dependencies using:  
   ```sh
   pip install requests pyjokes
   ```
4. Run the script:  
   ```sh
   python levi_chatbot.py
   ```
5. Start chatting! Type `"exit"` to quit.  

## 🛠 Installation  
This chatbot requires the following Python libraries:  
- `requests` (for fetching weather data)  
- `pyjokes` (for generating jokes)  

Install them using:  
```sh
pip install requests pyjokes
```

## 🌦 Weather Functionality  
Levi fetches real-time weather updates for **Karachi** using the **OpenWeatherMap API**.  

If you want to change the city:  
1. Find the following line in the script:  
   ```python
   CITY = "Karachi"
   ```
2. Replace `"Karachi"` with your desired city.  

## 🎭 Example Chat Session  
```
Hi 👋🏼 I'm Levi, a simple ChatBot created by Haroon The Goat.
You: hi
Levi: Hello! I'm Levi, a simple ChatBot. How can I assist you?

You: time
Levi: 15:30:45

You: weather
Levi: Current Temperature in Karachi: 28°C, Condition: Clear Sky

You: tell me a joke
Levi: Why do programmers prefer dark mode? Because light attracts bugs! 😂

You: exit
Levi: Goodbye! Have a great day! 😊
```

## 🔥 Fun Easter Eggs  
Levi has some fun responses, such as:  
- `"who is the goat?"` → **"Muhammad Ali 🐐"**  
- `"who is the greatest fighter of all time?"` → **"Jon Jones is the GOAT 🐐"**  

## 🔗 Contributing  
Feel free to fork and improve the chatbot! 🚀  

---

👨‍💻 Created by **Haroon The Goat** 🐐  
```
