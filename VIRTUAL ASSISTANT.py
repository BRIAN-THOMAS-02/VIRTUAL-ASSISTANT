import speech_recognition as sr
import playsound
from gtts import gTTS
import webbrowser
import os
import subprocess
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyttsx3
import pyaudio
import vlc
import time
import win10toast
from win10toast import ToastNotifier
import pyautogui
import keyword
import datetime
from datetime import datetime
from datetime import date
from bs4 import BeautifulSoup
import re
import requests
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print("")
print(voices[1].id)
engine.setProperty('voice', voices[1].id)
newVoiceRate = 165
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


num = 1


def assistant_speaks(output):
    global num
    import playsound
    num += 1
    print("Assistant : ", output)

    toSpeak = gTTS(text=output, lang='en', slow=False)
    file = str(num) + ".mp3"
    toSpeak.save(file)

    playsound.playsound(file, True)
    os.remove(file)


def get_audio():
    import speech_recognition as sr
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print(" ")
        print("Listening...")
        audio = rObject.listen(source, phrase_time_limit=5)

        try:
            text = rObject.recognize_google(audio, language='en-us')
            print("You said... :", str.capitalize(text))
            print(" ")
            return text

        except:
            print(" ")
            print("Could not understand you, PLease try again !")
            speak("Could not understand you, PLease try again !")
            print(" ")
            return 0


def reminder_seconds():
    global reminder_sec
    import win10toast
    from win10toast import ToastNotifier
    import time
    from datetime import datetime

    print("What should I remind you...?")
    speak("What should I remind you...?")
    reason1 = get_audio()
    g = z
    now = datetime.now()
    g = [int(i) for i in g.split() if i.isdigit()]
    r = 60
    for r in range(0, r):
        if r in g:
            print("I have set a reminder for ", r, "secs")
            # speak("I have set a reminder for " + r + "secs")
            current_sec = (now.second)
            current_min = (now.minute)
            current_hour = (now.hour)
            print("Current Time = ", current_hour, ":", current_min, ":", current_sec)
            reminder_sec = current_sec + r
            if reminder_sec <= 60:
                print("Notify at...", current_hour, ":", current_min, ":", reminder_sec)
                # speak("Notify at " + reminder_sec)
                time.sleep(r - 0.6)
                print(" ")
                print("I'm reminding you to " + str(reason1))
                speak("I'm reminding you to " + str(reason1))
                toaster = ToastNotifier()
                toaster.show_toast("Sir " + str.upper(reason1), duration=5)

            else:
                extra_sec = reminder_sec - 60
                extra_seconds = extra_sec + 0
                print("Notify at...", current_hour, ":", current_min, ":", extra_seconds)
                time.sleep(r - 0.6)
                print(" ")
                print("I'm reminding you to " + str(reason1))
                speak("I'm reminding you to"), speak(str(reason1))
                toaster = ToastNotifier()
                toaster.show_toast("Sir " + str.upper(reason1), duration=5)
                break


def write_content():
    while True:
        keyword = get_audio()
        if "continue" in str(keyword).lower():
            while True:
                global writing
                writing1 = get_audio1()
                writing = str(writing1)

                if "next line" in str(writing1).lower():
                    pyautogui.press("enter")

                if "bold" in str(writing1).lower():
                    pyautogui.keyDown("ctrl")
                    pyautogui.press("b")
                    pyautogui.keyUp("ctrl")

                if "italics" in str(writing1).lower():
                    pyautogui.keyDown("ctrl")
                    pyautogui.press("i")
                    pyautogui.keyUp("ctrl")

                if "underline" in str(writing1).lower():
                    pyautogui.keyDown("ctrl")
                    pyautogui.press("u")
                    pyautogui.keyUp("ctrl")

                if "left align" in str(writing1).lower():
                    pyautogui.keyDown("ctrl")
                    pyautogui.press("l")
                    pyautogui.keyUp("ctrl")

                if "right align" in str(writing1).lower():
                    pyautogui.keyDown("ctrl")
                    pyautogui.press("r")
                    pyautogui.keyUp("ctrl")

                if "center align" in str(writing1).lower() or "centre align" in str(writing1).lower():
                    pyautogui.keyDown("ctrl")
                    pyautogui.press("e")
                    pyautogui.keyUp("ctrl")

                sd = (writing.replace("Centre align", " ").replace("next line", " ").replace("left align", " ").replace(
                    "right align", " ").replace("bold", " ").replace("underline", " ").replace("italics", " "))
                pyautogui.write(sd)
                pyautogui.press('space')
                continue

                if "stop typing" in str(sd).lower():
                    global seconds5
                    seconds1 = (datetime.now() - start).seconds
                    seconds5 = int(seconds1)
                break
            break


