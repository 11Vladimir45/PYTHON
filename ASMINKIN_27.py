# 27. Гласные и согласные. Разработайте программу, запрашивающую у пользователя букву латинского алфавита.
# Если введенная буква входит в следующий список (a, e, i, o или u), необходимо вывести сообщение о том, что эта буква гласная.
# Если была введена буква y, программа должна написать, что эта буква может быть как гласной, так
# и согласной. Во всех других случаях должно выводиться сообщение о том, что введена согласная буква
letter = input('Введите букву:')
print(letter)
if letter.lower() in ('a', 'e', 'i', 'o', 'u'):
    print('vowel letter')
elif letter.lower() == 'y':
    print("Эта буква может быть как гласной, так и согласной.")
else:
    print('consonant letter')