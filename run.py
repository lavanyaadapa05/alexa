import speech_recognition as sr 
import pyttsx3 
import pywhatkit 
import datetime 
import wikipedia 
import pyjokes
import sounddevice as sd
from scipy.io.wavfile import write

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def record_audio():
    fs = 44100  
    duration = 5 
    print("Listening...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')
    sd.wait()  
    write("output.wav", fs, audio_data)  
    return "output.wav"

def take_command():
    command = ""  
    try:
    
        audio_file = record_audio()
        with sr.AudioFile(audio_file) as source:
            audio = listener.record(source) 
            command = listener.recognize_google(audio)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(f"Command: {command}")
    except sr.WaitTimeoutError:
        print("Listening timed out. No command received.")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
    except Exception as e:
        print(f"Error: {e}")  
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk("Sorry, I don't have access to a calendar.")

    elif 'are you single' in command:
        talk('I am in a relationship with wifi.')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif "satvika" in command:
        talk("She is a beautiful girl with long hair and big eyes...")
    else:
        talk('Please say the command again.')

while True:
    run_alexa()
