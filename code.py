import collections
from tkinter import *
import threading
import datetime
import pickle
import os.path
import os
import pyttsx3
import speech_recognition as sr
import pytz
import subprocess
import webbrowser
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import ctime, sleep
from datetime import datetime


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def record():
    try:
        thread = threading.Thread(target=click, daemon=True)
        thread.start()
    except:
        pass


def command():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        audio = r.listen(mic)
        input = ""
        try:
            input = r.recognize_google(audio)

            print(input)
        except:
            return " "

    return input


def search_google():
    ggcontent = command().lower()
    speak("Here are the search results ")
    url = "https://google.com/search?q=" + ggcontent
    print(url)
    webbrowser.open_new_tab(url)


def open_youtube():
    ytcontent = command().lower()
    url = "https://www.youtube.com/results?search_query=" + ytcontent
    print(url)
    speak("Here are the search results ")
    webbrowser.open_new_tab(url)


def open_facebook():
    url = "https://www.facebook.com/"
    print(url)
    webbrowser.open_new_tab("https://www.facebook.com/")


def open_musicpage():
    mcontent = command().lower()
    url = "https://www.nhaccuatui.com/tim-kiem?q=" + mcontent
    print(url)
    speak("Here are the search results ")
    webbrowser.open_new_tab(url)


def open_game():
    url = "http://game.granbluefantasy.jp/#mypage"
    print(url)
    webbrowser.open_new_tab("https://vi.y8.com/games/8ball_online")


def open_gmail():
    url = "https://gmail.com/"
    print(url)
    webbrowser.open_new_tab("https://gmail.com/")


def click():
    global content
    check = "hi"
    speak("What can i help you")
    while True:
        content.set("Please say 'hi' and start command.")
        text = command().lower()
        
        if text.count(check) > 0:
            speak("hello boss. What do you want")
            content.set("Hello boss. What do you want?")
            timeout = time.time() + 10
            while time.time() < timeout:
                text = command().lower()
                if text == " ":
                    continue
                else:
                    timeout = time.time() + 10

                health_text = ["how are you"]
                for query in health_text:
                    if query in text:
                        speak("I am fine, thank you")
                        content.set("I am fine, thank you!")
                        continue

                time_text = ["tell me the time", "what time is it"]
                for query in time_text:
                    if query in text:
                        now = datetime.now()
                        current_time = now.strftime("It's %H:%M")
                        print(current_time)
                        content.set(current_time)
                        speak(current_time)
                        continue

                google_text = ["google", "Google"]
                for query in google_text:
                    if query in text:
                        speak("search for")
                        print("search for")
                        content.set("Opening Google")
                        sleep(1)
                        search_google()
                        content.set("Google is opened")
                        continue

                youtube_text = ["youtube", "you tube", "you tu be", "YouTube", "Youtube"]
                for query in youtube_text:
                    if query in text:
                        speak("search for")
                        print("search for")
                        content.set("Opening Youtube")
                        sleep(1)
                        open_youtube()
                        content.set("Youtube is opened")
                        continue

                facebook_text = ["Facebook", "play book", "facebook"]
                for query in facebook_text:
                    if query in text:
                        content.set("Opening Facebook")
                        sleep(1)
                        open_facebook()
                        content.set("Facebook is opened")
                        continue

                mail_text = ["email", "gmail", "mail", "male", "Gmail"]
                for query in mail_text:
                    if query in text:
                        content.set("Opening Gmail")
                        sleep(1)
                        open_gmail()
                        content.set("Gmail is opened")
                        continue

                music_text = ["music", "Music"]
                for query in music_text:
                    if query in text:
                        speak("search for")
                        print("search for")
                        content.set("Opening Music")
                        sleep(1)
                        open_musicpage()
                        content.set("Music is opened")
                        continue

                game_text = ["game", "Game"]
                for query in game_text:
                    if query in text:
                        content.set("Opening Game")
                        sleep(1)
                        open_game()
                        content.set("Game is opened")
                        continue

                notepad_text = ["notepad", "Notepad"]
                for query in notepad_text:
                    if query in text:
                        speak("Opening Notepad")
                        content.set("Opening Notepad")
                        sleep(1)
                        os.startfile("C:\\Windows\\System32\\notepad.exe")
                        content.set("Notepad is opened")
                        continue

                calculator_text = [
                    "calculate",
                    "Calculate",
                    "Calculation",
                    "calculation",
                    "calculator",
                    "Calcualtor",
                ]
                for query in calculator_text:
                    if query in text:
                        speak("Opening Calculator")
                        content.set("Opening Calculator")
                        os.startfile("C:\\Windows\\System32\\calc.exe")
                        content.set("Calculator is opened")
                        continue

                out_text = ["bye", "goodbye", "out", "Out", "quit", "Quit"]
                for query in out_text:
                    if query in text:
                        speak("Goodbye. See you again")
                        quit()

            


if __name__ == "__main__":
    root = Tk()
    root.title("Virtual Assistant")
    root.geometry("400x500")
    root.resizable(0, 0)

    content = StringVar()

    recImg = PhotoImage(file="microphone.png")

    txtDisplay = Entry(root, background="#CCFFFF", fg="black", textvariable=content)
    txtDisplay.place(height="60px", width="500px")

    btnRec = Button(root, height=64, width=64, image=recImg, command=record, bd=0)
    btnRec.place(x=168, y=436)

    root.mainloop()
