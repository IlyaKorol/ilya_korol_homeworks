#4. Создается два кортежа, размером 10 элементов,
# из случайных чисел из диапазона от 15 до 55.
# Нужно найти в каждом кортеже максимальный элемент и сравнить их,
# вывести тот, что больше. Если максимальные элементы равны,
# то сравнивать минимальные элементы.

import random
tupl1 = tuple([random.randint(15,55) for i in range(10)])
tupl2 = tuple([random.randint(15,55) for i in range(10)])
print(tupl1)
print(tupl2)
if max(tupl1) > max(tupl2):
    print(max(tupl1))
elif max(tupl2) > max(tupl1):
    print(max(tupl2))
elif max(tupl1) == max(tupl2):
    if min(tupl1) > min(tupl2):
        print(min(tupl1))
    elif min(tupl2) > min(tupl1):
        print(min(tupl2))
    else:
        print('Минимальные элементы равны(как и максаимальные)')
