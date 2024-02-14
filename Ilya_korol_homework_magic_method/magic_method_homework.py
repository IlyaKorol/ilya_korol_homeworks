# Задача №1.
# Исходные данные:
# - скрипт task1, который содержит реализацию классов Tank, TankCommander, TankGunner и
# код для проверки результата
# Необходимо:
# 1. Реализовать всю необходимую логику так, чтобы скрипт task1 выводил:
#     >>> Test passed. Amazing job!
# Желательно:
# 1. Привести альтернативные способы решения задачи.
# Примечание:
# - НЕЛЬЗЯ менять реализацию приведенных в исходных данных классов и проверочного кода.
# - Нет ограничений по реализации классов Tankman и Vehicle, а также вспомогательной логики.

class M1:
    def __init__(self, id=0):
        self.id = id

    def __get__(self, id, cls):
        self.id += 1
        if id == None:
            return self
        else:
            setattr(id, 'id', self.id)
            return self.id


class M2:
    id = M1()


class Vehicle(M2):
    pass


class Tankman(M2):
    pass


class Tank(Vehicle):
    def __init__(self):
        object_id_collector = self.id


class TankCommander(Tankman):
    def __init__(self):
        object_id_collector = self.id


class TankGunner(Tankman):
    def __init__(self):
        object_id_collector = self.id


def check_object_id_collector():
    expected_ids = (1, 2, 3, 4, 5)
    actual_ids = (TankGunner().id, TankGunner().id, Tank().id, TankCommander().id, Tank().id)
    assert actual_ids == expected_ids, 'Expected_ids: {}. Actual_ids: {}.'.format(expected_ids, actual_ids)
    print('Test passed. Amazing job!')


check_object_id_collector()


