print("Hello,World!")
name = input(" Введите свое имя:")
name = "John"
print(name)  # ctrl-shift-alt-L это фарматирование текта
print(type(name))  # Это комментарий, узнаем тип данных переменной name
print("Привет,", name)
print("Привет," + name + "!")
print("Привет ,{}!".format(name))  # Работает на  python2 python3
print(f"Привет, {name}!")  # f-строки
name = "Bob"
surname = "Kennedy"
print(f'Hello,"{name} {surname}!"')
print(f"Hello,'{name} {surname}!'")
this_is_var = "world"
first_var = "hello"
print(this_is_var)
print("Привет,", name)
# \n- переход на новую строку
print('Hello', 'world', sep='_')  # sep-по умолчанию пробел
print('Hello', 'world', end='\n')  # end-по умолчанию \n
print('Hello', 'world', end='\t\t')
print('Hello', 'world', end='!')
print()

# ЗАДАНИЕ. Что будет на выводе???
print('*' * 80)

result = 2 ** 3 ** 4
print(result)

print('*' * 80)

print(163 % 100)

print('*' * 80)

result = "Яблоко"

if result == "яблоко":
    print(123)
else:
    result == "Апельсин"
    print(456)

print('*' * 80)

height = 170
weight = 70
lose_weight = True

if height >= 170 or weight >= 100 and lose_weight == True:
    print(2000)
elif height < 170 or weight < 100:
    print(2500)
else:
    print(1800)

print('*' * 80)

x = 100

if x == 99 and x / 0 == 0:
    print("hello")  # принт не сработает , потому что условие не выполнится на первом же сравнении

print('*' * 80)

x = 0
if x:
    x = 1
print(x == 1)  # выведет False

print('*' * 80)

# Сколько итераций будет выполнено в теле цикла?
x = 0
while x <= 10:  # у цикла будет 11 итераций
    print(x)
    x += 1

print('*' * 80)

# Чему будет равна переменная i после выполнения кода?
i = 99
for i in range(1, 10, 2):
    i += 1

print(i)  # выведет 10

print('*' * 80)

# Чему будет равна переменная i после выполнения кода?

i = 99

for i in range(1, 10, -2):
    i += 1

print(
    i)  # Выведет 99,потому что не будет переопределения переменной i, т.к. цикл не выполнится, границы и шаг в функции
# range выставлены не корректно.

print('*' * 80)

# Каким будет результат следующей операции и почему?

print("0550" == 550)  # выведет False, потому что число типа str не может быть равно числу типа int

print('*' * 80)

# Что будет выведено в консоль следующим кодом?

x, y = 0, 0

for i in range(5):
    for j in range(10):
        y += 1
    x += 1

print(x,
      y)  # выведет 5 50,т.к.здесь вложенный цикл т.е. за каждую итерации внешнего цикла(от 0 до 4) выполняется 10 итераций
# внутреннего цикла (от 0 до 9)


print('*' * 80)

# Исправьте код так, чтобы в итоге с его помощью можно было посчитать общее количество цифр больше пяти во всей
# последовательности (выберите несколько вариантов ответа):

n = int(input("Количество чисел в последовательности: "))
cipher_count = 0
for _ in range(n):
    new_number = int(input("Введите число: "))
    while new_number:
        if new_number % 10 > 5:
            cipher_count += 1
        new_number //= 10
else:
    print(f'Кол-во цифр,которые больше 5, в введёных числах = {cipher_count}')

print('*' * 80)

# Каким будет вывод в консоль при выполнении следующего кода?

print(0.1 + 0.1 + 0.1)  # выведет 0.30000000000000004

print('*' * 80)


# Каким будет результат работы кода?

def check_number(number):
    return count_number_len(number) > 4


def count_number_len(x):
    count = 0
    while x:
        count += 1
        x //= 10
    return count


x = 12344
if check_number(x):
    print("1")  # будет выведено "1", т.е. длинна числа больше 4 цифр
else:
    print("2")

print('*' * 80)


# Выберите причину и вариант исправления кода, чтобы после правок функция правильно считала длину числа:

# Некорректно прописано условие выхода из цикла. Нужно изменить while x на while x is not None

# Цикл не может обращаться к count, так как переменная создана вне цикла. Нужно внести операцию count = 0 внутрь цикла
# while

# Оператор return будет возвращать не только итоговый ответ, но и все промежуточные. Return нужно убрать

# Return прерывает работу функции и цикла, поэтому функция будет возвращать либо 1, либо None (если цикл не начнётся).
# Нужно вынести return из цикла, чтобы он выполнялся после того, как цикл будет завершён.

def count_number_len(x):
    count = 0
    while x:
        count += 1
        x //= 10
        #return count
    print(count)

count_number_len(1234)
