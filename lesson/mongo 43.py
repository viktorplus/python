from pymongo import MongoClient

client = MongoClient(
    "mongodb://ich_editor:verystrongpassword"
    "@mongo.itcareerhub.de/?readPreference=primary"
    "&ssl=false&authMechanism=DEFAULT&authSource=ich_edit"
)


# if client.admin.command("ping")["ok"]:
#     print("Connection successful!")

db = client["ich_edit"]
products_coll = db["products_101025_viktor"]
# print(products)

product = {
    "name": "Notebook",
    "price": 5.99,
    "stock": 120
}

result = products_coll.insert_one(product)
print("Inserted ID:", result.inserted_id)

items = [
    {"name": "Pen", "price": 1.50, "stock": 300},
    {"name": "Pencil", "price": 0.99, "stock": 500},
    {"name": "Eraser", "price": 0.75, "stock": 200},
]

result = products_coll.insert_many(items)
print("Inserted IDs:", result.inserted_ids)



client.close()