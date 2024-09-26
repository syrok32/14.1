import pytest

from src.main import Category, Product


@pytest.fixture()
def product_milk():
    return Product("milk", "очень вкусное", 230, 34)


@pytest.fixture()
def category_sweet():
    return Category("candy", "очень вкусное", ["milka", "mars"])
