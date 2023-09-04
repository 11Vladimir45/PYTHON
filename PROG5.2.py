from sys import getrefcount
# Кортежи (Tuple)
# Это упорядоченные наборы элементов (последовательность)
# Кортежи отличаются от списков тем, что кортежи неизменяемы
my_tuple = ()
print(my_tuple)
my_tuple = tuple()
print(my_tuple)
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
my_tuple = (1, 'Hello', ('Wo', 'rld'), [2, 3, 4], 5.6)
print(my_tuple)
my_tuple = 1, 'hello', 3.5
print(my_tuple)
mtp1, mtp2, mtp3 = (1, 'hello', 3.5)
print(mtp1, mtp2, mtp3)
# Разница между кортежем и списком
my_list_old = [1, 2, 3]
my_tuple_old = (1, 2, 3)
my_list_old.append(4)
my_list_new = my_list_old
my_tuple_new = my_tuple_old + (4,)
print(my_list_old is my_list_new)
print(my_tuple_old is my_tuple_new)
# Создание кортежа с одним элементом
value = (4)
print(value, type(value))  # 4 <class 'int'>
my_tuple = (4,)
print(my_tuple, type(my_tuple))  # (4,) <class 'tuple'>

# Изменение списка внутри кортежа возможна
my_tuple = (1, 2, [3, 4], 5, 6)
print(my_tuple)
my_tuple[2][0] = 100
print(my_tuple)
# Кортежи можно склеивать и умножать (повторять)
my_tuple = (1, 2, 3) + (4, 5, 6)
print(my_tuple)
my_tuple = (99, 98, 97) * 6
print(my_tuple)
# Склеивать можно только одинаковые типы данных (кортеж с кортежем (не список))
# my_tuple = (1, 2, 3) + [4, 5, 6]  # TypeError: can only concatenate tuple (not "list") to tuple
# my_tuple.index()
# my_tuple.count()
my_tuple = (1, 2, 3) + (4, 5, 6)
my_list = list(my_tuple)
print(my_list)
print(tuple(my_list))
mtp = tuple('hello')
print(mtp)
mlp = list('hello')
print(mlp)
print(str((1, 2, 3) + (4, 5, 6)))
my_str = '(1, 2, 3, 4, 5, 6)'
print(my_str)
print(getrefcount(my_str))
'''

'''
my_str = 'hello, world'
print(getrefcount(my_str))
print(getrefcount(mtp))
