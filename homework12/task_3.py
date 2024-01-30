# 3.В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов.
file = open('2file.txt')
lines = 0
for line in file:
    lines += 1
    symb = 0
    for i in line:
        if i != ' ' and symb == 0:
            symb = 1
        elif i == ' ':
            symb = 0
    print(line,'Символов', len(line))
print(lines,'строк')
file.close()