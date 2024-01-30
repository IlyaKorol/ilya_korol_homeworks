# Задача 3. Необходимо заполнить список ста нулями, кроме первого и последнего элементов, которые должны быть равны единице
list1 = []
list1.append(1)
list1.append(100*'0')
list1.append(1)
print(list1)

# либо другой вариант

list2 = []
for i in range(100):
    list2.append('0')
list2[0] = '1'
list2[-1] = '1'
print(list2)