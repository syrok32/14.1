from tests.conf import category_sweet, product_milk


def test_product_init(product_milk):
    assert product_milk.name == "milk"
    assert product_milk.description == "очень вкусное"
    assert product_milk.price == 230
    assert product_milk.quantity == 34


def test_categ_init(category_sweet):
    assert category_sweet.name == "candy"
    assert category_sweet.description == "очень вкусное"
    assert category_sweet.products == ["milka", "mars"]
    assert category_sweet.quantity_of_goods == 2
    assert category_sweet.number_of_categories == 1
