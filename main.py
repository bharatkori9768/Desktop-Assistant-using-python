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

#text = takeCommand()   # this will text whati say
#speak(text)           # speak that text
# if __name__ == "__main__":
# # wish me
#while True:
def wishme():
    hour = (datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning bharat. how are you?")
        
    elif hour >= 12 and hour < 18:
        speak("good afternoon bharat. what did you eat?")   
    
    else:
        speak("go to sleep")

if __name__ == "__main__":
    
    wishme()
    
    while True:
        query = takeCommand().lower()
        #print(query)
        if "wikipedia" in query:
            speak("wikipedia is searching")
            query = query.replace("wikipedia","")
            #print(query)
            results = wikipedia.summary(query,sentences = 2)
            speak("according to wikipedia")
            print(results)
            speak(results)
            
        elif "youtube" in query:
            speak("searching and opening on youtube")
            webbrowser.open("youtube.com")
            
        elif "google" in query:
            speak("searching in google")
            webbrowser.open("google.com")
            
        elif "github" in query:
            speak("open git")
            webbrowser.open("github.com")
            
        elif "good bye" in query:
            speak("ok sir bye-bye")
            exit()
            
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is{strTime}")
        
           
