def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


some_val = True
some_val2 = False
print((add if some_val else subtract)(5, 7))  # 12
print((add if some_val2 else subtract)(5, 7))  # -2

a = (i for i in range(12))
print(type(a))

from functools import reduce


def add(c, b):
    return c + b


print(reduce(add, [0, 3, 5, 7, 9]))  # 24

from gtts import gTTS

from playsound import playsound

text_val = 'I have your'
tts = gTTS(text=text_val, lang='en', slow=False)
tts.save('text.mp3')
playsound('text.mp3')
