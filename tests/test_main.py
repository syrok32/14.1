from tests.conftest import category_sweet, product_milk


def test_product_init(product_milk):
    assert product_milk.name == "milk"
    assert product_milk.description == "очень вкусное"
    assert product_milk.price == 230
    assert product_milk.quantity == 34


def test_categ_init(category_sweet):
    assert category_sweet.name == "candy"
    assert category_sweet.description == "очень вкусное"
    assert category_sweet.products == ["milka", "mars"]
    assert category_sweet.category_count == 2
    assert category_sweet.product_count == 1


def test_utils():
    from src.utils import create_to, read_json

    prod = create_to(read_json("products.json"))
    assert prod[0].name == "Смартфоны"
