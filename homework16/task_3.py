# 3. Создайте класс Фрукт, его свойствами будет: название фрукта, цвет и размер.
# - создайте метод, который будет выводить название и цвет фрукта
# - создайте абстрактный метод, который будет реализован в классах-потомках
#  Также создайте от класса Фрукт несколько потомков для которых будет определено: страна от куда приехал фрукт (private)
# - создайте метод, который будет выводить название фрукта и страну от куда он приехал, цвет, размер (он класса-родителя через super)
# - придумайте любой метод, который бы реализовывал абстрактный метод класса-родителя
from abc import ABC, abstractmethod
class Fruit(ABC):
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
    def info(self):
        return f'{self.name}, {self.color}'
    @abstractmethod
    def abstr(self):
        pass
class Fruit1(Fruit):
    def abstr(self, country):
        return f'{self.name},{country},{self.color},{self.size}'
class Fruit2(Fruit):
    def abstr(self, country):
        return f'{self.name},{country},{self.color},{self.size}'

f1 = Fruit1('apple','red', 3)
f2 = Fruit2('banana','yellow', 5)
print(f1.abstr('poland'))
print(f2.abstr('brazil'))