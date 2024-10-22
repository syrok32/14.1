from src.Classes import Product


class Smartphone(Product):
    """ Новый класс который"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity) # берем иницализацию с родительского класса
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """ складываем ценну если два обЪекта являюются одинаковыми классами"""
        if type(other) == Smartphone:
            return self.price + other.price
        else:
            raise TypeError


class LawnGrass(Product):

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)# берем иницализацию с родительского класса
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """ складываем ценну если два обЪекта являюются одинаковыми классами"""
        if type(other) == LawnGrass:
            return self.price + other.price
        else:
            raise TypeError
