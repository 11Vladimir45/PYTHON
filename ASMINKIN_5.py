# 5. Пользователь вводит время в минутах и расстояние в километрах. Найдите скорость в м/c
time = float(input('Введите время в минутах:'))
long = float(input('Введите расстояние в км:'))
speed = (long * 1000) / (time * 60)
print(speed)
print(time)
