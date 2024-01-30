# 2.Создайте суперкласс «Персональные компьютеры» и на его основе подклассы: «Настольные ПК» и «Ноутбуки».
# В классе-родителе определите общие свойства: размер памяти, модель. А в классах-потомках уникальные свойства:
# - для настольных: монитор, клавиатура, мышь; и метод для вывода этой информации
# - для ноутбуков: габариты, диагональ экрана; и метод для вывода этой информации.
class PC:
    def __init__(self, memory, model):
        self.memory = memory
        self.model = model

class TPC(PC): # настольные ПК
    def __init__(self, memory, model, monit, keyb, mouse):
        super().__init__(memory, model)
        self.monit = monit
        self.keyb = keyb
        self.mouse = mouse
    def info(self):
        return f'Модель: {self.model}, размер памяти: {self.memory} терабайт, монитор {self.monit}, клавиатура {self.keyb}, мышь {self.mouse}'

class LPTP(PC): # ноутбуки
    def __init__(self, memory, model, dimens, scrDiag):
        super().__init__(memory, model)
        self.dimens = dimens
        self.scrDiag = scrDiag
    def info(self):
        return f'Модель: {self.model}, размер памяти: {self.memory} терабайт, габариты {self.dimens}, диагональ экрана {self.scrDiag} дюймов'


pc1 = TPC(256, 'ABC', 'Присутствует', 'Присутствует', 'Присутствует')
pc2 = LPTP(512, 'MacBook', 100*20, 16)
print(pc1.info())
print(pc2.info())


