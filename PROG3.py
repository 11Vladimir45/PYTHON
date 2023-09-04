# Списки
my_list = [1, 2.3, 'str', True]
print(my_list)
my_list = list()
print(my_list)
my_list = ['World', [1, 2, 3], 4, [5, 6, 7], ['H'], 'ello']
print(my_list)
# Индексация
#           0           1      2      3        4       5
my_list = ['World', [1, 2, 3], 4, [5, 6, 7], ['H'], 'ello']
print(my_list[0])  # World
print(my_list[-2])  # ['H']
# print(my_list[99])  # IndexError: list index out of range
print(my_list[1][1])  # 2
print(my_list[0][2])  # r
print(my_list[3][0]) # 5
print(my_list[2]) # 4
my_list = 'h e l l o , w o r l d !'.split(sep=' ')
print(my_list)  # ['h', 'e', 'l', 'l', 'o', ',', 'w', 'o', 'r', 'l', 'd', '!']
my_list = 'hello,world!'.split(',')
print(my_list) # ['hello', 'world!']
my_list = 'hello,world!'.split('l')
print(my_list)  # ['he', '', 'o,wor', 'd!']
my_list = ['h', 'e' 'l', 'l', 'o' ',', 'w', 'o' 'r', 'l', 'd' '!']
print(my_list) # ['h', 'el', 'l', 'o,', 'w', 'or', 'l', 'd!']
# my_list = ['he', 'llo' True, False True, 1, 2 3]  # SyntaxError: invalid syntax. Perhaps you forgot a comma?
# print(my_list)
my_list = ['he', 'llo', True, False, True, 1, 2, 3 , '=']
print(my_list)
print('-' * 50)
# Изменение значений
my_list = [2, 4, 6, 8]
print(my_list)
my_list[0] = 1
print(my_list)
my_list[0] = [1, 3, 5]
print(my_list) # [[1, 3, 5], 4, 6, 8]
my_list[1:1] = [1, 3, 5]
print(my_list) # [[1, 3, 5], 1, 3, 5, 4, 6, 8]
my_list[0:0] = [1, 3, 5]
print(my_list) # [1, 3, 5, [1, 3, 5], 1, 3, 5, 4, 6, 8]
# my_list[0:0] = 99  # TypeError: can only assign an iterable
# print(my_list)
my_list = [2, 4, 6, 8]
my_list[0:1] = [100, 101, 102]  # [100, 101, 102, 4, 6, 8]
print(my_list)
my_list[0:4] = [100, 101, 102]  # [100, 101, 102, 6, 8]
print(my_list)
my_list = [2, 4, 6, 8]
my_list[1:1] = [100, 101, 102]  # [2, 100, 101, 102, 4, 6, 8]
print(my_list)
my_list = [2, 4, 6, 8]
my_list[1:2] = [100, 101, 102]  # [2, 100, 101, 102, 6, 8]
print(my_list)
my_list = [2, 4, 6, 8]
my_list[2:3] = [100, 101, 102]  # [2, 4, 100, 101, 102, 8]
print(my_list)
print('-' * 50)
# Методы списков
my_list = [1, 3, 5]
# append - вставка в конец списка
my_list.append(7)
print(my_list)  # [1, 3, 5, 7]
my_list.append([9, 11, 13])
print(my_list)  # [1, 3, 5, 7, [9, 11, 13]]
my_list.append('hello')
print(my_list)  # [1, 3, 5, 7, [9, 11, 13], 'hello']
# extend - добавить значения из последовательности в конец списка
my_list.extend([15, 17, 19])
print(my_list)  # [1, 3, 5, 7, [9, 11, 13], 'hello', 15, 17, 19]
my_list.extend('world')
print(my_list)  # [1, 3, 5, 7, [9, 11, 13], 'hello', 15, 17, 19, 'w', 'o', 'r', 'l', 'd']
# my_list.extend(8)  # TypeError: 'int' object is not iterable
my_list = [1, 3, 4, 5]
# insert - вставка на определенную позицию (index, object)
my_list.insert(1, 2)
print(my_list)  # [1, 2, 3, 4, 5]
my_list.insert(3, [6, 7])
print(my_list)  # [1, 2, 3, [6, 7], 4, 5]
# count - Подсчет количества элементов в строке
my_list = 'h e l l o , w o r l d !'.split()
print(my_list.count('l'))
my_list = [4, 3, 1, 1, 1, 1, 2]
print(my_list.count(1))
print(my_list.count(99))
# index - индекс элемента (obj, start, stop)
print(my_list.index(1))
print(my_list.index(1, 1))
print(my_list.index(1, 2))
print(my_list.index(1, 3))
print(my_list.index(1, 0, 3))
# print(my_list.index(1, 0, 2))  # ValueError: 1 is not in list
my_list = [1, 2, 3, 4, 5]
if 6 in my_list:
    print(my_list.index(6))
print('')
if 3 in my_list:
    print(my_list.index(3))
print('-' * 50)
# Удаление методом remove без возврата значения
my_list = 'h e l l o , w o r l d !'.split()
print(my_list)
print(my_list.remove('e'))
print(my_list)
my_list.remove('l')
print(my_list)
# my_list.remove('99')  # ValueError: list.remove(x): x not in list
# Удаление методом pop по индексу с возвратом значения
my_list.pop(0)
print(my_list)
value = my_list.pop()  # POP без аргументов всегда удаляет последний
print(my_list)
print(value)
print('-' * 50)

# Сортировка списков
# Сортировать можно только элементы одного типа
my_list = [99, 9, 0, 1, 4, 3]
print(my_list)
my_list.sort()
print(my_list)
my_list = [99, 9, 0, 1, 4, 3, '1']  # ОШИБКА! РАЗНЫЕ ТИПЫ ДАННЫХ
print(my_list)
# my_list.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'
my_list = ['99', '9', '0', '1', '4', '3', '1', 'a', 'abc', '!', '?', '.']
print(my_list)
my_list.sort()
print(my_list)
print(ord('9'))  # 57 в таблице Unicode
print(ord('!'))  # 33
print(ord('?'))  # 63
# print(ord('99'))  # TypeError: ord() expected a character, but string of length 2 found
print('abc' > 'abw')
print('-' * 50)
my_list = [99, 9, 0, 1, 4, 3]
print(my_list)
my_list.sort(reverse=True)
print(my_list)
print(len('hello, world!'))
print(len([1, 2, 3, 4, 5]))

names = ['Bob', 'John', 'Jessica', 'Carl', 'Bern', 'Wendy']
names.sort()
print(names)  # ['Bern', 'Bob', 'Carl', 'Jessica', 'John', 'Wendy']

names = ['Bob', 'John', 'Jessica', 'Carl', 'Bern', 'Wendy']
names.sort(key=len)
print(names)

print('-' * 50)
from copy import copy,deepcopy
my_list_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_list_2 = my_list_1.copy()  # Поверхностное копирование
my_list_2 = deepcopy(my_list_1) # Полное копирование . Рекурсивное создание нового обьекта
print(my_list_1)
print(my_list_2)
print(my_list_1 is my_list_2)
my_list_2[-1][-1] = 'AA'
print(my_list_1)
print(my_list_2)
print(my_list_1 is my_list_2)

x = [1,2,3]
print(x)
x.append(x)
print(x)