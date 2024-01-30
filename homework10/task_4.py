# 4.  Необходимо создать словарь, где ключами будут выступать числа от 0 до n (n задается с клавиатуры),
# а значениями будут случайные числа из диапазона от 100 до 200.
import random
n = int(input('Введите число: '))
list1 = list(range(0, n+1))
list2 = list(random.randint(100,200) for i in range(n+1))
dict1 = dict(zip(list1,list2))
print(dict1)