from src.Classes import Category, Product


class Support_range_product:
    def __init__(self, category):
        self.class_cuteg = category
        self.products = category._Category__products

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count < len(self.products):
            product = self.products[self.count]
            self.count += 1
            return product
        else:
            raise StopIteration

    def __str__(self):

        result = ""
        for product in self.products:
            result += f"{product.name} "
        return result.strip()


product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


category1 = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    [product1, product2, product3],
)


r = Support_range_product(category1)
print(str(r))

for i in r:
    print(i)
