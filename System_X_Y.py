import matplotlib.pyplot as plt

# Создаем данные для графика
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Строим график
plt.plot(x, y)

# Настраиваем оси графика и заголовок
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Пример графика')

# Отображаем график
plt.show()