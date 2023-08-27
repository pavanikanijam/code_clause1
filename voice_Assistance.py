import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
from tkinter import COMMAND

listener=sr.Recognizer()
engine=pyttsx3.init()

#voices=engine.getProperty('voices')
#engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_command():
    try:
        with sr.Microphone() as source:
            print("Bantu...working")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower() # type: ignore
            if 'bantu' in command:
                command=command.replace("bantu","")
                print(command)
            elif 'hey bantu' in command:
                talk('Your bantu here')
                talk('how can i help you')
    except:
        print("Ooops! mike is not working")
    
    return COMMAND

def run_bantu():
    command=get_command()
    if 'time' in command:
        time=datetime.datetime.now().strftime('%I %M %p')
        print(time)
        talk("Now time is"+time)

    elif 'date' in command:
        date=datetime.date.today().strftime('%B %d %Y')
        print(date)
        talk("Today is"+date)
    elif 'tell me about' in command:
        things=command.replace('tell me about','')  # type: ignore
        info=wikipedia.summary(things,2)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("i cannot understand")
        talk("can you tell me once again")

while 1:
    run_bantu()
