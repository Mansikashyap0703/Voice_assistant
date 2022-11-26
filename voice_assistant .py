
import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') 

engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio) 
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
         speak("good evening")
    speak("please tell me how may i help you")
def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n") 

    except Exception as e:
          

        print("Say that again please...")   
        return "None" 
    return query    

    
if __name__=="__main__" :
    speak("my name is pikachu")
    wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
              webbrowser.open("youtube.com") 
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'who are you' in query:
            speak("i am pikachu and i want love")    
        elif 'i miss you' in query:
            speak("i miss you too doll")    
        elif 'quit' in query or 'bye' in query:
            speak("take care little doll")
            exit()
   



