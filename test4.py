# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:01:35 2019

@author: Dell
"""

import random
#1 Сначала выведите третий символ этой строки
string1 = "testing string1"
print(string1[2])

#2 Во второй строке выведите предпоследний символ этой строки.
string2 = "testing string2"
print(string2[-2])

#3 В третьей строке выведите первые пять символов этой строки.
string3 = "testing string3"
print(string3[:5])

#4 В четвертой строке выведите всю строку, кроме последних двух символов.
string4 = "testing string4"
print(string4[:-2])

#5 В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).
string5 = "testing string5"
print(string5[::2])

#6 В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
string = "testing string"
print(string[1::2])

#7 В седьмой строке выведите все символы в обратном порядке.
print(string[::-1])

#8 В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего
print(string[::-2])

#9 В девятой строке выведите длину данной строки.
print(len(string))


##########################################
#1 Создайте список чисел, вывести минимальный и максимальный элемент списка.

spisok = [random.randrange(1,10) for _ in range(10)]
print(spisok)
print("MIN:",min(spisok))
print("MAX:",max(spisok))

#2 Заполнить список нулями и единицами, при этом данные значения чередуются, начиная с нуля
i=0
n=10
#n=int(input('Введите количество элементов:'))
zeroandone = []
for i in range(n):
    if i%2 == 0:
        zeroandone.append(0)
    else:
        zeroandone.append(1)
print(zeroandone)

#2 Заполнить список нулями, кроме первого и последнего элементов, которые должны быть равны единице.
array=[]
for i in range(n):
    if i == 0 or i==n-1:
        array.append(1)
    else:
        array.append(0)
print(array)

#3 Определите, есть ли в списке повторяющиеся элементы, если да, то вывести на экран это значение.
spisoknomber3 = [random.randrange(0,10) for _ in range(10)]
#spisoknomber3=[2,2,6,6,3,3,7,8,9,10,1]
print("spisok")
print(spisoknomber3)
povtor=[]
i=1
for i in sorted(spisoknomber3):
    if spisoknomber3[i] == spisoknomber3[i-1]:
        povtor.append(spisoknomber3[i])

print("Повторяющиеся элементы:",list(set(povtor)))

#4 Присвойте произвольную строку длиной 10-15 символов переменной ...
g=input('vvedite text:')
b=int(len(g))
c = int((b-4)/2)
d = c + 4
print(g[c:d])
