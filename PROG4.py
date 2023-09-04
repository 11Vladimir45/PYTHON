# Условия
# if-elif-else (оператор ветвления)
EXPECTED_1 = 5
EXPECTED_2 = 55

#
# print('Угадай число!')
# # my_list = input('Введите числа через пробел: ').split()
# # value_1 = my_list[0]
# # value_2 = my_list[1]
# value_1, value_2 = input('Введите числа через пробел: ').split()
# if value_1.isdigit() is False:
#     exit(0)
# if not value_2.isdigit():
#     exit(0)
# value_1 = int(value_1)
# value_2 = int(value_2)
# if (value_1 == EXPECTED_1) and (value_2 == EXPECTED_2):
#     print('Вы выиграли!')

# score = int(input('Введите вашу оценку за тест: '))
# if score >= 90:
#     print('Отлично! Ваша оценка - A')
#     if score >= 95:
#         print('Приходите в деканат...')
# elif score >= 80:
#     print('Хорошо! Ваша оценка - B')
# elif score >= 70:
#     print('Удов.! Ваша оценка - C')
# elif score >= 60:
#     print('Ваша оценка - D. Повторите материал.')
# else:
#     print('Вы не сдали экзамен.')
#
# print('Завершение работы...')

# Циклы
# for
# для <каждого элемента> в <последовательности>:
#     <выполняем тело цикла>
for i in range(10):
    print(i)
print()
nums = [1, 2, 3, 4, 5, 6, 7]
nums.reverse()
for i in range(len(nums)):
    print(nums[i], end='')
print()
print('-' * 50)
# start, stop, step
for index in range(0, len(nums), 2):
    print(f'{index}-{nums[index]} ', end='')
# Отрицательный
print()
print('-' * 50)
for index in range(len(nums) - 1, 0, -1):
    print(f'{index}-{nums[index]} ', end='')
print()
for i in range(30, 10, -2):
    print(i)
print()
print('-' * 50)
# Итерация по элементам
nums = [1, 2, 3, 4, 5, 6, 7]
for num in nums[::-1]:
    print(num)
for letter in 'hello, world!'[::2]:
    print(letter)

# 1-8, 25, 32 из practice-handbook.pdf в тг
# Одно задание - один файл
# putanov_<номер задания>.py
# Внутри файла должен быть текст самого задания вверху файла в виде комментария
# Задания 3 и 4 решить через циклы
