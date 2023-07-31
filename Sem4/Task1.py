#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
#Затем пользователь вводит сами элементы множеств.

import random

print("Введите длину первого массива: ")
n = int(input())
print("Введите длину второго массива: ")
m = int(input())

mass_1 = []
mass_2 = []
print("Введите элементы первого массива:")
for i in range(n):
    mass_1.append(int(input()))
    mass_1.append(random.randint(1, 20))
for j in range(m):
    mass_2.append(random.randint(1, 20))

print(mass_1)
print(mass_2)
mass_1.sort()
mass_2.sort()

mass_3 = list(set(mass_1 + mass_2))

print(mass_3)