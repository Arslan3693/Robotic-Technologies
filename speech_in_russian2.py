import pyttsx3
from gtts import gTTS
from datetime import datetime, date,time
import random
import time
import playsound
import speech_recognition as sr
tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voice','ru')

for voice in voices:
    if voice.name == 'Vsevolod':
        tts.setProperty('voice',voice.id)
tts.say('Salom')
tts.runAndWait()
def listen_command():
    r = sr.Recognizer()
    r.pause_threshold = 0.5
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        our_speech = r.recognize_google(audio, language="ru")
        print("Вы сказали: "+our_speech)
        return our_speech
    except sr.UnknownValueError:
        return "ошибка"
    except sr.RequestError:
        return "ошибка"
def do_this_command(message):
    message = message.lower()
    if "привет" in message:
        tts.say('приветствую')
        tts.runAndWait()
    elif "салам" in message:
        tts.say('салам папалам')
        tts.runAndWait()
    elif "как дела" in message:
        tts.say('лучше чем у нигеров')
        tts.runAndWait()
    elif "сколько тебе лет" in message:
        tts.say('два дня, но уже я поумнее чем вы скромные люди')
        tts.runAndWait()
    elif "как тебя зовут" in message:
        tts.say('разработчики еще не определились')
        tts.runAndWait()
    elif "кто тебя создал" in message:
        tts.say('компания энджайн, детка')
        tts.runAndWait()
    elif "сколько время" in message:
        time_checker = datetime.now()
        say_time(f'время: {time_checker.hour} часов {time_checker.minute} минут.')
    elif "время" in message:
        time_checker = datetime.now()
        say_time(f'времяt: {time_checker.hour}часов {time_checker.minute}минут.')
    elif "пока" in message:
        # print("Salomat boling")
        tts.say('Пращай')
        tts.runAndWait()
        exit()
def say_time(msg):
    tts.say(msg)
    tts.runAndWait()
def say_message(message):
    voice = gTTS(message, lang="ru")
    file_voice_name = "_audio_"+str(time.time())+"_"+str(random.randint(0,100000))+".mp3"
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    # print("Голосовой ассистент: "+message)
if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)
        tts.runAndWait()