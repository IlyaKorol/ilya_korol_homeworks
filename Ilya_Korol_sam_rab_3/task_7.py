# Задача №7. Создайте класс Students, содержащий поля: фамилия и инициалы, номер группы,
# успеваемость (список из пяти элементов).
# Создать класс School:
# Добавить возможность для добавления студентов в школу
# Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 5 или 6.
# Добавить возможность вывода учеников заданной группы
# Добавить возможность вывода учеников претендующих на автомат(средний балл >= 7)

class Students:
    def __init__(self, full_name, number_group, academic_performance):
        self.full_name = full_name
        self.number_group = number_group
        self.academic_performance = academic_performance

class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):  # возможность для добавления студентов в школу
        self.students.append(student)

    def mark_5or6(self):  # возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 5 или 6
        mark_5or6 = []
        for student in self.students:
            for mark in student.academic_performance:
                if mark == 5 or mark == 6:
                    mark_5or6.append((student.full_name, student.number_group))
        return mark_5or6

    def std_group(self, number_group):  # возможность вывода учеников заданной группы
        std_group = []
        for student in self.students:
            if student.number_group == number_group:
                std_group.append(student.full_name)
        return std_group

    def avtomat(self):  # возможность вывода учеников претендующих на автомат(средний балл >= 7)
        avtomat = []
        for student in self.students:
            for mark in student.academic_performance:
                if (sum(student.academic_performance) / len(student.academic_performance)) >= 7:
                    avtomat.append((student.full_name, student.number_group))
        print(f'Студенты, претендующие на автомат: {student.full_name} из группы №{student.number_group}')


school = School()

st1 = Students('Иванов И.И.', 1, [4, 6, 8, 7, 9])
st2 = Students('Петров П.П.', 2, [1, 3, 2, 5, 7])
st3 = Students('Сидоров С.С.', 2, [2, 4, 3, 7, 6])
st4 = Students('Смирнов Д.Д.', 1, [8, 10, 7, 9, 9])

school.add_student(st1)
school.add_student(st2)
school.add_student(st3)
school.add_student(st4)

mark_5or6 = school.mark_5or6()
for student in mark_5or6:
    print(f'Студенты с баллами 5 или 6: ',
          f'Студент {student[0]} из группы №{student[1]}')

print("\nСтуденты из группы 1:")
students_group1 = school.std_group(1)
for student in students_group1:
    print(student)

avtomat = school.avtomat()
