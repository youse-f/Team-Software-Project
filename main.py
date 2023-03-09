import speech_recognition as sr
import pyttsx3
import time as t

listener = sr.Recognizer()
audio = pyttsx3.init()
vocals = audio.getProperty('voices')
audio.setProperty('voice', vocals[1].id)


def get_voice_ar(): #Speech_to_text in Arabic
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)   #Get_voice
        vo = listener.recognize_google(voice, language='ar-EG')   #Recognize_Voice
        vo = vo.capitalize()
        print(vo)


def get_voice_en(): #Speech_to_text in English
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)   #Get_voice
        vo = listener.recognize_google(voice, language='en-US')   #Recognize_Voice
        vo = vo.capitalize()
        return vo


def text_to_speech():
    n = input('Enter text to translate: ')
    t.sleep(0.5)
    audio.say(n)
    audio.runAndWait()
