# Задача №9. Создать 4 фрукта.
# Апельсин, яблоко, мандарин, банан
# У всех фруктов есть сорт, список витаминов, цена, имя
# У апельсина, мандарина, банана есть метод очистить
# У яблока метод порезать
# У банана есть характеристика: кол-во калия
# Создать 4 объекта фрукта и использовать все доступные методы и характеристики
# При вызове метода очистить, должно писаться имя фрукта
# Например:
# apple = Apple("sort", [a,b,c], 120, "apple")
# apple.clear()
# >>"apple очищен"

class Fruit:
    def __init__(self, variety, vitamins, price, name):
        self.variety = variety
        self.vitamins = vitamins
        self.price = price
        self.name = name


class Orange(Fruit):
    def __init__(self, variety, vitamins, price):
        super().__init__("Апельсин", variety, vitamins, price)

    def clean(self):
        return f'Апельсин очищен'


class Apple(Fruit):
    def __init__(self, variety, vitamins, price):
        super().__init__("Яблоко", variety, vitamins, price)

    def cut(self):
        return f'Яблоко порезано'


class Mandarin(Fruit):
    def __init__(self, variety, vitamins, price):
        super().__init__("Мандарин", variety, vitamins, price)

    def clean(self):
        return f'Мандарин очищен'


class Banana(Fruit):
    def __init__(self, variety, vitamins, price, potassium):
        super().__init__("Банан", variety, vitamins, price)
        self.potassium = potassium

    def clean(self):
        return f'Банан очищен'


orange = Orange('Севильский', ['C', 'B'], 10)
apple = Apple('Голден', ['A', 'B', 'C'], 6)
mandarin = Mandarin('Клементин', ['C', 'D', 'E'], 8)
banana = Banana('Нендрум', ['D', 'E'], 7, 53)

print(orange.clean())
print(apple.cut())
print(mandarin.clean())
print(banana.clean())
