import json

from src.Classes import Category, Product


def create_to(data):
    """Перобразовывает JSon в класс"""
    category = []
    for i in data:
        product = []
        for k in i["products"]:
            product.append(Product(**k))
        i["products"] = product
        category.append(Category(**i))
    return category


def read_json(file_js: str) -> dict:
    """Чтение jSon файла"""
    with open(f"./data/{file_js}", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


ds = create_to(read_json("products.json"))

print(ds[0].products)
