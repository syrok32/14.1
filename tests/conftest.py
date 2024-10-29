import pytest

from src.Classes import Category, Product
from src.Classes_new import LawnGrass, Smartphone
from src.sup_class import Support_range_product


@pytest.fixture()
def product_milk():

    return Product("milk", "Fresh milk", 50, 10)


@pytest.fixture()
def category_sweet():
    product1 = Product("milka", "очень вкусный шоколад", 100, 50)
    product2 = Product("mars", "шоколадный батончик", 80, 30)
    return Category("candy", "очень вкусное", [product1, product2])



@pytest.fixture()
def category_sweet_error():
    product1 = Product("milka", "очень вкусный шоколад", 100, 50)
    product2 = Product("mars", "шоколадный батончик", 80, 30)
    return Category("candy", "очень вкусное", [])




@pytest.fixture()
def Smartphone_class():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture()
def grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture()
def categoty_new_prod():
    product_data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000,
        "quantity": 5,
    }
    product = Product.new_product(product_data)
    return product


@pytest.fixture()
def category_price_setter():
    product = Product("iPhone 14", "128GB, Black", 90000, 10)
    return product


@pytest.fixture()
def support_func():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    return Support_range_product(category1)

