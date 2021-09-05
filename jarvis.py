import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests, json
import vlc 
import pafy
url = "https://www.youtube.com/watch?v=sCbbMZ-q4-I&list=RDsCbbMZ-q4-I&start_radio=1"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# for voice in voices:
#     print("Voice: %s" % voice.name)
#     print(" - ID: %s" % voice.id)
#     print(" - Languages: %s" % voice.languages)
#     print(" - Gender: %s" % voice.gender)
#     print(" - Age: %s" % voice.age)
#     print("\n")
# print(voices[3])
engine.setProperty('voice',voices[11].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour <18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Jarvis, Please tell me how can i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)#Language='en') #show_all=True)
        # response = json.dumps(query, ensure_ascii=False).encode('utf8')
        print(query)


    except Exception as e:
        print(e)
        print("Say That again please...")

        return "None"

    return query

if __name__ == "__main__":
    # speak("Hello Aniket")
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....please wait')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            speak(results)

        elif 'hello' in query:
            speak("Hello sir")

        elif 'how are you jarvis' in query:
            speak("Im good sir, what about you?")


        elif 'open youtube' in query:
            speak("Opening youtube for you sir")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak("Opening google for you sir")
            webbrowser.open("https://www.google.com/")

        elif 'open wikipedia' in query:
            webbrowser.open("https://www.wikipedia.com/")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com/")
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%-I:%M %p")
            print(strTime)
            speak("Its ")
            speak(strTime)
            speak("Sir")

        elif 'open code' in query:
            speak("Opening Visual studio code for you sir")
            os.system('code')

        elif 'open control' in query:
            speak("Opening Gnome control center for you sir")
            os.system('gnome-control-center')

        elif 'kya kar rahe ho' in query:
            speak("Kuch khaas naahi sir")
            # os.system('gnome-control-center')

        elif 'thank you' in query:
            speak("Welcome sir, anything else do you want to know sir")


        elif 'song from youtube' in query:
            speak("Playing your favorite song from youtube sir")

            video = pafy.new(url) 
  
            # getting best stream 
            best = video.getbest() 

            playurl = best.url

            Instance = vlc.Instance()
            player = Instance.media_player_new()
            Media = Instance.media_new(playurl)
            Media.get_mrl()
            player.set_media(Media)
            player.play()
  
            # creating vlc media player object 
            # media = vlc.MediaPlayer(best.url) 
  
            # start playing video 
            # media.play() 
        
        if 'bye' in query:
            speak("Ok Bye, have a nice day sir")
            break