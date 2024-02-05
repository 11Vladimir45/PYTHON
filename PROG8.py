# Рекурсия в Python
import sys
import datetime

print(sys.getrecursionlimit())
# sys.setrecursionlimit(990)
print(sys.getrecursionlimit())


def recursion_test():
    recursion_test()


# recursion_test() n!
def factorial_recursive(n: int) -> int:
    if n == 1:
        return n
    return n * factorial_recursive(n - 1)

print('-' * 78)
# Факториал числа - это число умноженное на каждое предыдущее вплоть до 1
# 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 = 5040
start = datetime.datetime.now()
result = 1
for i in range(1, 997):
    result *= i
print(result)

print('-' * 78)

print(datetime.datetime.now() - start)
start = datetime.datetime.now()
result = factorial_recursive(5)
print(result)
print(datetime.datetime.now() - start)
# factorial_recursive(5)
# factorial_recursive(4)
# factorial_recursive(3)
# factorial_recursive(2)
# factorial_recursive(1)
# return  5 * 4 * 3 * 2 * 1

print('-' * 78)

# Функции высшего порядка - функции, которые могут принимать в
# качестве аргумента функцию и возвращать функцию, как результат своей работы
# map, filter, reduce
# map - принимает функцию и итератор, возвращает итератор,
# элементами которого являются результаты применения функции к элементам итератора
nums = [1, 2, 3, 4, 5]


def add(x):
    return x ** 2


result = tuple(map(add, nums))
print(result)
result = tuple(map(str, nums))
print(result)
result = tuple(map(float, nums))
print(result)

print('-' * 78)

# filter - принимает функцию и итератор, возвращает
# итератор , элементами которого являются данные
# из исходного списка , для которых функция вернула True
nums = list(range(-2, 12, 2))
print(nums)


def check(num):
    if num >= 0:
        return True
    return False


result = filter(check, nums)
print(list(result))

print('-' * 78)

# reduce - принимает функцию и последовательность и возвращает один результат
from functools import reduce, partial
import operator

nums = list(range(1, 10))
print(nums)
result = reduce(operator.add, nums)
print(result)
result = reduce(operator.mul, nums)
print(result)
product = partial(reduce, operator.mul)
print(product([1, 2, 3, 5]))


# product = reduce(operator.mul, )
print('-' * 78)

# Замыкания
def talk(n: int, name: str):
    def hello():
        return f'Привет, {name}!'

    def goodbye():
        return f'Пока, {name}!'

    if n > 0:
        return hello
    return goodbye


print(talk(1, 'John')())
goodbye = talk(-2, 'Bob')
print(type(goodbye()), goodbye.__name__)
print(goodbye())


def mul(a: int):
    def helper(b: int):
        return a * b
    return helper


mul5 = mul(5)
print(mul5(4))
mul2 = mul(2)
print(mul2(4))

print('-' * 78)

# Декораторы
def first():
    print('Test function - 1')


def second():
    print('Test function - 2')

from functools import wraps

def decor(func):
    @wraps(func)
    def wrapper():
        print(f'Run function at {datetime.datetime.now()}')
        func()
        print(f'Stop function at {datetime.datetime.now()}')
    return wrapper


first_wrapped = decor(first)()
second_wrapped = decor(second)
second_wrapped()


@decor
def first():
    """
    test doc for first func
    :return:
    """
    print('Test function - 1')


first()
print(first.__name__)
print(first.__doc__)
print(help(first))
