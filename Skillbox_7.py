                # task_1     #Задание 1. Дом для семьи
                             # Максим написал программу, которая должна определять, подходит ли земельный участок
                             # для его семьи или нет.
                             # Живут они втроем, вот и условие будет таким же: если количество квадратных метров
                             # делится на 3, то участок подходит.

# for meters in 100, 90, 95, 87, 102:
#     if meters % 3 == 0:
#         print(meters, 'Подходит')
#     else:
#         print(meters, 'Не подходит')

            # task_2  Задание 2. Таблица степеней
            # Аркадию для выступления с докладом нужно выучить таблицу степеней для определённых чисел.
            # Правда, память у него работает довольно необычно, и ему проще учить их в нужном ему порядке.
            # Напишите программу, которая выводит вторую, третью и четвёртую степень для каждого числа в отдельной
            # строке (первая строка - степени для числа 3, вторая строчка - степени для числа 7 и т.д.). Числа: 3,7,5,6,4.


# numbers = [3, 7, 5, 6, 4]
#
# for num in numbers:
#     print(num**2, num**3, num**4)


                        # task_2 с усложнением.(Вложенный цикл for)

# for meters in 3, 7, 5, 6, 4:
#     for i in 2, 3, 4:
#         print(meters ** i, end=" ")
#     print()


        # task_3  Задача 3. Лотерея 2
        # Напишите программу для немного усложнённой версии задачи про выигрышные билеты.
        # Есть заранее известные номера билетов: 345, 19, 87, 1020 и 421 (можете брать свои номера,
        # не стесняйтесь). Теперь, билет считается выигрышным, если номер билета - трёхзначное число и оно делится на 5.
        # Выведете в консоль сообщение для каждого выигрышного билета и количество победителей.

# numbers = [345, 19, 87, 1020, 421, 545]
# count = 0
#
# for num in numbers:
#     if num >= 100 and num <= 999 and num % 5 == 0:
#         print(f'Билет: {num} является выигрышным!')
#         count += 1
#
# print(f'Количество победителей: {count}')

                            # Задача 1. Квадраты чисел
                            # Напишите программу, которая выводит квадраты чисел от 0 до 10.
                            # Для этого используйте цикл for и функцию range.

# for num in range(11):
#     print(num ** 2, end=' ')
# print()


                            # Задача 2. Кукушка
                            # Напишите программу, которая имитировала бы часы с кукушкой.
                            # В начале работы она спрашивает, который час, а затем нужное количество раз пишет “Ку-ку!”.


# time = int(input('Который час? : '))
#
# for i in range(time):
#     print('Ку-ку!')


                            # Задача 3. Любовь с первой цифры (цикл for)
                            # Перепишите программу из прошлого модуля, используя цикл for.
                            # Паша очень любит математику. Настолько сильно, что у него по всей комнате висят всякие
                            # таблицы умножения,
                            # сложения, какие-то графики, формулы. И теперь он захотел распечатать таблицу степеней
                            # двойки, у них как раз
                            # началась новая тема по информатике.
                            # Используя цикл for, выведите на экран для числа 2 его степени от 0 до 20.


# for i in range(21):
#     print(f'2 в степени {i} = {2 ** i}')


                           # Задача 1. Квадраты превратились в кубы
                           # Напишите программу, которая выводит кубы чисел (число в третьей степени),
                           # лежащих в диапазоне от 1 до 10


# for i in range(1, 10):
#     print(i ** 3, end=' ')
# print()


                            # Задача 2. Сумма чисел
                            # Напишите программу, где пользователь вводит любые два целых положительных числа.
                            # А программа суммирует все числа в диапазоне от первого до второго.
                            # Гарантируется, что первое введённое число всегда меньше второго.


# first_num = int(input('Введите первое число: '))
# second_num = int(input('Введите второе число: '))
# summ = 0
#
# for i in range(first_num, second_num + 1):
#     summ += i
# print(summ)


            # Задача 3. Поел — можно и поспать, поспал — можно и поесть
            # Напишите программу, разобранную в уроке.
            # У Саши интересный режим сна: он может проснуться когда угодно, хоть ночью, но засыпает всегда до того,
            # как наступит полночь, обычно в 23 часа. А ещё он очень любит поесть. Он ест каждый час и если съедает
            # больше 2000 калорий, то он просто падает спать. Напишите программу, которая поможет Саше понять, всё ли
            # с ним хорошо. Для этого нужно посчитать, сколько он всего съест калорий и сколько часов будет бодрым.


# wake_up = int(input('Во сколько проснулся: '))
# wake_hours = 0
# calories_sum = 0
# let = ' '
#
# for hour in range(wake_up, 23):
#     print(f'Сейчас {wake_hours + 1} час бодрствования')
#     calories = int(input('Сколько съел калорий?: '))
#     calories_sum += calories
#     #wake_hours += 1
#     if calories_sum > 2000:
#         print('Хорошо поел, теперь можно и поспать!')
#         break
#     wake_hours += 1
# if wake_hours == 1:
#     let = 'час'
# elif wake_hours <= 4:
#     let = 'часа'
# else:
#     let = 'часов'
# print(f'Саша бодрствовал {wake_hours} {let} и съел {calories_sum} калорий)


'''
    // Алгоритм нахождения простых чисел// Простым числом называется ,число которое делится на 1 и на само себя.
    В цикле for диапазон функции range указываем такой, чтобы исключить возможность деления на 1 и на само себя.Поэтому
    начало диапазона задаём 2 , а конец диапазона указываем вводимое число number , но в range конечное значение диапазона 
    не включаемо в сам диапазон ,поэтому исключаем возможность деления числа на само себя.
'''
                                 # The first release
number = int(input('Введите число: '))

isPrime = True
for divider in range(2, number):
    print(divider)
    if number % divider == 0:
        isPrime = False
        break

if isPrime:
    print('Число простое')
else:
    print('Число составное')

                                    # The second release


# number = int(input('Введите число: '))
#
# for divider in range(2, number):
#     print(divider)
#     if number % divider == 0:
#         print('Число составное')
#         break
# else:
#     print(f'Число {number} не делится без остатка не на одно число из данного диапазона, поэтому оно простое')


'''
Для работы с циклом for вы также можете использовать конструкцию for-else. Эта конструкция в Python позволяет выполнить
блок кода, если цикл for завершился нормально. Это может быть полезно, если вы хотите выполнить какие-то действия после
завершения цикла for.
Вы также можете использовать оператор break для остановки цикла внутреннего вложения for.
'''

for i in range(1, 5):
    if i % 3 == 0:
        print("Делимое найдено", i)
        break
    print(i, "Не делится без остатка! продолжаю искать")
else:
    print("Ни одного делимого не было найдено")