def get_audio1():
    import speech_recognition as sr
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print(" ")
        print("Listening...")
        audio = rObject.listen(source, phrase_time_limit=6)

        try:
            text = rObject.recognize_google(audio, language='en-us')
            print("You said... :", str.capitalize(text))
            print(" ")
            return text

        except:
            print(" ")
            print("PLease try again...")
            speak("PLease try again...")
            print(" ")
            return 0


def news_top_scroll():
    # text = soup.find("h1").get_text()
    print("")
    print(
        "-------------------------------------------------------------Top News-------------------------------------------------------------")
    speak("Top News")
    print("")
    print(soup.find('div', class_='cont_cmn big_mid').get_text())
    speak(soup.find('div', class_='cont_cmn big_mid').get_text())
    print(soup.find('div', class_='sponscont').get_text())
    speak(soup.find('div', class_='sponscont').get_text())
    print(soup.find('div', class_='comn_cnt').get_text())
    speak(soup.find('div', class_='comn_cnt').get_text())
    print(soup.find('div', class_='wid_stry').get_text())
    speak(soup.find('div', class_='wid_stry').get_text())
    print(soup.find('div', class_='shd_grd').get_text())
    speak(soup.find('div', class_='shd_grd').get_text())
    top_scroll_links = []
    for link in soup.findAll('a', attrs={
        'href': re.compile("topscroll")}):  # re.compile is for finding out text with common word "topscroll"
        top_scroll_links.append(link.get('href'))
        final_top_scroll_links = '\n'.join(top_scroll_links)
        top_scroll_list = final_top_scroll_links.split()
    print(top_scroll_list[0])


def big_stories():
    print("")
    print("-------------------------------------------------------------" + (soup.find('h2',
                                                                                       class_='section_head').get_text()) + "-------------------------------------------------------------")
    # speak(soup.find('h2', class_='section_head').get_text())
    print("")
    print(soup.find('div', class_='cont_cmn big-story-1227').get_text())
    speak(soup.find('div', class_='cont_cmn big-story-1227').get_text())
    links = []
    for link in soup.findAll('a', attrs={'href': re.compile("bigstory")}):
        links.append(link.get('href'))
        final_links = '\n'.join(links)
        big_stories_list = final_links.split()  # converting to list not spliting!!!!!
        x = big_stories_list[0]  # calling the first element in the list!!!
    print(x)


def top_stories():
    print("")
    print(
        "-------------------------------------------------------------Top Stories-------------------------------------------------------------")
    print("")
    print(soup.find('div', class_='featured_cont').get_text())  # best way to extract specfic text
    speak(soup.find('div', class_='featured_cont').get_text())
    links = []
    for link in soup.findAll('a', attrs={'href': re.compile("topstories")}):
        links.append(link.get('href'))
        final_top_stories_links = '\n'.join(links)
        top_stories_list = list(final_top_stories_links.split())
        s = top_stories_list[0]
    print(s)
    print("")


def li():
    for a in soup.findAll('div', class_='featured_cont'):
        a = a.get_text()
        print(a)


def opinion():
    print("")
    print(
        "-------------------------------------------------------------Opinion-------------------------------------------------------------")
    print("")
    # speak("Opinion")
    print(soup.find('div', class_='opinion_opt opinion-165').get_text())
    speak(soup.find('div', class_='opinion_opt opinion-165').get_text())
    # print(soup.find('div', class_='description').get_text())
    links = []
    for link in soup.findAll('a', attrs={'href': re.compile("ndtv_opinion")}):
        links.append(link.get('href'))
        opinion_links = '\n'.join(links)
        opinion_list = list(opinion_links.split())
        s = opinion_list[0]
    print(opinion_links)                # will give all the links
    # print(s)                          #will give only first link
    print("")


