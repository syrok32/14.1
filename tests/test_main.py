from tests.conftest import category_price_setter, category_sweet, categoty_new_prod, product_milk


def test_product_init(product_milk):
    assert product_milk.name == "milk"
    assert product_milk.description == "очень вкусное"
    assert product_milk.price == 230
    assert product_milk.quantity == 34


def test_categ_init(category_sweet):
    assert category_sweet.name == "candy"
    assert category_sweet.description == "очень вкусное"

    assert category_sweet.category_count == 2
    assert category_sweet.product_count == 1


def test_new_product(categoty_new_prod):

    assert categoty_new_prod.name == "Samsung Galaxy S23 Ultra", "Ошибка: имя продукта"
    assert categoty_new_prod.description == "256GB, Серый цвет, 200MP камера", "Ошибка: описание продукта"
    assert categoty_new_prod.price == 180000, "Ошибка: цена продукта"
    assert categoty_new_prod.quantity == 5, "Ошибка: количество продукта"

    print("test_new_product: PASSED")


def test_utils():
    from src.utils import create_to, read_json

    prod = create_to(read_json("products.json"))
    assert prod[0].name == "Смартфоны"


def test_price_setter(category_price_setter):

    category_price_setter.price = 950000
    assert category_price_setter.price == 950000

    # Попытка уменьшить цену (в реальной жизни нужно подтвердить через input())
