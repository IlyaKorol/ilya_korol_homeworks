# Задача №6. Вы идете в путешествие, надо подсчитать сколько у денег у каждого студента.
# Класс студен описан следующим образом:
# class Student:
# def __init__(self, name, money):
# 	self.name = name
# 	self.money = money

class Student:
    def __init__(self, name, money):
        self.name = name
        self.money = money


st1 = Student('Илья', 8)
st2 = Student('Алеся', 10)
st3 = Student('Яна', 12)
students = [st1, st2, st3]

max_money = max(students, key=lambda student: student.money)

if all(student.money == max_money.money for student in students):
    print('У всех студентов одинаковое количество денег')
else:
    print(f'У студента {max_money.name} больше всего денег: {max_money.money} рублей')
