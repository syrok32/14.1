# README Файл

## Описание

Данный проект реализует классы `Product` и `Category`, которые предназначены для управления товарами и категориями в системе. Классы включают функциональность для хранения информации о товарах и группировке их по категориям.

## Классы

### Product

Класс `Product` представляет отдельный товар и содержит следующие свойства:

- `name` (str): Название товара.
- `description` (str): Описание товара.
- `price` (float): Цена товара.
- `quantity` (int): Количество товара в наличии.

#### Инициализация
При создании объекта класса `Product` необходимо передать все параметры:

class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


### Category

Класс `Category` представляет категорию товаров и содержит следующие свойства:

- `name` (str): Название категории.
- `description` (str): Описание категории.
- `products` (list): Список товаров, относящихся к категории.

#### Атрибуты класса
Класс имеет два атрибута, которые отслеживают общее количество категорий и количество товаров в каждой категории:

- `total_categories` (int): Общее количество категорий.
- `total_products` (int): Общее количество товаров во всех категориях.

#### Инициализация
При создании объекта класса `Category` необходимо передать все параметры:

class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        # Обновление класса атрибутов
        Category.total_categories += 1
        Category.total_products += len(self.products)


## Установка

Для использования классов просто скопируйте файл с классами в ваш проект. Вы можете использовать следующую структуру:

/проект
│
├── main.py
└── product_category.py 


Где `product_category.py` — это файл, содержащий определения классов `Product` и `Category`.

## Тестирование

Для тестирования корректности работы классов используйте библиотеку `pytest`. Необходимо проверить:

- Корректность инициализации объектов класса `Category`.
- Корректность инициализации объектов класса `Product`.
- Подсчет количества продуктов.
- Подсчет количества категорий.

Пример тестов:

import pytest
from product_category import Product, Category

def test_product_initialization():
    p = Product("Товар 1", "Описание товара 1", 100.0, 10)
    assert p.name == "Товар 1"
    assert p.description == "Описание товара 1"
    assert p.price == 100.0
    assert p.quantity == 10

def test_category_initialization():
    cat = Category("Категория 1", "Описание категории 1")
    assert cat.name == "Категория 1"
    assert cat.description == "Описание категории 1"
    assert cat.products == []
    assert Category.total_categories == 1

def test_product_count():
    cat = Category("Категория 2", "Описание категории 2", [Product("Товар 2", "Описание товара 2", 200.0, 5)])
    assert Category.total_products == 1

def test_multiple_categories():
    cat1 = Category("Категория 3", "Описание категории 3")
    cat2 = Category("Категория 4", "Описание категории 4", [Product("Товар 3", "Описание товара 3", 150.0, 7)])
    assert Category.total_categories == 4
    assert Category.total_products == 1


## Использование

Создавайте объекты классов `Product` и `Category` и используйте их в вашем приложении для управления товарами и категориями. 

# Пример использования:
p1 = Product("Товар 1", "Описание товара 1", 100.0, 10)
cat1 = Category("Категория 1", "Описание категории 1", [p1])


## Лицензия
