# Найдите сумму цифр трехзначного числа n.
n = int(input('Введите трехзначное число: '))
n = int(n)
n1 = n // 100 # Нахождение первой цифры числа
n2 = (n % 100) // 10 # Нахождение второй цифры числа
n3 = n % 10 # Нахождение третьей цифры числа
res = n1 + n2 + n3
print("Сумма цифр числа:", res)