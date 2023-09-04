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
