import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except Exception as e:
        print(e)
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'send a message on whatsapp to' in command:
        contact = command.replace('send a message on whatsapp to', '')
        send_whatsapp_message(contact, "Hi, how are you?")
    else:
        search_results = wikipedia.search(command)
        if search_results:
            info = wikipedia.summary(search_results[0], sentences=1)
            print(info)
            talk(info)
        else:
            talk("Sorry, I couldn't find any information about that.")


def send_whatsapp_message(contact, message):
    try:
        pywhatkit.sendwhatmsg(f"+1234567890", message, 0, 0)  # Replace with the recipient's phone number
        talk(f"Message sent to {contact} successfully.")
    except Exception as e:
        print(e)
        talk("Sorry, I couldn't send the message.")


while True:
    run_alexa()
