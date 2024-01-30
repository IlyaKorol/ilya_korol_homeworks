# 2. Вы разрабатываете систему управления магазином продуктов. У вас есть класс Product, представляющий продукт.
# Каждый продукт имеет имя, цену и количество на складе. Вам нужно реализовать методы для инициализации и обновления информации
# о продуктах.
# Ваша задача - создать методы класса Product, которые позволяют устанавливать начальные значения для продуктов и обновлять
# информацию о них. Кроме того, вы должны создать метод calculate_total_price, который вычисляет общую стоимость продуктов на складе.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def set_product(self, price, quantity):

        self.price = price
        self.quantity = quantity
    def get_product(self):
        return self.name, self.price, self.quantity

    def calculate_total_price(self):
        return self.price * self.quantity

prod1 = Product('milk', 10, 20)
prod2 = Product('meat', 15, 10)
prod3 = Product('bread', 2, 40)
prod1.set_product(12,18)
prod2.set_product(17,12)
prod3.set_product(3,50)
print(f'{prod1.get_product()},',
      f'{prod2.get_product()},',
      f'{prod3.get_product()}')
print(f'Ообщая стоимость продуктов на складе равна', prod1.calculate_total_price()
      +prod2.calculate_total_price()+prod3.calculate_total_price())