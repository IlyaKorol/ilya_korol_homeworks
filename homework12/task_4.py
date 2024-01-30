# 4. (try-except, изучить raise) Напишите программу, которая запрашивает ввод строки.
# Если в ней есть хотя бы символ - число, то выведите ошибку и заново попросите ввести строку.
# Если все символ буквы, то выведите количество буквы «а».
str1 = input('Введите строку: ')
for i in str1:
    if i.isdigit():
        try:
            raise NameError(input('Введите строку заново: '))
        except NameError:
            break
            print(str1.count('a'))
print(str1.count('a'))