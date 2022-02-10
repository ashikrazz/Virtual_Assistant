import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice',voices[1].id)

def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.......')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is'+time)
    elif 'play' in command:
        song = command.replace('play','')
        talk('Playing'+song)
        pywhatkit.playonyt(song)
    elif 'date' in command:
        talk('Sorry Ashik, i have a boyfriend his name is wifi. You go alone.')
    elif 'are you single' in command:
        talk("I am in a relationship with wifi")
    elif 'who are you' in command:
        talk('I am Alexa, Your virtual assistance')
    elif 'do you know me' in command:
        talk('Yes, you are my creator and i call you Ashik.')
    elif 'tell me about' in command:
        look_for = command.replace('tell me about','')
        info = wikipedia.summary(look_for,1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif "stop" in command:
        talk('ok thank you')
        exit()
    else:
        talk('I did not get it I am going to search for you')
        pywhatkit.search(command)



while True:
    run_alexa()