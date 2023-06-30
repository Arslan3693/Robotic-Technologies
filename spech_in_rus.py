import pyttsx3
tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voice','ru')
for voice in voices:
    if voice.name == 'Vsevolod':
        tts.setProperty('voice',voice.id)
tts.say('Привет братан')
tts.runAndWait()