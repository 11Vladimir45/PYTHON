# # Task 33
# args = []
# flag = True
# while flag:
#     var = int(input("Введите значение: "))
#     if var == 0:
#         flag = False
#     args.append(var)
# print(args)
# sum(args) / len(args)
# Словарь Dict
my_dict = {}
print(my_dict)
my_dict = dict()
print(my_dict)
# Ключ: значение
my_dict = {
    'name': 'Bob',
    'job': 'dev',
    'age': 40
}
print(my_dict)  # {'name': 'Bob', 'job': 'dev', 'age': 40}
my_dict = {
    1: 'Bob', 2: 'dev', 3: 40
}
print(my_dict)
my_dict = {
    (1, 1): 'X',
    (1, 2): 'Y',
    (1, 3): 'Z',
}
my_list1 = [0, 1, 2]
my_list2 = [((1, 1), 'X'), ((1, 2), 'Y',), ((1, 3), 'Z')]
print(my_dict)
# my_dict = {
#     (1, [2, 3]): 'X'
# }
print(my_dict)
print(hash(123))  # Хеш числа всегда один
print(hash(256))
print(hash(89448187886880108))
# 6254291519441760108 -> ('str', 123) -> ('str1', 321)
print(hash('str'))
print(hash('str'))
# Создание словаря по ключевым словам
my_dict = dict(name='Bob', job='dev', age=40)
print(my_dict)  # {'name': 'Bob', 'job': 'dev', 'age': 40}
my_dict = dict([(1, 2), (2, 3), (4, 5)])
print(my_dict)  # {1: 2, 2: 3, 4: 5}
my_dict = {
    'name': 'Bob',
    'job': ['dev', 'manger', 'boss'],
    'age': [[[[49]]]]
}
print(my_dict)
my_dict = {
    'employees': {
        'Bob': 'dev',
        'Jane': 'manager',
        'John': 'boss'
    }
}
print(my_dict)
# Доступ к элементам
my_dict = {
    'name': 'Bob',
    'job': 'dev',
    'age': 40
}
value = my_dict['name']
print(value)  # Bob
# value = my_dict['abcd']
# print(value)
value = my_dict.get('job')
print(value)  # dev
value = my_dict.get('abcd')
print(value)  # None
value = my_dict.get('abcd', 'default')
print(value)  # default
# Изменение значений
my_dict = {
    'name': 'Bob',
    'job': 'dev',
    'age': 40
}
print(my_dict)
my_dict['name'] = 'Jane'
print(my_dict)
my_dict['abcd'] = None
print(my_dict)
print('-' * 30)
# Методы словарей
# update - обновление и добавление значений
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares)
squares.update({6: 36})
print(squares)
squares.update({1: 3, 2: 5, 3: 10})
print(squares)
print('*'*70)
# Вывод ключей и значений
for i in squares.items():
    print(i)
# Вывод только ключей
print(squares.keys())  # dict_keys([1, 2, 3, 4, 5, 6])
# Вывод только значений
print(squares.values())  # dict_values([3, 5, 10, 16, 25, 36])
# Удаление значений
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# Удаление методом pop с возвратом значения
value = squares.pop(5)
print(value)
# value = squares.pop(9)  # Удаление методом pop несущ ключа приведет к ошибке KeyError: 9
# print(len(squares))
# Удаление методом popitem последнего (-1) элемента c возвратом самого значения в формате (ключ, значение)
print(squares)
value = squares.popitem()
print(value)
print(squares)
# Очистка словаря
squares.clear()
print(squares)
my_dict = {
    'key_1': [1, 2, 3],
    'key_2': (1, 2, 3, ['hello'], ('world',))
}
print(my_dict)
from operator import add, mul, sub
my_dict = {
    '+': add,
    '*': mul,
    '-': sub
}
oper = my_dict['+']
result = oper(1, 2)
print(result)
oper = my_dict['-']
result = oper(result, 5)
print(result)
oper = my_dict.get(')', add)
result = oper(result, 5)
print(result)

# Оператор In со словарями
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(1 in squares)  # True
print(9 in squares)  # False
# =
print(1 in squares.keys())  # True
print(9 in squares.keys())  # False

print(1 not in squares.keys())  # False
print(9 not in squares.keys())  # True
# Проверка на наличие значения
print(9 in squares.values())  # True
print(2 in squares.items())  # False
print((1, 1) in squares.items())  # True
print((5, 20) in squares.items())  # False
print((5, 25) in squares.items())  # True
# Множества Sets
# Это изменяемая неупорядоченная группа элементов, в которой сами элементы неизменяемы
my_set = set()
print(my_set)  # {}
my_set = {}
print(type(my_set), my_set)
my_set = {1, 2, 3, 4, 5}
print(my_set)
my_set = {1, 'hello', 1.5, (1, 2, 3)}
print(my_set)
my_set = {1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4}  # {1, 2, 3, 4}
print(my_set)
print(len(my_set))
# print(my_set[2])  # TypeError: 'set' object is not subscriptable
# my_set = {'world', [1, 2, 3], {'name': 'bob'}, {4, 5}}  # TypeError: unhashable type: 'list'
# my_set = {(1, 2, [3, 4])}
# print(my_set)  # TypeError: unhashable type: 'list'
# my_set = {1, 2, 3} + {4, 5}  # TypeError: unsupported operand type(s) for +: 'set' and 'set'
# Изменение множеств
print(my_set)
my_set.add(5)  # Добавление одного элемента
my_set.add('hello')
my_set.add((6, 7))
print(my_set)
# Добавление нескольких элементов
my_set.update([5, 6, 7])
print(my_set)
my_set.update((8, 9))
my_set.update('hello, world')
print(my_set)
# Удаление элементов из множества
my_set = set('hello, world!')
print(my_set)
# pop - удаляет случайный элемент
# my_set.pop(4)  # TypeError: set.pop() takes no arguments (1 given)
my_set.pop()
print(my_set)
# remove - удаление значения из множества с вызовом ошибки, если элемента нет
my_set.remove('e')
print(my_set)
# my_set.remove('e')  # KeyError: 'e'
# print(my_set)
# discard - удаление значения из множества с без вызова ошибки, если элемента нет
my_set.discard('e')
print(my_set)
print(my_set.__dir__())
