import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

try:
    with sr.Microphone() as source:
        print("Adjusting for noise...")
        listener.adjust_for_ambient_noise(source)
        print("Listening...")
        voice = listener.listen(source)
        print("Recognizing...")
        command = listener.recognize_google(voice)
        print("You said:", command)
        talk("You said " + command)

except Exception as e:
    print("There was an error:")
    print(e)
    talk("Sorry, I did not catch that.")
