import pyttsx3                     ## text to speech
import speech_recognition as sr    ## speech recognition
import datetime                    ## date time teller
import wikipedia                   ## wikipedia
import webbrowser                  ## browser
import os                          ## operating system

# taking voice from my computer system
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')

#print(voices)
#print(type(voices))
#print(voices[0].id)
#print(voices[1].id)

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',150)
# speech function

def speak(text):
    """This  fuction takes text speak with voices
    
    Args:
        text (_type_): string
    """
    engine.say(text)
    engine.runAndWait()

#speak("hello i am data scientist, how are you?")

# python main.py



# speech recognition function

def takeCommand():
    """This function will recognise voice and return text
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language = "en-in")
            print(f"User said: {query}\n")
            
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query

text = takeCommand()
speak(text)
