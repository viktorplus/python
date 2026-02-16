# import json
#
# data = {"name": "Alice", "age": 25, 'is_student': False}
#
# json_string = json.dumps(data)  # Преобразование в JSON-строку
# print(type(json_string))
# print(json_string)

#
# import json
#
# data = {"name": "Alice", "age": 25, "is_student": False}
#
# with open("data.json", "w") as file:
#     json.dump(data, file)  # Запись JSON в файл


# import json
#
# json_object = '{"name": "Alice", "age": 25, "is_student": false}'
# json_objects = '''
#                 [{"name": "Alice", "age": 25, "is_student": false},
#                 {"name": "Bob", "age": 20, "is_student": true}]'''
#
# data_dict = json.loads(json_objects)  # Преобразование JSON-строки в Python-объект
# print(type(data_dict))
# print(data_dict)


# import json
#
# with open("data.json", "r") as file:
#     data = json.load(file)  # Загрузка JSON из файла
#
# print(type(data))
# print(data)


# import json
#
# data = {
#     "dict_example": {"key": "value"},
#     "list_example": ["apple", "banana"],
#     "tuple_example": ("apple", "banana"),
#     "string_example": "Hello",
#     "int_example": 42,
#     "float_example": 3.14,
#     "bool_example_true": True,
#     "bool_example_false": False,
#     "none_example": None
# }
#
# # Запись в файл data.json
# with open("data.json", "w", encoding="utf-8") as file:
#     json.dump(data, file)


#
# import json
#
# # Чтение данных обратно в Python
# with open("data.json", "r", encoding="utf-8") as file:
#     loaded_data = json.load(file)
#
# # Вывод загруженных данных
# print(type(loaded_data))
# print(loaded_data)
#
#

# import json
#
# data = {"name": "Alice", "age": 25, "is_student": False,
#         "courses": {"math": "A", "physics": "B" }}
#
# json_string = json.dumps(data)  # Без отступа
# print(json_string)
#
# json_string = json.dumps(data, indent=4)  # С отступом
# print(json_string)

#
# import json
#
# data = {"город": "Берлин", "страна": "Германия"}
#
# json_string = json.dumps(data)  # По умолчанию (ensure_ascii=True)
# print(json_string)
#
# json_string = json.dumps(data, ensure_ascii=False)  # Отключаем ASCII-кодировку
# print(json_string)

# import json
#
# data = {"name": "Alice", "age": 25, "is_student": False, "city": "London"}
#
# json_string = json.dumps(data, indent=4)  # Без сортировки ключей
# print(json_string)
#
# json_string = json.dumps(data, indent=4, sort_keys=True)  # Сортировка ключей
# print(json_string)


# import json
#
# invalid_json = '{"name": "Alice", "age": 25, "is_student": false,'  # Ошибка: нет закрывающей скобки
#
# data = json.loads(invalid_json)  # Загрузка некорректного JSON

# import json
#
# invalid_json = '''{"name": "Alice", 'age': 25, "is_student": false}'''  # Ошибка: нет закрывающей скобки
#
# try:
#     data = json.loads(invalid_json)  # Попытка загрузки некорректного JSON
# except json.JSONDecodeError as e:
#     print(f"Ошибка декодирования JSON: {e}")


# ---------------------------------------------------------------------------

# from datetime import datetime
#
# now = datetime.now()  # Получаем текущую дату и время
# print(type(now))  # Объект datetime
# print(now)

#
# from datetime import datetime
#
# now_object = datetime.now()
#
# print("Год:", now_object.year)
# print("Месяц:", now_object.month)
# print("День:", now_object.day)
# print("Часы:", now_object.hour)
# print("Минуты:", now_object.minute)
# print("Секунды:", now_object.second)
# print(now_object.year, now_object.month, now_object.day)


# from datetime import datetime
#
# now = datetime.now()
# # Преобразование в строку
# print(str(now))
# # Преобразование в строку указанного формата
# formatted_date = now.strftime("%d.%m.%Y %H:%M:%S")
# print(type(formatted_date))
# print(formatted_date)
#
# formatted_date = now.strftime("%d%m%Y")
# print(type(formatted_date))
# print(formatted_date)

#
# from datetime import datetime
#
# now = datetime.now()
# print(now.strftime("%Y-%m-%d"))       # 2025-02-28 (ISO формат)
# print(now.strftime("%d/%m/%Y"))       # 28/02/2025 (европейский формат)
# print(now.strftime("%I:%M %p"))       # 02:30 PM (12-часовой формат)
# print(now.strftime("%A, %B %d, %Y"))  # Friday, February 28, 2025
#

# from datetime import datetime
#
# date_string = "28|02|2025 14-30-15"  # Дата в виде строки
# date_obj = datetime.strptime(date_string, "%d|%m|%Y %H-%M-%S")  # Указываем форматы и те же разделители
#
# print(type(date_obj))
# print(date_obj)



# from datetime import datetime
#
# now = datetime.now()
# deadline = datetime.strptime("01.12.2026", "%d.%m.%Y")
#
# if now > deadline:
#     print("Срок истёк!")
# else:
#     print("До дедлайна ещё есть время.")


# from datetime import datetime
#
# date1 = datetime(2025, 2, 28)
# date2 = datetime(2025, 7, 5)
#
# print(date1)
# print(date2)
#
# difference = date2 - date1  # Разница между датами
# print(type(difference))
# print(difference)
# print(difference.days)
# print(difference.seconds)


# from datetime import datetime
#
# dt1 = datetime(2025, 2, 28, 14, 30)
# dt2 = datetime(2025, 3, 2, 10, 0)
#
# difference = dt2 - dt1
# print(difference)
# print(difference.total_seconds())


from datetime import datetime, timedelta

# Дата начала задачи
start_date = datetime(2025, 2, 28)

# Дедлайн через 2 недели
deadline = start_date + timedelta(weeks=2)
print("Дедлайн:", deadline.strftime("%d.%m.%Y"))

# Проверка, прошёл ли дедлайн
today = datetime(2025, 3, 15)  # Текущая дата

if deadline > today:
    print("Дедлайн пропущен!")
else:
    print("Ещё есть время для выполнения задачи.")

