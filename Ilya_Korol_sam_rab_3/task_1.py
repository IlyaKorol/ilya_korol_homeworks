#Задача №1.  Требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
# Для этого создайте класс TriangleChecker, принимающий только положительные числа.
# С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
# Ура, можно построить треугольник!
# С отрицательными числами ничего не выйдет!
# Жаль, но из этого треугольник не сделать.

class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return 'С отрицательными числами ничего не выйдет!'
        elif self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return 'Ура, можно построить треугольник!'
        else:
            return 'Жаль, но из этого треугольник не сделать.'

tri1 = TriangleChecker(1,2,3)
print(tri1.is_triangle())
tri2 = TriangleChecker(-1,-2,-3)
print(tri2.is_triangle())
tri3 = TriangleChecker(3,4,5)
print(tri3.is_triangle())
