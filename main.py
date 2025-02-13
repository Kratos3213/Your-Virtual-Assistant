import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio as pa
import pyjokes
import pywhatkit
import pyautogui
import smtplib

class understand:
    def __self__(self):
        self.query="what do you want me to do"
        def takecommand(self):
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold=1
                r.energy_threshold=3000
                audio=r.listen(source)
            try:
                print("Recognizing...")
                query=r.recognize_google(audio,language='en-in')
                print(f"User said: {query}\n")
            except Exception as e:
                print("Say that again please...")
                return "None"
            return query
        



def speak(audio):
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hello Sir I am Pet. How may I help you")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.energy_threshold=3000
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
 try:
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('email','password')
    server.sendmail('email',to,content)
    server.close
    speak("Email has been sent!")
 except Exception as e:
    print(e)
    speak("Sorry my friend. I am not able to send this email")


def think():
    speak("I am thinking of something")
    query=takeCommand()
    return query



if __name__=="__main__":
    
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'open code' in query:
            codePath="C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'send mail' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="vg446636@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
        
        elif 'something funny' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())
        elif 'search' in query:
            query=query.replace("search","")
            pywhatkit.search(query)
        elif 'play' in query:
            song=query.replace("play","")
            speak("playing"+song)
            pywhatkit.playonyt(song)
        elif 'pause' in query:
            pywhatkit.pause()
        elif 'stop' in query:
            speak("Bye take care")
            exit()
        
        elif 'stop' in query:
            speak("Bye take care")
            exit()
        elif ('open riot' in query) or ('open league of legends' in query):
            webbrowser.open("valorant.com")
        elif ('open dota' in query) or ('open dota 2' in query):
            webbrowser.open("dota2.com")
        elif ('game download' in query):
            speak("Downloading the game")
            webbrowser.open("dodi repacks")
        elif ('writing' in query):
            speak("What should I write")
            content=takeCommand()
            speak("Please say the name of the file")
            name=takeCommand()
            file=open(name+".txt","w")
            file.write(content)
            file.close()
        elif ('read' in query):
            speak("Please say the name of the file")
            name=takeCommand()
            file=open(name+".txt","r")
            print(file.read())
            speak("Done")
        elif ('open valorant'in query):
            os.startfile("C:\\Riot Games\\Riot Client\\RiotClientServices.exe")
        elif ('thanks' in query):
            speak("You are welcome")
        elif ('you are so cute' in query):
            speak("ohh my dear thanks for complimenting me")
        elif ("download" in query):
            speak("What should I download")
            download=takeCommand()
            webbrowser.open(download)
            speak("downloading"+download)
        
        elif "where is" in query:
            query = query.split(" ")
            location = query[2]
            speak("Hold on mate, I will show you where " + location + " is.")
            webbrowser.open("https://www.google.nl/maps/place/" + location + "/&amp;")

        elif "music" in query:
            try:
                music_dir = 'C:\\Users\\vg541\\Music'#file path which contains the music file
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))
            except:
                speak(f"There is some error with the path: {str(e)}")
        
    







