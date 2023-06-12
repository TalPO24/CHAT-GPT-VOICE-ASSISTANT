# import speech_recognition as sr
# import pyttsx3
# import openai
# import webbrowser

# openai.api_key = "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"

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voices', voices[1].id)

# r = sr.Recognizer()
# mic = sr.Microphone(device_index=1)

# conversation = ""
# user_name = "Tal"
# bot_name = "John"

# def open_website(website):
#     if "youtube" in website:
#         webbrowser.open("https://www.youtube.com")
#     elif "google" in website:
#         webbrowser.open("https://www.google.com")
#     else:
#         return "Sorry, I can only open YouTube or Google."

# while True:
#     with mic as source:
#         print("\nListening...")
#         r.adjust_for_ambient_noise(source, duration=0.2)
#         audio = r.listen(source)
#     print("No longer listening")

#     try:
#         user_input = r.recognize_google(audio)
#     except:
#         continue

#     prompt = user_name + ":" + user_input + "\n" + bot_name + ":"
#     conversation += prompt

#     if "open" in user_input:
#         website = user_input.split("open", 1)[1].strip()
#         open_result = open_website(website)
#         if open_result:
#             response_str = open_result
#     else:
#         response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=conversation,
#             temperature=0.7,
#             max_tokens=256,
#             top_p=1,
#             frequency_penalty=0,
#             presence_penalty=0
#         )

#         response_str = response["choices"][0]["text"].replace("\n", "")
#         response_str = response_str.split(user_name + ":", 1)[0].split(bot_name + ":", 1)[0]

#     conversation += response_str + "\n"
#     print(response_str)

#     engine.say(response_str)
#     engine.runAndWait()


import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import subprocess

# Initialize the speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set the voice for the assistant
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_current_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def get_current_date():
    now = datetime.datetime.now()
    current_date = now.strftime("%A, %B %d, %Y")
    speak(f"Today is {current_date}")

def open_website(url):
    webbrowser.open(url)
    speak("Opening the website")

def open_spotify():
    # Modify the path below to the location of your Spotify application
    spotify_path = r"C:\Users\User\AppData\Roaming\Spotify"
    subprocess.Popen(spotify_path)
    speak("Opening Spotify")

def support_frontend():
    speak("Sure, I can help you with front-end development. What would you like to know?")

def check_weather():
    speak("What city's weather would you like to check?")
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    city = recognizer.recognize_google(audio).lower()

    # Code to fetch and display weather information for the specified city
    # Implement your weather API integration here

def take_note():
    speak("What would you like to make a note of?")
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    note = recognizer.recognize_google(audio)

    # Code to save the note to a file or database
    # Implement your desired note-taking functionality here

def search_wikipedia():
    speak("What would you like to search for on Wikipedia?")
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    query = recognizer.recognize_google(audio)
    query = query.replace(" ", "_")

    search_url = f"https://en.wikipedia.org/wiki/{query}"
    open_website(search_url)

# Voice Assistant initialization message
speak("Hi Tal, I'm John. How can I assist you today?")

# Main loop for voice commands
while True:
    try:
        # Record audio from the microphone
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        # Recognize speech using Google Speech Recognition
        command = recognizer.recognize_google(audio).lower()
        print("Command:", command)

        # Process the recognized command
        if "time" in command:
            get_current_time()
        elif "date" in command:
            get_current_date()
        elif "open" in command:
            if "google" in command:
                open_website("https://www.google.com")
            elif "youtube" in command:
                open_website("https://www.youtube.com")
            elif "chat gpt" in command:
                open_website("https://chat.openai.com/")
            elif "github" in command:
                open_website("https://github.com/TalPO24?tab=repositories")
            elif "spotify" in command:
                open_spotify()
        elif "front-end" in command or "frontend" in command or "web development" in command:
            support_frontend()
        elif "weather" in command:
            check_weather()
        elif "note" in command or "make a note" in command:
            take_note()
        elif "search" in command or "wikipedia" in command:
            search_wikipedia()
        elif "quit" in command or "exit" in command or "goodbye" in command:
            speak("Goodbye Master!")
            break
        else:
            speak("Sorry, I didn't understand that. Could you please repeat?")

    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand what you said. Could you please repeat?")
    except sr.RequestError:
        speak("Sorry, I'm having trouble accessing the Google Speech Recognition service.")



