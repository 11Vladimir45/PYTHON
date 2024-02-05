# Строки
my_string = 'hello,world!\t'
print(my_string)
my_string = "hello,world!\n"
print(my_string)
my_string = """
    hello,
    
        world
        !
"""
print(my_string)  # Тройные кавычки сохраняют форматирование
my_string = '\n\thello,\n\n\n\t\tworld\n\t\t\t!'
print(my_string)
print('hello' + "world!")  # сложение строк
# Строки неизменяемы
value = 'vvvar'
result = value.replace('v', 'F', 2)  # заменяет все буквы v на F,2 -это индекс сколько букв  v надо заменить
print(value)
print(result)
var = 'hello,world!'
print(var.upper())  # HELLO,WORLD! пишет все буквы большие заглавные
print(var.capitalize())  # Hello,world! пишет строку с заглавной буквы
print(var.lower())  # hello,world! пишет всю строку с маленькими буквами т,е, переводит в нижний регистр
print("-" * 80)
# Срезы строк работают для любых контенерных типов данных(строки,списки,кортежи)
# Cрез может в себе содержать только целые числа
my_string = "hello, world!"
print(f'Index 1:{my_string[1]}')  # Index 1: e
print(
    f'Hello slice: {my_string[0:3]}')  # Hello slice: Hel т,е происходит срез слова после буквы (n-1) т,е,после 2 {0,1,2}
print(f'Index -1: {my_string[-1]}')  # Index -1: !
print(f'world slice: {my_string[7:12]}')  # world slice:world
print(f'{my_string[:6]}')  # hello
print(f'{my_string[7:]}')  # world
print(f'{my_string[:]}')  # hello, world!
print(f'{my_string[:]}')  # длина строки + (-index)
print(f'{my_string[-5:-1]}')  # orld
print(f'{my_string[1:-1]}')
from sys import getsizeof

print('*' * 80)
print(getsizeof('hello,world!'))
print('*' * 80)
# Числа int/float
value = 1
print(value)
value = 1.3
print(value)
value = 0.1 + 0.1 + 0.1
print(value == 0.3)
print(7 + 8)
print(7 - 8)
print(7 * 8)
print(8 / 8)
print(8 // 7)
print(8 % 7)
print(8 ** 8)
print(1_000_000_000)
print(1_0)
print('-' * 50)

# bool
true = True  # 1
false = False  # 0
# Привидение типов данных
print(bool(0))  # False
print(bool(1))  # True
print(bool(-1))  # True
print(bool(1000000))  # True
print(bool(False))
print(bool(True))
print('*'* 80)

# Если обьект пустой,то-False , иначе True
print(bool(''))
print(bool('abcd'))
print(int('123'))
print(str(456))
print(float('123.6'))
print(int(15.6))
print(float(5))
print('*'* 80)

# Округление чисел
print(round(1.5))
print(round(2.65))
print(round(2.56, 1))
print(round(1.558, 2))

x = 256
y = 256
print(x is y)
x = 257
y = 257
print(x is y)
