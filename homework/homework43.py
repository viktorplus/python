"""Python Fundamentals 2025: Домашнее задание 43

Добавление товаров
Создайте программу, которая подключается к MongoDB и:
выбирает базу ich_edit и коллекцию products_<your_group>_<your_full_name>
очищает коллекцию перед началом
добавляет 3 товара с полями: name, price, stock
выводит сообщение о количестве добавленных товаров"""

from pymongo import MongoClient

client = MongoClient(
    "mongodb://ich_editor:verystrongpassword"
    "@mongo.itcareerhub.de/?readPreference=primary"
    "&ssl=false&authMechanism=DEFAULT&authSource=ich_edit"
)

db = client["ich_edit"]
products = db["products_lesson_43"]

# Очистка перед добавлением
products.delete_many({})

items = [
    {"name": "Pen", "price": 1.5, "stock": 100},
    {"name": "Notebook", "price": 3.99, "stock": 50},
    {"name": "Backpack", "price": 25.0, "stock": 20},
]

result = products.insert_many(items)
print(f"{len(result.inserted_ids)} products inserted.")

"""Увеличение цен
Продолжите предыдущую задачу. Теперь программа должна:
увеличить цену всех товаров на 20%
вывести количество обновлённых записей
затем вывести список всех товаров с новыми ценами"""

from pymongo import MongoClient

client = MongoClient(
    "mongodb://ich_editor:verystrongpassword"
    "@mongo.itcareerhub.de/?readPreference=primary"
    "&ssl=false&authMechanism=DEFAULT&authSource=ich_edit"
)

db = client["ich_edit"]
products = db["products_lesson_43"]

cursor = products.find({})
updated = 0

for doc in cursor:
    # Увеличение цен на 20%
    new_price = round(doc["price"] * 1.2, 2)
    result = products.update_one(
        {"_id": doc["_id"]},
        {"$set": {"price": new_price}}
    )
    if result.modified_count:
        updated += 1


print(f"Prices updated for {updated} products.\n")

# Вывод товаров после обновления
print("Updated products:")
for doc in products.find():
    print(f"- {doc['name']} — ${doc['price']:.2f}")

# extra

from pymongo import MongoClient

client = MongoClient(
    "mongodb://ich_editor:verystrongpassword"
    "@mongo.itcareerhub.de/?readPreference=primary"
    "&ssl=false&authMechanism=DEFAULT&authSource=ich_edit"
)

db = client["ich_edit"]
products = db["products_lesson_43"]


result = products.update_many(
    {},
    {"$mul": {"price": 1.2}}  # Увеличение цен на 20%
)

print(f"Prices updated for {result.modified_count} products.\n")

# extra

from pymongo import MongoClient

client = MongoClient(
    "mongodb://ich_editor:verystrongpassword"
    "@mongo.itcareerhub.de/?readPreference=primary"
    "&ssl=false&authMechanism=DEFAULT&authSource=ich_edit"
)

db = client["ich_edit"]
products = db["products_lesson_43"]

updated = 0

result = products.update_many(
    {},
    [
        {
            "$set": {
                "price": {
                    "$round": [
                        {"$multiply": ["$price", 1.2]},  # Увеличение цен на 20%
                        2  # до 2 знаков
                    ]
                }
            }
        }
    ]
)

print(f"Prices updated for {result.modified_count} products.\n")
