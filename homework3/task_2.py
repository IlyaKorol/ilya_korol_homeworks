# Задача 2. Вводится число, как строка, в клавиатуры. Необходимо проверить делится ли оно на 5 и вывести «Yes» или «No». Также проверить делится ли оно на 4 и вывести «Yes» или «No».
a = int(input('Введите число: '))
if a % 5 == 0 and a != 0:
    print('Yes')
else:
    print('No')
if a % 4 == 0 and a != 0:
    print('Yes')
else:
    print('No')
