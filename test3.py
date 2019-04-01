# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 15:17:06 2019

@author: Dell
"""
"""
string = "Hello"
print(len(string))
for(i in range (10)):
    print(string[i])
"""
#строка
a=b=c=1
a,b,c = 1,"test",True
string = "Hello"
print("Первый элемент "+string[0])
print("Последний элемент "+string[-1])
print("Срез "+string[1:-1])
for i in range(5):
    print(string[i])

#Кортеж и лист
kortej1 = (string[0],string[2:-1])
kortej2 = ('n',)

#for i in range(5):
   # kortej1(i) = string[i]
    
print(kortej1)

listi = []

for i in range(5):
    listi.extend(string[i])
print(listi)
a =[3,7,23,47,1,0,-1]
print(a)
print("sorted")
print(sorted(a))
#генераторы списков
b = [i for i in range(1,10) if i !=5]
print(b)



string1 ="testing"
c = [i for i in string1]
print(c)

d = [i*i for i in range(10)]
print(d)


#dictionary


di ={"first":1,
     "second":2
     }

print("\n")

print(di["first"])

di["second"] = 4
print(di["second"])
print(di)