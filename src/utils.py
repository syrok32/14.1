import json

from main import Category, Product


def create_to(data):
    category = []
    for i in data:
        product = []
        for k in i["products"]:
            product.append(Product(**k))
        i["products"] = product
        category.append(Category(**i))
    return category


def read_json(file_js: str) -> dict:
    with open(f"./data/{file_js}", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


ds = create_to(read_json("products.json"))

print(ds[0].name)
