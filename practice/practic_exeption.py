# while True:
#     data = input('Введите число: ')
#
#     try:
#         float(data)
#
#         print('Вы ввели число:', data)
#         break
#
#     except ValueError:
#         print('Ошибка: Введите корректное число.')
#
#
"""
Напишите функцию, которая проверяет, что возраст пользователя не меньше 18 лет с использованием ошибок
Пример вывода
Введите возраст: 17
Ошибка: Возраст должен быть 18 лет и старше.
"""

#
# def check_age(age:int) -> None:
#     if age < 18:
#         raise ValueError("Возраст должен быть 18 лет и старше.")
#
# age = int (input("Введите возраст: "))
# try:
#     check_age(age)
# except ValueError as e:
#     print(e)


"""Реализуйте аналог deepcopy() с помощью рекурсии. Не забудьте проверить, чтобы изменения в копии не затронули оригинал.
Данные:
original_data = [
[1, 2, 3], # Вложенный список
(4, [5, 6], {7, 8}), # Кортеж с вложенными структурами
{"a": 9, "b": [10, 11]}, # Словарь со списком
"Hello", # Строка
[12, (13, 14)], # Список с кортежем
15.5, # Число с плавающей точкой
5 # Целое число
]
Пример вывода:
Исходный: [[1, 2, 3], (4, [0, 6], {8, 7}), {'a': 9, 'b': [10, 11]}, 'Hello', [12, (13, 14)], 15.5, 5]
Копия: [[1, 2, 3], (4, [5, 6], {8, 7}), {'a': 9, 'b': [10, 11]}, 'Hello', [12, (13, 14)], 15.5, 5]"""

original_data = [
[1, 2, 3], # Вложенный список
(4, [5, 6], {7, 8}), # Кортеж с вложенными структурами
{"a": 9, "b": [10, 11]}, # Словарь со списком
"Hello", # Строка
[12, (13, 14)], # Список с кортежем
15.5, # Число с плавающей точкой
5 # Целое число
]

def deep_copy(obj):
    if isinstance(obj, list):
        return [deep_copy(x) for x in obj]
    elif isinstance(obj, dict):
        return {key: deep_copy(value) for key, value in obj.items()}
    elif isinstance(obj, set):
        return {deep_copy(x) for x in obj}
    elif isinstance(obj, tuple):
        return tuple([deep_copy(x) for x in obj])

    else:
        return obj


baselist = [1, 2, "stroka"]
result = deep_copy(original_data)
# result.append(55)
result[0].append(55)
print(result)
print(original_data)
