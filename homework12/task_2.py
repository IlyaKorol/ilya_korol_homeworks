# 2.В текстовый файл построчно записаны фамилия и имя каждого учащегося класса и их оценка
# за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3 баллов, и посчитать средний балл по классу.
f = open("2file.txt")
sum = 0
n = 0
for line in f:
    line = line.split()
    d = int(line[2])
    sum += d
    n += 1
    if d < 4:
        print(line[0], line[1] , line[2])
f.close()
print('Средний балл %.2f' %(sum/n))

