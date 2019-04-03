# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:57:50 2019

@author: Dell
"""

from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010] # годы
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3] # ввп

# создание линейной диаграммы : годы по оси X, ввп по оси Y
plt.plot(years, gdp, color = 'red', linestyle = 'solid') # в отличии от книги параметр market не нужен



# добавление названия диаграммы
plt.title("Номинальный ВВП")

# добавление подписи к оси Y
plt.ylabel("Млрд $")

# добавление подписи к оси X
plt.xlabel("Годы")

# отображение диаграммы
plt.show()
print('\a')

xs = [i +0.1 for i, _ in enumerate(years)]
plt.bar(xs,gdp)
plt.show()

############## ЛИНЕЙНЫЕ ГРАФИКИ
variance = [1,2,4,8,16,32,64,128,256]
bias_squared = [256,128,64,32,16,8,4,2,1]
# суммарная ошибка
total_error = [ x + y for x,y in zip(variance,bias_squared)]
xs = [i for i, _ in enumerate(variance)]
plt.plot(xs, variance, 'g-', label = 'Дисперсия')
plt.plot(xs, bias_squared, 'r-.', label = 'Смещение^2')
plt.plot(xs, total_error, 'b:', label = 'Суммарная Ошибка')
# loc=9 наверху посередине
plt.legend(loc = 9)
plt.xlabel("Сложность модели")
plt.title("Компромисс между смещением и дисперсией")
plt.show()

plt.scatter(variance,bias_squared)
plt.show()