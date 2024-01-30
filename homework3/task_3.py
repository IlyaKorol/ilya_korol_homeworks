# Задача 3. Случайное число от 1 до 12 (номер месяца), использовать random. Нужно вывести какой это сезон года (зима, весна, лето, осень).
import random
m = random.randint(1,12)
print(m)
if m>=1 and m<=2 or m==12:
    print('Зима')
elif m>=3 and m<=5:
    print('Весна')
elif m>=6 and m<=8:
    print('Лето')
else:
    print('Осень')