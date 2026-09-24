import speech_recognition as sr
import pyttsx3
import datetime as dt
import webbrowser as wb
import pywhatkit as pk
import wikipedia as wiki

# Initialize recognizer and speaker
listener = sr.Recognizer()
speaker = pyttsx3.init()

# Voice settings
speaker.setProperty('rate', 170)
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)   # Female voice


def speak(text):
    print("MAXX:", text)
    speaker.say(text)
    speaker.runAndWait()


def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source, duration=1)
            audio = listener.listen(source, timeout=5, phrase_time_limit=5)

            print("Recognizing...")
            command = listener.recognize_google(audio, language='en-IN')
            command = command.lower()
            print("You said:", command)

    except sr.UnknownValueError:
        speak("I could not recognize your voice")

    except sr.RequestError:
        speak("Internet connection issue")

    except Exception as e:
        print("Error:", e)
        speak("I can't understand, please say again sir")

    return command


def run_assistant(user_command):
    if 'hello' in user_command:
        speak("Hello Dileep, how can I help you?")

    elif 'open google' in user_command:
        speak("Opening Google")
        wb.open("https://www.google.com")

    elif 'time' in user_command:
        current_time = dt.datetime.now().strftime('%I:%M %p')
        speak(f"The time is {current_time}")

    elif 'play' in user_command:
        song = user_command.replace('play', '').strip()
        speak(f"Playing {song}")
        pk.playonyt(song)

    elif 'who is' in user_command:
        person = user_command.replace('who is', '').strip()
        info = wiki.summary(person, 2)
        speak(info)

    elif 'what is' in user_command:
        thing = user_command.replace('what is', '').strip()
        info = wiki.summary(thing, 2)
        speak(info)

    elif 'stop' in user_command or 'exit' in user_command:
        speak("Goodbye Dileep")
        exit()

    else:
        speak("I can't understand, please say again sir")


# Main Program
speak("Hello Dileep, I am MAXX. How can I help you?")

while True:
    user_command = take_command()

    if user_command:
        run_assistant(user_command)