if __name__ == "__main__":

    i = 0
    while i < 10:
        i = i + 1
        nm = get_audio()
        if nm == 0:
            continue

        if "olivia" in str(nm).lower():  # or "" in str(nm).lower():
            print("Hey Brian, how can I help you...?")
            speak("Hey Brian, how can I help you...?")

        else:
            print("Speak my name")
            speak("Speak my name")
            continue

        break

    while True:
        text = get_audio()
        if text == 0:
            continue

        if 'reminder' in str(text).lower():
            z = str(text)
            reminder_seconds()

        if "open word" in str(text).lower():
            print(" ")
            print("Opening Microsoft Word...")
            speak("Opening Microsoft Word...")
            os.system("start Hands_free_test.docx")
            time.sleep(2)
            write_content1 = get_audio()
            if "start writing" in str(write_content1).lower():
                print(" ")
                print("Say Continue to Start Writing and Stop Typing to Stop Writing")
                speak("Say Continue to Start Writing and Stop Typing to Stop Writing")
                write_content()

        if 'search' in str(text).lower():
            text1 = text.replace("search", "")
            webbrowser.open_new_tab(text1)
            time.sleep(8)

        if "i need help in python" in str(text).lower():
            print("1. GeeksForGeeks")
            print("2. W3Schools")
            print("3. StackOverflow")
            print("")
            print("Which one would you want me to open...?")
            speak("Which one would you like me to open...?")
            site = get_audio()
            if "1" in str(site).lower() or "geeks for geeks" in str(site).lower():
                print(" ")
                print("Opening GeeksForGeeks")
                speak("Opening GeeksForGeeks")
                webbrowser.open("https://www.geeksforgeeks.org/python-programming-language/")

            if "3" in str(site).lower() or "w 3 schools" in str(site).lower():
                print(" ")
                print("Opening W3Schools")
                speak("Opening W3Schools")
                webbrowser.open("https://www.w3schools.com/python/")

            if "2" in str(site).lower() or "stack overflow" in str(site).lower():
                print(" ")
                print("Opening StackOverflow")
                speak("Opening StackOverflow")
                webbrowser.open("https://stackoverflow.com/questions/tagged/python")

            else:
                print("Invalid Input")
                speak("Invalid Input")

        if "open youtube" in str(text).lower():
            print(" ")
            print("Opening Youtube...")
            speak("Opening Youtube...")
            webbrowser.open('https://www.youtube.com/')

        if "open whatsapp" in str(text).lower():
            print(" ")
            print("Opening WhatsAppWeb...")
            speak("Opening WhatsAppWeb...")
            #subprocess.call('whatsapp.exe')
            webbrowser.open('https://web.whatsapp.com/')

        if "who made you" in str(text).lower() or "created you" in str(text).lower():
            print(" ")
            print("I have been created by a team.")
            speak("I have been created by a team")

        if "who are you" in str(text).lower() or "define yourself" in str(text).lower():
            print(" ")
            print("Hello, I'm Olivia. Your personal Assistant")
            print("I could get the date, time, day, open urls, open apps and all")
            speak("Hello, I'm Olivia. Your personal Assistant")
            speak("I could get the date, time, day, open yourls, open apps and all")

        if "time" in str(text).lower():  # or "tell the time" in str(text).lower() or "time kya hai" in str(text).lower():  # time
            import datetime
            current_time = datetime.datetime.now()
            print(" ")
            print("The Time is ", end="")
            print((current_time.hour), ":", (current_time.minute), ":", (current_time.second))
            tme = ((current_time.hour), (current_time.minute))
            speak("The Time is")
            speak(tme)

        if "date" in str(text).lower():
            import datetime
            from datetime import date
            today = date.today()
            print(today.strftime("Today is " + ("%A") + (" %d") + "-" + ("%b") + "-" + ("%Y")))
            if (today.strftime("%d") == "01"):
                speak(today.strftime("Today" + "is " + "%A" + "First"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "02"):
                speak(today.strftime("Today" + "is " + "%A" + "Second"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "03"):
                speak(today.strftime("Today" + "is " + "%A" + "Third"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "04"):
                speak(today.strftime("Today" + "is " + "%A" + "Fourth"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "05"):
                speak(today.strftime("Today" + "is " + "%A" + "Fifth"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "06"):
                speak(today.strftime("Today" + "is " + "%A" + "Sixth"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "07"):
                speak(today.strftime("Today" + "is " + "%A" + "Seventh"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "08"):
                speak(today.strftime("Today" + "is, " + "%A " + "Eight" + "of, " + "%b %Y "))
            elif (today.strftime("%d") == "09"):
                speak(today.strftime("Today" + "is " + "%A" + "Ninth"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "10"):
                speak(today.strftime("Today" + "is " + "%A" + "Tenth"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "11"):
                speak(today.strftime("Today" + "is" + "%A" + "Eleventh"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "12"):
                speak(today.strftime("Today" + "is" + "%A" + "Twelfth"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "13"):
                speak(today.strftime("Today" + "is" + "%A" + "Thirteenth"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "14"):
                speak(today.strftime("Today" + "is" + "%A" + "Fourteenth"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "15"):
                speak(today.strftime("Today" + "is" + "%A" + "Fifteenth"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "16"):
                speak(today.strftime("Today" + "is" + "%A" + "Sixteenth"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "17"):
                speak(today.strftime("Today" + "is" + "%A" + "Seventeenth"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "18"):
                speak(today.strftime("Today" + "is" + "%A" + "Eighteenth"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "19"):
                speak(today.strftime("Today" + "is" + "%A" + "Nineteenth"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "20"):
                speak(today.strftime("Today" + "is" + "%A" + "Twentieth"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "21"):
                speak(today.strftime("Today" + "is" + "%A" + "Twenty First"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "22"):
                speak(today.strftime("Today" + "is" + "%A" + "Twenty Second"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "23"):
                speak(today.strftime("Today" + "is" + "%A" + "Twenty Third"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "24"):
                speak(today.strftime("Today" + "is" + "%A" + "Twenty Fourth"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "25"):
                speak(today.strftime("Today" + "is" + "%A" + "Twenty Fifth"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "26"):
                speak(today.strftime("Today" + "is" + "%A" + "Twenty Sixth"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "27"):
                speak(today.strftime("Today" + "is" + "%A" + "Twenty Seventh"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "28"):
                speak(today.strftime("Today" + "is" + "%A" + "Twenty Eight"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "29"):
                speak(today.strftime("Today" + "is" + "%A" + "Twenty Ninth"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "30"):
                speak(today.strftime("Today" + "is" + "%A" + "Thirty"  "of " + "%b %Y "))
            elif (today.strftime("%d") == "31"):
                speak(today.strftime("Today" + "is" + "%A" + "Thirty First"  "of " + "%b %Y "))
            else:
                print("Invalid Date")

        if "day" in str(text).lower() or "din" in str(text).lower():  # or "what's the day" in str(text).lower() or "kaun sa din hai aaj" in str(text).lower():  # day
            import datetime
            now = datetime.datetime.now()
            print(" ")
            print("You don't know the day!!")
            speak("You don't know the day??")
            print("What a shame!")
            speak("What a shame!")
            print(" ")
            print("Today is " + (now.strftime('%A')))
            speak("Today is " + (now.strftime('%A')))

        if "open spotify" in str(text).lower():
            subprocess.call('spotify.exe')

        if "news" in str(text).lower():
            website = requests.get('https://www.ndtv.com/')
            soup = BeautifulSoup(website.content, 'html.parser')
            NDTV = str((soup.title.string)).center(250)
            print(NDTV)
            news_top_scroll()
            big_stories()
            top_stories()
            opinion()

        if "a joke" in str(text).lower():
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
            sound_file = vlc.MediaPlayer("D:\PYTHON\PROJECTS\Virtual_Assistant\Virtual_Assistant PROJECT\Laughing sound final.mp3")
            sound_file.play()
            time.sleep(4)

        if "some jokes" in str(text).lower():
            i12 = 0
            while i12 < 3:
                i12 = i12 +1
                jokes = pyjokes.get_joke()
                print(jokes)
                speak(jokes)
                sound_file = vlc.MediaPlayer("D:\PYTHON\PROJECTS\Virtual_Assistant\Virtual_Assistant PROJECT\Laughing sound final.mp3")
                sound_file.play()
                time.sleep(4)

        if "i don't like your voice" in str(text).lower() or "change your voice" in str(text).lower():
            print(voices[0].id)
            engine.setProperty('voice', voices[0].id)
            newVoiceRate = 160
            engine.setProperty('rate', newVoiceRate)

            print(" ")
            print("Hey I'm Asher")
            speak("Hey I'm Asher")
            print("Would you like to keep me...?")
            speak("Would you like to keep me?")

            voice = get_audio()
            if "yes" in str(voice).lower() or "yea" in str(voice).lower():
                print(" ")
                print("Cool!")
                speak("Cool !")
            elif "no" in str(voice).lower() or "nah" in str(voice).lower():
                print(" ")
                assistant_speaks("This is another voice")
                assistant_speaks("I hope you like me")

                av = get_audio()
                if "yes" in str(av).lower():
                    assistant_speaks("Yay!")
                elif "no" in str(av):
                    print(" ")
                    assistant_speaks("You're very rude")
                    assistant_speaks("You're expectations are too much")
                    assistant_speaks("I'm not a voice artist...!")
        break
