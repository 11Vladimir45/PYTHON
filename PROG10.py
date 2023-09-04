# Файлы
# Чтение файлов
# r - read
# w - write - перезаписывает файл
# a - append
# w+ - append
file = open('little_dorrit_1.txt', 'r', encoding='utf-8')
# result = file.read()
# print(result)
for line in file:
    print(line, end='')
file.close()
print('*' * 77)
# Менеджеры контекста with
# __enter__
# __exit__
with open('little_dorrit_1.txt', 'r', encoding='utf-8') as file:
    # for line in file:
    #     print(line)
    # result = file.readlines()  # возвращает список в котором элементами явл. строки из файла
    # print(file.readline())
    # It was a Sunday evening in London, gloomy, close, and stale. Maddening church bells of all degrees of dissonance,
    print(file.readline())  # считать 1 строку
    # sharp and flat, cracked and clear, fast and slow, made the brick-and-mortar echoes hideous. Melancholy streets,
    print(file.readline())  # считать 2 строку
    result = file.readline()  # считать 3 строку
# in a penitential garb of soot, steeped the souls of the people who were condemned to look at them out of windows,
print(result)
print('*' * 88)
# Запись в файл
with open('example.txt', 'w', encoding='utf-8') as w_file:
    # w - создает или перезаписывает файл
    w_file.write('hello, world!\n')


with open(r'C:\Users\Пользователь\PycharmProjects\pythonProject\PYTON\little_dorrit_1.txt', 'r', encoding='utf-8') as r_file, open(
        'new.txt', 'w', encoding='utf') as w_file:
    data = r_file.readlines()
    w_file.writelines(data)


# D:\PycharmProjects\nntu_march
with open('example_print.txt', 'w', encoding='utf-8') as file:
    for line in data:
        print(line, file=file, end='')


with open('example.txt', 'a', encoding='utf-8') as w_file:
    # a - добавляет в конец файла
    w_file.write('hello, world!!!\n')

import csv

rows = []
with open('addresses.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        rows.append(row)


with open('new_addresses.csv', 'w') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(row)
    writer.writerows(rows)
