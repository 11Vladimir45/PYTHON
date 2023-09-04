nums = [1, 2, 3, 4, 5, 6, 7]
for num in nums:
    if num == 2:
        pass  # pass - ничего не делать
    elif num == 3:
        ...  # Заглушка, которая показывает, что код будет добавлен позже
    elif num == 4:
        print(f'Пропустим {num}')
        continue  # Continue позволяет пропустить итерацию цикла
    elif num == 6:
        print(f'Выход из цикла на {num}')
        break  # break - это остановить работу цикла
    print(num)
else:  # Блок исполнится только, если цикл отработает полностью (без применения break)
    print('Выполняется блок else...')
print('Конец работы!')

print('-' * 50)
# Цикл while
# пока <условие истинно>:
#   <выполняем тело цикла>
counter = 10
while counter >= 1:
    print(counter)
    counter -= 1
print()
print(counter)
print()
while counter >= 1:
    print(counter)
    counter -= 1
print('-' * 50)
# Циклы не создают новую область видимости переменных
x = 'Hello, World!'
print(x)
for x in range(10):
    pass
print(x)
print()
counter = 10
while bool(counter >= 1):
    print(counter)
    counter -= 1
    # if counter == 6:
    #     break
else:
    print(f'Цикл окончил свою работу с {counter=}')
# Бесконечный цикл
# while True:
#     ...
flag = True
while flag:
    ...
    flag = False