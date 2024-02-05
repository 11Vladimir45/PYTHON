import speech_recognition as sr
from translate import Translator
from gtts import gTTS
from playsound import playsound
import os
import time


record = sr.Recognizer()
microphone = sr.Microphone()

try:
    while True:
        with microphone as source:
            record.adjust_for_ambient_noise(source)
            audio = record.listen(source)
            result = record.recognize_google(audio, language='ru_RU')
            result = result.lower()
            print(format(result))
            translator = Translator(from_lang='ru', to_lang='en')
            end_text = translator.translate(result)
            print(end_text)
            text_val1 = end_text
            language = 'en'
            obj = gTTS(text=text_val1, lang=language, slow=False)
            obj.save('text3.mp3')
            time.sleep(0.1)
            playsound('text3.mp3')
            os.remove('text3.mp3')

except sr.UnknownValueError:
    print('Сервис Google не отвечает')



