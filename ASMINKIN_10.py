# 10. Приветствие. Напишите программу, запрашивающую у пользователя его имя.
# В ответ на ввод на экране должно появиться приветствие с обращением по имени, введенному с клавиатуры ранее
name = input(" Введите свое имя:")
if name == ('Vladimir'):
    print('Hello , Vladimir !')
    print(f"Привет, {name}!")
else:
    print('Это не моё имя')
