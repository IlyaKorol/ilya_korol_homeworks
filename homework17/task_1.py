# 1. Создайте класс Vector, представляющий вектор в трехмерном пространстве.
# Определите магические методы для арифметических операторов (+, -, *, /), чтобы можно было выполнять операции над векторами.
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z
        return Vector(new_x, new_y, new_z)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z
        return Vector(new_x, new_y, new_z)

    def __mul__(self, other):
        new_x = self.x * other.x
        new_y = self.y * other.y
        new_z = self.z * other.z
        return Vector(new_x, new_y, new_z)
    def __truediv__(self, other):
        new_x = self.x / other.x
        new_y = self.y / other.y
        new_z = self.z / other.z
        return Vector(new_x, new_y, new_z)
v1 = Vector(10,20,30)
v2 = Vector(5,2,3)
res1 = v1 + v2
res2 = v1 - v2
res3 = v1 * v2
res4 = v1 / v2
print(f'+ {res1.x,res1.y,res1.z},',
      f'- {res2.x,res2.y,res2.z},',
      f'* {res3.x,res3.y,res3.z},',
      f'/ {res4.x,res4.y,res4.z},')