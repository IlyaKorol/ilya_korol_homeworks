# 3. Создайте функцию, которая будет заполнять список числами в диапазоне, указанном пользователем.
# Функция должна принимать два аргумента - начало диапазона и его конец, при этом ничего не возвращать. Вывести список.
# Подсказка: список сделать global.
def spis(a,b):
    global list1
    list1 = list(i for i in range(x, y+1))
    print(list1)
x = int(input('Введите начало диапазона: '))
y = int(input('Введите конец диапазона: '))
spis(x,y)
