# Задача 4. Вводится список чисел.
# Определите, сколько в этом списке элементов,
# которые больше двух своих соседей и выведите количество таких элементов.

a = [int(input('Введите список чисел: ')) for i in range(5)]
b = 0
for i in range(1, len(a) - 1):
    if a[i-1] < a[i] > a[i+1]:
        b += 1
print(b)