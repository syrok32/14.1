import pytest

from src.Classes import Category, Product


@pytest.fixture()
def product_milk():
    return Product("milk", "очень вкусное", 230, 34)


@pytest.fixture()
def category_sweet():
    return Category("candy", "очень вкусное", ["milka", "mars"])


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
