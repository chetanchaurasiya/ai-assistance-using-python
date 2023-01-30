import pywhatkit
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
import pyaudio
import wolframalpha


from tkinter import *
from PIL import Image, ImageTk

chetan_root = Tk()

chetan_root.title("Project")
chetan_root.geometry("600x500")
chetan_root.minsize(600,434)
chetan_root.maxsize(600,434)

img=Image.open("Z:\project/ai_personal_assistant_software.jpg")
re=img.resize((600,434),Image.LANCZOS)
pic=ImageTk.PhotoImage(re)

l=Label(image=pic)
l.pack(fill=BOTH,expand=1)

x=Label(l,text="Welcome into python based assistant",font=("Algerian",20,"bold"))
x.pack(pady=10)

b=Button(l,fg="blue",bg="yellow",text="Start",font=("bold",16),anchor=NW,command=lambda:chetan_root.destroy())
b.pack(padx=50,pady=70,anchor=W,side=BOTTOM)



engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("welcome into our project demo")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing")
        quiry=r.recognize_google(audio, language='en-in')
        print(f"user said: {quary}\n")
    except Exception as e:
        print("can you say that again please !")
        return "None"
    return 'quary'



if __name__=="__main__":
    chetan_root.mainloop()
    wishMe()
    while True:
        quary=takecommand().lower()
        # quary=input()
        if "wikipedia" in quary:
            speak("searching on wikipedia")
            quary=quary.replace("wikipedia","")
            result=wikipedia.summary(quary, sentences=3)
            speak("accordig to wikipedia")
            print(result)
            speak(result)
        elif 'open youtube' in quary:
            webbrowser.open("youtube.com")
        elif "open google" in quary:
            webbrowser.open("google.com")
        elif "the time" in quary:
            t=datetime.datetime.now().strftime('%H:%M:%S')
            time=f"the current time is {t}"
            print(time)
            speak(time)
        elif "good night" in quary:
            hour=int(datetime.datetime.now().hour)
            if hour>=21 and hour<=3:
                speak("good night")
                print("good night")
            elif hour<=18 and hour>=12:
                print("THis is not sleeping time ! \nso, good afternoon")
                speak("THis is not sleeping time ! \nso, good afternoon")
            elif hour>=18 and hour<=21:
                print("THis is not sleeping time ! \nso, good evening")
                speak("THis is not sleeping time ! \nso, good evening")
            elif hour<=3 and hour>=12:
                print("THis is not sleeping time ! \nso, good morning")
                speak("THis is not sleeping time ! \nso, good morning")
        elif "search" in quary:
            quary=quary.replace("search","")
            webbrowser.open_new_tab(quary)
        elif "shutdown" in quary:
            pywhatkit.shutdown(time=180)
        elif "cancel" in quary:
            pywhatkit.cancel_shutdown()
        elif "stop" in quary:
            break
        else:
            client = wolframalpha.Client('748LQE-7TKLXLV7JQ')
            res=client.query(quary)
            output=next(res.results).text
            print(output)
            speak(output)
