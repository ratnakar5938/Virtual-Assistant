import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

# paths are different of everyone's device

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    """
    :param audio: takes a string and speak it out
    :return: None
    """
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """
    Wishes the user as per the time
    :return: none
    """
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour <= 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("I am Jarvis Sir. Please tell me how do I help you")

def takeCommand():
    """
    It takes microphone input from the user
    :return: string
    """
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
            # print(e)
            print("Say that again please...")
            return "None"
        return query

def sendEmail(sendto, contentToSend):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    speak("Enter your email")
    email = input("Enter your email: ")
    speak("Enter your password")
    password = input("Enter your password: ")
    server.login(f"{email}", f"{password}")
    server.sendmail(f"{email}", sendto, contentToSend)
    server.close()

if __name__ == '__main__':
    wishMe()

    while True:
        query = takeCommand().lower()
        # logic for executing task based on query
        if "wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir = ""
            if "english" in query:
                music_dir = "E:\\Song\\Eng"  # path of music folder in the device
            elif "bollywood" in query:
                music_dir = "E:\\Song\\My Music RR"  # path of music folder in the device
            elif "trap" in query:
                music_dir = "E:\\Song\\Audio\\Trap"  # path of music folder in the device
            else:
                continue
            songs = os.listdir(music_dir)
            choice = random.randint(0, len(songs)-1)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[choice]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "open code" in query:
            code_path = "C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  # path of vs code in the device
            os.startfile(code_path)

        elif "open cad" in query:
            cad_path = "C:\\Program Files\\Autodesk\\AutoCAD 2020\\acad.exe"  # path of autocad in the device
            os.startfile(cad_path)

        elif "open java" in query:
            java_path = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2020.3\\bin\\idea64.exe"  # path of intellij idea in the device
            os.startfile(java_path)

        elif "open pycharm" in query:
            pycharm_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.2\\bin\\pycharm64.exe"  # path of pycharm in the device
            os.startfile(pycharm_path)

        elif "open fox" in query:
            fox_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"  # path of firefox in the device
            os.startfile(fox_path)

        elif "open chrome" in query:
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # path of chrome in the device
            os.startfile(chrome_path)

        elif "open edge" in query:
            edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"  # path of ms edge in the device
            os.startfile(edge_path)

        elif "email to me" in query:
            try:
                speak("what should I say")
                content = takeCommand()
                to = "rattu5938@gmail.com"  # email of receiver
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry my friend ravi bhai. I am not able to send this email")

        elif "hey jarvis" in query:
            speak("How can I help you sir")

        elif "quit" in query or "stop jarvis" in query:
            exit()