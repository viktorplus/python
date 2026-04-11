from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich')
filter={
    'Energy': {
        '$gt': 0.8
    }
}

result = client['ich']['Spotify_Youtube'].find(
    filter=filter
)

for item in result:
    print(item)







# from pymongo import MongoClient
#
# client = MongoClient("mongodb://ich1:password@mongo.edu.itcareerhub.de:27017/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich")
# db = client['ich']  # Подключение к конкретной базе данных
#
# # Подключаемся к коллекции Spotify_Youtube
# collection = db['Spotify_Youtube']
#
# # Извлечение всех документов из коллекции Spotify_Youtube
# results = collection.find()
#
# # Выводим данные в консоль
# for document in results:
#     print(document)
#
# import pandas as pd
#
# # Извлечение данных из коллекции
# data = list(collection.find())
#
# # Преобразование данных в DataFrame
# df = pd.DataFrame(data)
#
# # Вывод первых строк DataFrame
# print(df.head())
#
# client.close()
# print("Соединение с MongoDB закрыто")
#
