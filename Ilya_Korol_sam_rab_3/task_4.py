# Задача №4. Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age.
# По умолчанию name = Ivan, age = 18, groupNumber = 10A.
# Необходимо создать пять методов: getName, getAge, getGroupNumber, setNameAge, setGroupNumber.
# Метод getName нужен для получения данных об имени конкретного студента, метод getAge нужен для получения данных
# о возрасте конкретного студента, метод getGroupNumber нужен для получения данных о номере группы конкретного студента.
# Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, метод setGroupNumber позволяет
# изменить номер группы установленный по умолчанию. В программе необходимо создать пять экземпляров класса Student,
# установить им разные имена, возраст и номер группы.

class Student:
    def __init__(self, name="Ivan", age=18, groupNumber="10A"):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber


st1 = Student()
st1.setNameAge('Oleg', 22), st1.setGroupNumber('20B')
st2 = Student()
st2.setNameAge('Mongol', 70), st2.setGroupNumber('7B')
st3 = Student()
st3.setNameAge('Nurlan', 30), st3.setGroupNumber('26p')
st4 = Student()
st4.setNameAge('Khabib', 3), st4.setGroupNumber('4E')
st5 = Student()
st5.setNameAge('Albus', 150), st5.setGroupNumber('1G')
print(f'Студент {st1.getName()}, возрастом {st1.getAge()} лет, из группы {st1.getGroupNumber()}')
print(f'Студент {st2.getName()}, возрастом {st2.getAge()} лет, из группы {st2.getGroupNumber()}')
print(f'Студент {st3.getName()}, возрастом {st3.getAge()} лет, из группы {st3.getGroupNumber()}')
print(f'Студент {st4.getName()}, возрастом {st4.getAge()} лет, из группы {st4.getGroupNumber()}')
print(f'Студент {st5.getName()}, возрастом {st5.getAge()} лет, из группы {st5.getGroupNumber()}')
