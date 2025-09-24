import requests
import speech_recognition as sr
import pyttsx3

# Text-to-speech setup
tts = pyttsx3.init()

def speak(text):
    print("Speaking...")
    tts.say(text)
    tts.runAndWait()

def get_weather(city_name):
    api_key = "de401f3cb487308770a22fc7de5765f4"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city_name, "appid": api_key, "units": "metric"}

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        weather = data["weather"][0]

        output = f"""
Weather in {city_name.title()}:
Temperature: {main['temp']}°C
Condition: {weather['description'].title()}
Humidity: {main['humidity']}%
Min Temp: {main['temp_min']}°C
Max Temp: {main['temp_max']}°C
        """
        print(output)

        with open("weather_report.txt", "w", encoding="utf-8") as file:
            file.write(output.strip())

        summary = f"The temperature in {city_name.title()} is {main['temp']}°C with {weather['description']}."
        speak(summary)
    else:
        error = f"Could not find weather for '{city_name}'."
        print(error)
        with open("weather_report.txt", "w", encoding="utf-8") as file:
            file.write(error)
        speak(error)

def listen_for_weather():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Temperature — just say the city name:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("Processing...")

    try:
        request = recognizer.recognize_google(audio).lower()
        print(f"You said: {request}")

        # Clean up unnecessary words
        for word in ["tasu", "ask about", "temperature", "temperture", "weather", "wheather", "in"]:
            request = request.replace(word, "")
        city = request.strip()

        if city:
            get_weather(city)
        else:
            speak("Please mention a valid city name.")
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand what you said.")
    except sr.RequestError:
        speak("Speech Recognition service is not available.")

# # Run once
# if __name__ == "__main__":
#     listen_for_weather()
