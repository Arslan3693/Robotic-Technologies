from gtts import gTTS
import random
import time
import playsound
import speech_recognition as sr
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
    if "Salom" in message:
        print("Salom aleykum")
    elif "Haer" in message:
        print("Salomat boling")
        exit()
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