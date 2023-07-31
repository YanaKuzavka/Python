#Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
#(т.е. не меньше заданного минимума и не больше заданного максимума)

import random

print("Введите длину списка: ")
lenn = int(input())
list_1 = []
for i in range(lenn):
    list_1.append(random.randint(-10, 10))
print(list_1)
print("Введите минимальный диапазон:")
minn = int(input())
print("Введите максимальный диапазон:")
maxx = int(input())
list_2 =[]
def Indexx(list_2):
    if maxx - 1 > lenn:
        return False
    for i in range(len(list_1)):
            if list_1[i] > 0:
                if i >= minn and i <= maxx:
                    list_2.append(i)
    print(list_2)
Indexx(list_2)