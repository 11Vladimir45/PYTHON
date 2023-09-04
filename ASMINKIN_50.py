# 50. Проверка пароля на надежность. В данном упражнении вам необходимо написать функцию, проверяющую введенный пароль
# на надежность. Определим как надежный пароль, состоящий минимум из восьми символов и включающий хотя бы по одной букве
# в верхнем и нижнем регистрах и как минимум одну цифру. Функция должна возвращать True, если переданный в качестве
# параметра пароль отвечает требованиям надежности. В противном случае возвращаемым значением должно быть False.
# В основной программе необходимо запросить у пользователя пароль и оповестить его о том, является
# ли он достаточно надежным
from ASMINKIN_48 import generate_password   # импортируем только данную функцию
# from ASMINKIN_48 import *      # импортируем весь файл

print(f'_name_ASMINKIN_50.py is {__name__}')
def check_password(password):
    if len(password) >= 8:  # Проверка длины пароля (минимум 8 символов)
        uppercase = False
        lowercase = False
        digit = False
        for char in password:
            if char.isupper():
                uppercase = True
            elif char.islower():
                lowercase = True
            elif char.isdigit():
                digit = True
        if uppercase and lowercase and digit:  # Пароль содержит хотя бы одну букву в верхнем и нижнем регистрах и хотя бы одну цифру
            return True
    return False




# Запрос пароля у пользователя
#generate_password = input("Введите пароль:")
print('_'*80)
print(f'Введённый пароль:', generate_password())
print('_'*80)
print(f'Проверка надёжности пароля:')
print('_'*80)
# Проверка надежности пароля
if check_password(generate_password()):
    print("Ваш пароль является надежным!")
else:
    print("Ваш пароль не является надежным!")
