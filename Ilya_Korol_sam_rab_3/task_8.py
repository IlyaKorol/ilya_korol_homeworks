# Задача №8. Создайте класс Робот
# создайте 2 типа оружия: меч, автомат
# Создайте 2 типа амуниции: броня, шлем
# Добавьте оружию и амуниции свои характеристики(например урон, прочность)
# Создайте своего робота с каким либо оружием (может быть несколько и брони может быть несколько. Также может быть ничего)
# Выведите весь арсенал робота на экран

class Weapon:
    def __init__(self, name, damage, durability):
        self.name = name
        self.damage = damage
        self.durability = durability


class Ammunition:
    def __init__(self, name, protection, durability):
        self.name = name
        self.protection = protection
        self.durability = durability


class Robot:
    def __init__(self, name):
        self.name = name
        self.weapons = []
        self.ammunitions = []

    def equip_weapon(self, weapon):
        self.weapons.append(weapon)

    def equip_ammunition(self, ammunition):
        self.ammunitions.append(ammunition)

    def arsenal(self):
        print(f"Арсенал робота {self.name}:")
        if self.weapons:
            print("Оружие:")
            for weapon in self.weapons:
                print(f"- {weapon.name} (Урон: {weapon.damage}, Прочность: {weapon.durability})")
        else:
            print("Нет оружия")
        if self.ammunitions:
            print("Амуниция:")
            for ammunition in self.ammunitions:
                print(f"- {ammunition.name} (Защита: {ammunition.protection}, Прочность: {ammunition.durability})")
        else:
            print("Нет амуниции")


robot = Robot('Роза')

sword = Weapon("Меч", 50, 100)
rifle = Weapon("Автомат", 80, 150)

armor = Ammunition("Броня", 30, 200)
helmet = Ammunition("Шлем", 20, 100)

robot.equip_weapon(sword)
robot.equip_ammunition(armor)
robot.equip_ammunition(helmet)

robot.arsenal()
