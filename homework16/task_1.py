# 1. (кто не сделал на занятии) Создайте класс Point3D, который хранит координаты x, y, z.
# Создайте статический метод, который выведет результат x*y*z (где x = 2, y = 3, z = 4).
# Пропишите конструктор для создания экземпляров с локальными координатами.
# Также добавьте методы, позволяющие изменять координаты и получать их.
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    @staticmethod
    def res(x,y,z):
        print(x*y*z)

    def get_coords(self):
        return self.x, self.y, self.z

    def set_coords(self, x_new, y_new, z_new):
        self.x = x_new
        self.y = y_new
        self.z = z_new

a = Point3D(4,5,6)
b = Point3D(7,8,9)
Point3D.res(2,3,4)

coord = Point3D(2,3,4)
coord.set_coords(10,20,30)
print(coord.get_coords())






