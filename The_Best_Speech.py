import pyttsx3
from gtts import gTTS
from datetime import datetime, date,time
import random
import time
import playsound
import speech_recognition as sr
tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voice','uz')

for voice in voices:
    if voice.name == 'Sevinch':
        tts.setProperty('voice',200)
tts.say('Salom')
tts.runAndWait()
def listen_command():
    r = sr.Recognizer()
    r.pause_threshold = 0.5
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        our_speech = r.recognize_google(audio, language="uz")
        print("Siz aytiz: "+our_speech)
        return our_speech
    except sr.UnknownValueError:
        return "ошибка"
    except sr.RequestError:
        return "ошибка"
def do_this_command(message):
    message = message.lower()
    if "salom" in message:
        tts.say('Salom')
        tts.runAndWait()
    elif "assalomu alekum" in message:
        tts.say('Salom')
        tts.runAndWait()
    elif "nima gaplar" in message:
        tts.say('Kaley maley barmaley')
        tts.runAndWait()
    elif "enjan kompaniya haqida etib ber" in message:
        tts.say('Bugun brinchi kun ishlashim')
        tts.runAndWait()
    elif "sendayin kompaniya haqida etib berdi" in message:
        tts.say('Bugun brinchi kun ishlashim')
        tts.runAndWait()
    elif "sendayin kompaniyasi haqida etib ber" in message:
        tts.say('Bugun brinchi kun ishlashim')
        tts.runAndWait()
    elif "soat netchi" in message:
        time_checker = datetime.now()
        say_time(f'Voht: {time_checker.hour} soat {time_checker.minute} minut.')
    elif "soat necha" in message:
        time_checker = datetime.now()
        say_time(f'Voht: {time_checker.hour} soat {time_checker.minute} minut.')
    elif "soat nechi" in message:
        time_checker = datetime.now()
        say_time(f'Voht: {time_checker.hour} soat {time_checker.minute} minut.')
    elif "nechi soat" in message:
        time_checker = datetime.now()
        say_time(f'Voht: {time_checker.hour} soat {time_checker.minute} minut.')
    elif "xayr" in message:
        # print("Salomat boling")
        tts.say('Xayr')
        tts.runAndWait()
        exit()
def say_time(msg):
    tts.say(msg)
    tts.runAndWait()
def say_message(message):
    voice = gTTS(message, lang="uz")
    file_voice_name = "_audio_"+str(time.time())+"_"+str(random.randint(0,100000))+".mp3"
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    # print("Голосовой ассистент: "+message)
if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)
        tts.runAndWait()