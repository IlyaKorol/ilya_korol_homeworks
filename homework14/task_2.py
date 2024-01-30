# 2. Случайным образом генерируется список из чисел. Создайте функцию, которая посчитает сумму элементов.
def summa():
    import random
    list1 = [random.randint(1,10) for i in range(10)]
    print(list1)
    return sum(list1)
sum1 = summa()
print(sum1)