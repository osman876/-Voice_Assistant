import datetime
from threading import Event
import pyttsx3
import sys
import os
import operator
import pyautogui
import pywhatkit as kit
import requests
import subprocess
import speech_recognition as sr

from features.customvoice import speak

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
voicespeed = 140
engine.setProperty('rate',voicespeed)

            
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
     print("Recognizing....")
     query = r.recognize_google(audio, language='en-us')
     print(f"user said: {query}\n")
    except Exception as e:
      print(e)
      return "None"
    return query

def wakeupcommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("soni is sleeping....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
    try:
     query = r.recognize_google(audio, language='en-us')
     print(f"user said: {query}\n")
    except Exception as e:
      print(e)
      return "None"
    return query
    
def myself():
    speak('My Name Is soni')
    speak('I can Do Everything that my creator programmed me to do')
    
def refresh():
    pyautogui.moveTo(983,446,2)
    pyautogui.click(x=983, y=446, clicks=1, interval=0.5, button='right')
    pyautogui.moveTo(1021,520, 1)
    pyautogui.click(x=1021, y=520, clicks=1, interval=0.5, button='right')

def time():
    time = datetime.datetime.now().strftime('%H:%M:%S')
    speak(time)
    print(time)
 
def wishme():
    speak("Welcome back sir")
    
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak('Good morning')
    elif hour>=12 and hour<=18:
        speak('Good afternoon')
    elif hour>=18 and hour<=24:
        speak('Good evening')
    else:
        speak('Good night')
        
    speak('How can i help you today')
    
def openchrome():
    speak("opening google chrome sir")
    subprocess.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe"])
    while True:
        chromequery = takecommand().lower()
        if "maximize this window" in chromequery:
            pyautogui.hotkey("win","up")
        elif "search" in chromequery:
            chromequery1 = chromequery
            chromequery1 = chromequery1.replace("search","")
            pyautogui.write(chromequery1)
            pyautogui.hotkey("enter")
            speak("searching....")
        elif 'open new window' in chromequery:
            speak("opening new window")
            pyautogui.hotkey('ctrl', 'n')
        elif 'open incognito window' in chromequery:
            speak("opening incognito window")
            pyautogui.hotkey('ctrl', 'shift', 'n')
        elif "maximise this window" in chromequery or "maximize this window" in chromequery or "maximize window" in chromequery:
            speak("maximizing this window")
            pyautogui.hotkey("win","up")
        elif "minimise this window" in chromequery or "minimize this window" in chromequery or "minimize window" in chromequery:
            speak("minimizing this window")
            pyautogui.hotkey("win","down")
        elif "chrome in left" in chromequery:
            speak("chrome will be in left side")
            pyautogui.hotkey("win","left")
        elif "chrome in right" in chromequery:
            speak("chrome will be in right side")
            pyautogui.hotkey("win","right")
        elif "open history" in chromequery:
            speak("opening history")
            pyautogui.hotkey("ctrl","h")
        elif 'open downloads' in chromequery:
            speak("opening downloads")
            pyautogui.hotkey('ctrl', 'j')
        elif 'previous tab' in chromequery:
            speak("opening previous tab")
            pyautogui.hotkey('ctrl', 'shift', 'tab')
        elif 'next tab' in query:
            speak("opening next tab")
            pyautogui.hotkey('ctrl', 'tab')
        elif "open new tab" in chromequery or "open youtube" in chromequery or "open yo tab" in chromequery or "in new tab" in chromequery:
            speak("opening new tab")
            pyautogui.hotkey("ctrl","t")
        elif "close tab" in chromequery:
            speak("closing tab")
            pyautogui.hotkey("ctrl","w")
        elif 'close window' in chromequery or "close this window" in chromequery:
            speak("closing this window")
            pyautogui.hotkey('ctrl', 'shift', 'w')
        elif 'clear browsing history' in chromequery:
            speak("clearing browsing history")
            pyautogui.hotkey('ctrl', 'shift', 'delete')
        elif 'soni play' in chromequery or 'sony play' in chromequery:
            chromequery = chromequery.replace("soni play", "")
            chromequery = chromequery.replace("sony play", "")
            speak("playing " + chromequery)
            pyautogui.hotkey('alt', 'd')
            Event().wait(2)
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            Event().wait(2)
            pyautogui.write(chromequery)
            pyautogui.press('enter')
            Event().wait(1)
            pyautogui.moveTo(418,453,1)
            pyautogui.click(x=418, y=453, clicks=1, interval=0.5, button='left')
        elif 'exit chrome' in chromequery or 'close chrome' in chromequery:
            speak("leaveing chrome")
            break    
         
def shutdown():
    os.system("shutdown /s /t 1")
    
def restart():
    os.system("shutdown /r /t 1")

def open_V_Box():
    speak("opening virtual box")
    subprocess.Popen(["C:\Program Files\Oracle\VirtualBox\VirtualBox.exe"])

def opentor():
    speak("opening tor browser")
    subprocess.Popen([r"E:\Users\osman\OneDrive\Desktop\Tor Browser\Browser\firefox.exe"])
    
    
def open_vscode():
    speak("opening visual studio code")
    subprocess.Popen([r"E:\Users\osman\AppData\Local\Programs\Microsoft VS Code\Code.exe"])
    
def kali_linux():
    speak("opening kali linux")
    pyautogui.moveTo(57,542,1)
    pyautogui.click(x=57, y=542, clicks=1, interval=0.5, button='right')
    Event().wait(1)
    pyautogui.moveTo(117,159,1)
    pyautogui.click(x=117, y=159, clicks=1, interval=0.5, button='left')
    Event().wait(1)
    pyautogui.moveTo(1234,412,1)
    pyautogui.click(x=1234, y=412, clicks=1, interval=0.5, button='left')
    Event().wait(1)
    pyautogui.moveTo(886,121,1)
    pyautogui.click(x=886, y=121, clicks=1, interval=0.5, button='left')
"""    
def open_start_menu ():
    speak("opening start menu")
    pyautogui.moveTo(223,1056,1)
    pyautogui.click(x=223, y=1056, clicks=1, interval=0.5, button='left')
    Event().wait(1)
    speak("what do you wish to open")
    query = takecommand().lower()
    pyautogui.write(query)
    speak("opening " + query)
    Event().wait(1)
    pyautogui.moveTo(745,473,1)
    pyautogui.hotkey("enter")
"""
def open_file_explorer():
    speak("opening file explorer")
    subprocess.Popen(["C:\Windows\explorer.exe"])

def openvmware():
    speak("opening vmware")
    subprocess.Popen([r"E:\Program Files (x86)\VMware\VMware Workstation\vmware.exe"])
    
def closevmware():
    speak("closing vmware")
    os.system("taskkill /f /im vmware.exe")
       
def close_vscode():
    speak("closing visual studio code")
    os.system("taskkill /f /im Code.exe")
    
def closetor():
    speak("closing tor browser")
    os.system("taskkill /f /im firefox.exe")

def close_V_Box():
    speak("closing virtual box")
    os.system("taskkill /f /im VirtualBox.exe")
    
def closechrome():
    speak("closing chrome")
    os.system("taskkill /f /im chrome.exe")
    
def ipaddress():
    speak("Checking")
    try:
        ipAdd = requests.get('https://api.ipify.org').text
        speak("your ip adress is")
        speak(ipAdd)
    except Exception as e:
        speak("network is weak, please try again some time later")

    
def calculate():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("calculating")
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        my_string=r.recognize_google(audio)
        print(my_string)

        def get_operator_fn(op):
            return {
                '+' : operator.add,
                '-' : operator.sub,
                'multiplied' : operator.mul,
                '*' : operator.mul,
                'x' : operator.mul,
                'X' : operator.mul,
                '/' : operator.__truediv__,
            }[op]
        try:    
            def eval_bianary_expr(op1,oper, op2):
                op1,op2 = float(op1), float(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_bianary_expr(*(my_string.split())))
        except Exception as e:
            print(e)
            speak("unable to process")
            return None
    except Exception as e:
        print(e)
        return None

def screenpic():
    speak('tell me a name for the file')
    name = takecommand().lower()
    Event().wait(5)
    img = pyautogui.screenshot() 
    img.save(f"E:\screenshots\{name}.png") 
    speak("screenshot saved")
    
def youtube():
    speak("what do you want to play")
    query = takecommand().lower()
    speak("playing " + query)
    kit.playonyt(query)
    
def rightcursor():
    pyautogui.moveTo(1710,434,2)
    pyautogui.click(x=1710, y=434, clicks=1, interval=0.5, button='left')
    
def leftcursor():
    pyautogui.moveTo(177,476,2)
    pyautogui.click(x=177, y=476, clicks=1, interval=0.5, button='left')
    
def left():
    pyautogui.hotkey("win","left")

def right():
    pyautogui.hotkey("win","right")
           
def stop_execution():
    sys.exit()
    
if __name__ == "__main__":
    #wishme()
    while True:
        query = wakeupcommands().lower()
        if "wake up" in query:
            wishme()
            while True:
                query = takecommand().lower()
                print(query)
                
                if "good morning" in query:
                    speak("good morning sir")
                elif "good afternoon" in query:
                    speak("good afternoon sir")
                elif "good evening" in query:
                    speak("good evening sir")
                elif "time" in query:
                    time()
                elif "go to sleep" in query:
                    speak("i am going to hybernation sir")
                    break
                elif "relax" in query:
                    speak("ok sir,i am switching off and giving control to you")
                    stop_execution()
                elif "shutdown" in query:
                    speak("system is shutting down")
                    shutdown()
                elif "restart" in query:
                    speak("system is now restarting")
                    restart()
                #chrome automation commands
                elif "open chrome" in query:
                    openchrome()
                elif "close chrome" in query:
                    closechrome()
                elif "make volume" in query or "volume up" in query or "increase the volume" in query:
                    speak("volume high")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")    
                elif "volume low" in query or "decrease the volume" in query:
                    speak("volume low")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                elif "mute" in query:
                    pyautogui.press("volumemute")
                elif "calculate" in query:
                    calculate()
                elif "open virtualbox" in query:
                    open_V_Box()
                elif "open virtual box" in query:
                    open_V_Box()
                elif "close virtual box" in query:
                    close_V_Box()
                elif "take screenshot" in query or "take a screenshot" in query:
                    screenpic()
                elif "who are you" in query:
                    myself()
                elif "what is your name" in query:
                    myself()
                elif "open web" in query:
                    opentor()
                elif "close web" in query:
                    closetor()
                elif "hey soni" in query:
                    speak("yes boss, how can i help you")
                elif "open vs code" in query:
                    open_vscode()
                elif "close vs code" in query:
                    close_vscode()
                elif "refresh" in query:
                    refresh()
                elif "what is my ip address" in query:
                    ipaddress()
                elif 'open youtube' in query:
                    youtube()
                elif "open linux" in query:
                    kali_linux()
                elif "open files" in query or "open file explorer" in query:
                    open_file_explorer()
                elif "open vmware" in query:
                    openvmware()
                elif "close vmware" in query:
                    closevmware()
                elif "move right" in query:
                    rightcursor()
                elif "move left" in query:
                    leftcursor()
                elif "left side" in query:
                    left()
                elif "right side" in query:
                    right()