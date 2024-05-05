import datetime

now = datetime.datetime.now()
print("Now current date and time: ", now)
print(now.strftime('%Y-%m-%d %H:%M:%S'))
print(now.strftime('%H:%M:%S on %A, %B the %dth, %Y'))
print(f'Now current date and time: {now}')
print('*' * 80)

now_1 = datetime.datetime.utcnow()
moscow_now = now_1 + datetime.timedelta(hours=3)  # Московское время = UTC+3.
print(f'Я пишу этот код в {moscow_now} по московскому времени')

from gtts import gTTS
from translate import Translator
from playsound import playsound

result = f'Я пишу этот код в {moscow_now} по московскому времени'
translator = Translator(from_lang='ru', to_lang='en')
end_text = translator.translate(result)
text_val = end_text
tts = gTTS(text=end_text, lang='en', slow=False)
tts.save('text.mp3')
playsound('text.mp3')

v = 100
f = 215
print(f'Сумма равна: {v + f}')
result_1 = f'Вычисленная сумма равна {315}'
tts = gTTS(text=result_1, lang='ru', slow=False)
tts.save('text_1.mp3')
playsound('text_1.mp3')
