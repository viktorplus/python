"""Python Fundamentals 2025: Домашнее задание 20
Простое число
Напишите функцию, которая проверяет, является ли число n простым
(делится только на 1 и само себя) и возвращает булевый результат.
Данные:
n = 17
Пример вывода:
Число 17 является простым
"""
# def prime(m):
#     if m < 2:
#         return False
#     for i in range(2, m):
#         if m % i == 0:
#             return False
#     return True
#
# n = 17
# if prime(n):
#     print(f"Число {n} является простым")
# else:
#     print(f"Число {n} не является простым")



"""
Фильтрация чисел по чётности
Напишите функцию, которая принимает filter_type ("even" или "odd") и 
произвольное количество чисел, возвращая только те, которые соответствуют фильтру.
Пример вызова:
print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))
Пример вывода:
[2, 4, 6]
[15, 25]
Некорректный фильтр
"""
# def filter_numbers (typ, *num):
#     result = []
#     for i in num:
#         if typ == "even":
#             if i % 2 == 0:
#                 result.append(i)
#                 continue
#         elif typ == "odd":
#             if i % 2 != 0:
#                 result.append(i)
#                 continue
#         else:
#             return "Некорректный фильтр"
#     return result
#
# print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
# print(filter_numbers("odd", 10, 15, 20, 25))
# print(filter_numbers("prime", 2, 3, 5, 7))
"""
Объединение словарей
Напишите функцию, которая принимает любое количество словарей и объединяет их в один. 
Если ключи повторяются, используется значение из последнего словаря.
Данные:
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}

Пример вызова:
print(merge_dicts(dict1, dict2, dict3))
Пример вывода:
{'a': 1, 'b': 3, 'c': 4, 'd': 5}
"""
def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}
print(merge_dicts(dict1, dict2, dict3))