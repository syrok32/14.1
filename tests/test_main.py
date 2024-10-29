from tests.conftest import (Smartphone_class, category_price_setter, category_sweet, categoty_new_prod, grass,
                            product_milk, support_func, category_sweet_error)
from src.Classes import Category, Product

def test_product_init(product_milk):
    assert product_milk.name == "milk"
    assert product_milk.description == "Fresh milk"
    assert product_milk.price == 50
    assert product_milk.quantity == 10

def test_category_error(category_sweet_error):
    assert category_sweet_error.middle_price() == 0.0



def test_Smartphone_init(Smartphone_class):
    assert Smartphone_class.name == "Iphone 15"
    assert Smartphone_class.description == "512GB, Gray space"
    assert Smartphone_class.price == 210000.0
    assert Smartphone_class.quantity == 8
    assert Smartphone_class.efficiency == 98.2
    assert Smartphone_class.model == "15"
    assert Smartphone_class.memory == 512
    assert Smartphone_class.color == "Gray space"


def test_LawnGrass(grass):
    assert grass.name == "Газонная трава"
    assert grass.description == "Элитная трава для газона"
    assert grass.price == 500.0
    assert grass.quantity == 20
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_categ_init(category_sweet):
    assert category_sweet.name == "candy"
    assert category_sweet.description == "очень вкусное"
    assert category_sweet.category_count == 5
    assert category_sweet.product_count == 3


def test_new_product(categoty_new_prod):
    assert categoty_new_prod.name == "Samsung Galaxy S23 Ultra", "Ошибка: имя продукта"
    assert categoty_new_prod.description == "256GB, Серый цвет, 200MP камера", "Ошибка: описание продукта"
    assert categoty_new_prod.price == 180000, "Ошибка: цена продукта"
    assert categoty_new_prod.quantity == 5, "Ошибка: количество продукта"


def test_utils():
    from src.utils import create_to, read_json

    prod = create_to(read_json("products.json"))
    assert prod[0].name == "Смартфоны"


def test_price_setter(category_price_setter):
    category_price_setter.price = 950000
    assert category_price_setter.price == 950000


def test_category_products(category_sweet):
    assert str(category_sweet) == "candy, количество продуктов: 80 шт."


def test_product_str(product_milk):
    assert str(product_milk) == "milk, 50 руб. Остаток: 10 шт."


def test_support_class(support_func):
    assert str(support_func) == "Samsung Galaxy S23 Ultra Iphone 15 Xiaomi Redmi Note 11"



# def test_new_prod(new_prod):
#     assert repr(Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
#                        180000.0, 5))  == repr(Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5))