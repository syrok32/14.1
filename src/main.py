class Product:
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    name: str
    description: str
    products: list
    number_of_categories = 0
    quantity_of_goods = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.number_of_categories += 1
        Category.quantity_of_goods += len(products)
