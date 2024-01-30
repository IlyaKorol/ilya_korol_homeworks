# 4. Создайте калькулятор. Пользователь вводит два числа и операцию (+, - , *, **, /).
# Создайте разные лямба-функции для всех операций. Выведите итог.
x = int(input('Введите 1-ое число: '))
y = int(input('Введите 2-ое число: '))
z = input('Введите операцию: ')
if z == '+':
    func = lambda x,y: x+y
elif z == '-':
    func = lambda x,y: x-y
elif z == '*':
    func = lambda  x,y: x*y
elif z == '**':
    func = lambda x,y: x**y
elif z == '/':
    func = lambda x,y: x/y
print(func(x,y))


