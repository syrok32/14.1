import idlelib.run


class Product:
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity) -> None:
        """объявление аотрибувов"""
        self.name = name

        self.description = description
        self.__price = price

        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_product):
        return cls(**dict_product)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:
                answer_user = input()
                if answer_user == "y":
                    self.__price = new_price
                    print("ценна понижена")
                else:
                    print("ценна не будет пониженна")
            else:
                self.__price = new_price

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.price * self.quantity + (self.price * self.quantity)


class Category:
    name: str
    description: str
    products: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += 1
        Category.category_count += len(products)
        self.summ_prod = sum(product.quantity for product in products)

    def add_product(self, prod) -> None:
        """добовление родкута в котегорию"""

        if isinstance(prod, Product): # если является классом или подкласом Product
            self.__products.append(prod)
            Category.product_count += 1
            self.summ_prod += prod.quantity
        else:
            raise TypeError

    @property
    def products(self) -> str:
        new_str = ""
        for i in self.__products:
            new_str += f"{i.name}, {i.price} руб. Остаток:{i.quantity}\n"
        return new_str

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {self.summ_prod} шт."
