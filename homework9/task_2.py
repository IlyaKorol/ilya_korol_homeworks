# 2. Имеются два списка, сгенерированные случайным образом.
# Добавьте в конец первого списка все элементы второго списка.

import random
list1 = list([random.randint(0,5) for i in range(5)])
list2 = list([random.randint(6,10) for i in range(5)])
print(f'Элементы 1-ого списка', list1)
print(f'Элементы 2-ого списка', list2)
print(list1+list2)