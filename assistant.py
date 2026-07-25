# assistant.py
import datetime
import subprocess
import webbrowser
import urllib.parse

import pyttsx3
import speech_recognition as sr

apps = {
    "notepad": ["notepad.exe"],
    "calculator": ["calc.exe"],
    "paint": ["mspaint.exe"],
    "file explorer": ["explorer.exe"],
}

engine = pyttsx3.init()
engine.setProperty("rate", 175)
recognizer = sr.Recognizer()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source, timeout=6, phrase_time_limit=8)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
    except sr.RequestError:
        speak("Speech recognition is unavailable.")
    return ""


def run_command(command):
    if command in ["exit", "quit", "stop assistant"]:
        speak("Goodbye!")
        return False

    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"It is {current_time}")
        return True

    if command.startswith("search for "):
        query = command.replace("search for ", "", 1)
        speak(f"Searching for {query}")
        url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(query)
        webbrowser.open(url)
        return True

    if command in ["open browser", "open the browser"]:
        speak("Opening browser")
        webbrowser.open("https://www.google.com")
        return True

    if command.startswith("open "):
        app_name = command.replace("open ", "", 1).strip()

        if app_name in apps:
            speak(f"Opening {app_name}")
            subprocess.Popen(apps[app_name])
        elif "." in app_name and " " not in app_name:
            speak(f"Opening {app_name}")
            webbrowser.open("https://" + app_name)
        else:
            speak("I can open notepad, calculator, paint, file explorer, or websites.")
        return True

    speak("Command not recognized.")
    return True


speak("Voice assistant is ready.")

while True:
    try:
        user_command = listen()
        if user_command and not run_command(user_command):
            break
    except sr.WaitTimeoutError:
        print("No speech detected. Try again.")
    except KeyboardInterrupt:
        speak("Goodbye!")
        break