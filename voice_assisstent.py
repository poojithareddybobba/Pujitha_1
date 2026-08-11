import speech_recognition as sr
import win32com.client
import datetime
import webbrowser

# Windows Text-to-Speech
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def speak(text):
    print("Assistant:", text)
    speaker.Speak(text)

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I didn't understand. Please repeat.")
        return ""

    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def tell_date():
    current_date = datetime.datetime.now().strftime("%d %B %Y")
    speak(f"Today's date is {current_date}")

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Searching Google for {query}")

def main():
    speak("Hello! I am your Voice Assistant.")

    while True:
        command = listen()

        if command == "":
            continue

        if "hello" in command:
            speak("Hello! How can I help you?")

        elif "how are you" in command:
            speak("Iam fine, thank you for asking. How can I assist you today?")

        elif "what's your name" in command:
            speak("I am your voice assistant. You can call me any name you like.")

        elif "time" in command:
            tell_time()

        elif "date" in command:
            tell_date()

        elif "search" in command:
            query = command.replace("search", "").strip()

            if query:
                search_google(query)
            else:
                speak("What would you like me to search?")

        elif "ok thank you" in command or "thanks" in command:
            speak("You're welcome! If you need anything else, just ask me.")
            
        elif "exit" in command or "stop" in command:
            speak("ok bye see you again!")
            break

        else:
            speak("Sorry, I don't know that command.")

if __name__ == "__main__":
    main()
