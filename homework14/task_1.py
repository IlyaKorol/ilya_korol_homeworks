# 1. Вводится год с клавиатуры. Создайте функцию, которая будет проверять, является ли год високосным.
# Подсказка: високосный год одновременно делится на 4 и не делится на 100 или делится на 400.
def func(a):
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        print(f' {a} год является високосным')
    else:
        print(f' {a} год не является високосным')
year = int(input('Введите год: '))
func(year)