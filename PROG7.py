__all__ = ['check_area']
# Функции в Python
def hello_world():
    """
    Данная функция вывод надпись 'hello, world'
    в консоль
    """
    print('hello, world')


# print(hello_world.__code__.co_code)
hello_world()
hello_world()
help(hello_world)


# Функция с аргументами
def greet(name):
    print(f'Hello, {name}!')


greet('Elsa')
names = 'Joe', 'Bob', 'Lily'
for name in names:
    greet(name)


def speak(name: str, phrase: str):
    print(f'Hello, {name}. {name.capitalize()} says {phrase.lower()}')


for name in names:
    speak(name, 'Good Evening!')

speak('good evening', 'Jerry')
speak(name='Bob', phrase='Good morning')  # передача аргументов по ключевому слову
# Значения для позиционных аргументов идут первыми и только потом
# используются значения аргументов по ключевому слову
# speak(name='John', 'hello my friends')


def greet(names: list):
    for name in names:
        print(f'Hello, {name}!')


greet(['John'])
greet(['Bob', 'Yeale', 'Lily'])


def greet(*args):
    print(args)
    print(type(args))  # <class 'tuple'>


def greet(*names):
    print(names)
    print(type(names))  # <class 'tuple'>
    for name in names:
        print(f'Hello, {name}!')


greet('Bob')
greet('Lily', 'Tom', 'John')


def test_kwargs(**kwargs):
    print(type(kwargs))
    print(kwargs)


test_kwargs(abc='1', dbc='2', cba='3')

from typing import Callable
from operator import add, mul


def calc(*args: int, operation: Callable = add, **kwargs: str):
    result = 0
    for value in args:
        result = operation(result, value)
    print(result)
    print(args)
    print(kwargs)


# calc(1, 2, 3, 4, 5)
# calc(3, operation=mul)
calc(operation=add, _str='param 1', _str2='param 2')


def dict_viewer(values: dict[str, int]):
    print(values)


dict_viewer({'val1': 1})
dict_viewer({'val2': 'str'})


def speaker(name: str = 'Jane'):
    voiceline = f'Hello from {name}! Nice to meet you.'
    return voiceline


result = speaker('John')
print(result)
result = speaker()
print(result)


def calc(*args: int) -> tuple:
    adds, muls = 0, 1
    for value in args:
        adds += value
        muls *= value
    return adds, muls


result = calc(1, 2, 3, 4)
print(type(result))
print(result)


def hello_world():
    """
    Данная функция вывод надпись 'hello, world'
    в консоль
    """
    return 'hello, world'


result = hello_world()
print(result)
print('*' * 50)
# Области видимости переменных
value = 10
print(value)

for value in range(10, 0, -1):
    pass

print(value)

MY_CONST = None


def check_area(value: int = 0):
    value = 5
    print(f'Inner {value}')
    value += 1
    return value


value = 10
print(f'Outer {value}')
check_area()
print(f'Outer {value}')
print(check_area())


print(__name__)
