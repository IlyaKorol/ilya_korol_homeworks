# 1. Файл содержит числа и буквы. Каждый записан в отдельной строке.
# Нужно считать содержимое в список так, чтобы сначала шли числа по возрастанию,
# а потом слова по возрастанию их длины.
numbers = []
words = []
with open('1file.txt') as file:
    for line in file:
        line = line[:-1]
        if line.isdigit():
            numbers.append(line)
            numbers.sort()
        if line.isalpha():
            words.append(line)
            words = sorted(words, key=len)
print(numbers+words)




