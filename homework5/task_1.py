# Задача 1. Вводится два числа с клавиатуры. Выведите диапазон между этими двумя числами.
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
i = a
while i <= b:
    print(i)
    i += 1