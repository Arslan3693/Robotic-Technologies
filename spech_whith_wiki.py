# import wikipedia
# wikipedia.set_lang('ru')
# python_page = wikipedia.page('машина')
# print(python_page.html)
# print(python_page.original_title)
# print(python_page.summary)
import gtts
import speech_recognition
from playsound import playsound
import wikipedia
import webbrowser
def get_audio():
    recognition = speech_recognition.Recognizer()
    mic = speech_recognition.Microphone()
    with mic as audio_file:
        audio = recognition.listen(audio_file)
        text = ''
        try:
            text = recognition.recognize_google(audio,language='ru-RU')
        except Exception as e:
            print("Exeption: "+str(e))
        return text.lower()

wakeup = "гипс"
hello = gtts.gTTS("Слушаю, братан", lang="ru")
hello.save("hello.mp3")

wikipedia.set_lang("ru")

while True:
    print("Listening...")
    text = get_audio()
    if text.count(wakeup) > 0:
        print("I'm ready")
        playsound("hello.mp3")
        text = get_audio()
        print(text)
        if text.count("что такое") > 0:
            result = wikipedia.summary(text.replace("что такое ",""))
            info = gtts.gTTS(result,lang="ru")
            info.save("info.mp3")
            playsound("info.mp3")
            print(result)
        if text.count("открой интернет") > 0:
            webbrowser.get("chrome").open_new_tab("https://www.youtube.com")