# 1. (если не выполнили на занятии) Напишите программу, которая запрашивает у пользователя данные о студентах и
# сохраняет их в файл формата CSV. Программа должна запрашивать у пользователя информацию о каждом студенте, включая имя,
# фамилию и возраст. Информация о каждом студенте должна быть сохранена в отдельной строке файла CSV. Файл CSV должен
# иметь следующие заголовки столбцов: "Имя", "Фамилия", "Возраст". Программа должна продолжать запрашивать информацию
# о студентах до тех пор, пока пользователь не введет команду "stop" для завершения.
# В конце выполнения программы должно быть выведено сообщение о успешном сохранении данных.
import csv
with open('example.csv', 'w', encoding = 'utf-8', newline = '') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(('Имя', 'Фамилия', 'Возраст'))
while True:
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    age = int(input('Введите возраст: '))
    student = [first_name, last_name, age]
    *student, = first_name, last_name, age
    # print(student)
    with open('example.csv', 'a', newline = '') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(student)

    flag = input('Если вы хотите закончить ввод, введите stop: ')
    if flag == 'stop':
        print('Все успешно сохранено')
        break