"""Python Fundamentals 2025: Домашнее задание 32

Фабрика функций округления

Создайте функцию make_rounder(), которая принимает количество знаков для округления и возвращает другую функцию.
Полученная функция должна принимать число и возвращать его, округлённое до указанного ранее количества знаков после запятой.

Пример вызова:
print(round2(3.14159))
print(round2(2.71828))
print(round0(9.999))
Пример вывода:
3.14
2.72
10.0
"""
# def make_rounder(num_digits):
#     def func(value):
#         return round(value, num_digits)
#     return func
#
# round2 = make_rounder(2)
# round0 = make_rounder(0)
#
# print(round2(3.14159))
# print(round2(2.71828))
# print(round0(9.999))

"""
Расширяемый логгер событий

Создайте функцию, которая возвращает вложенный логгер событий.
Каждый вызов логгера должен сохранять событие с текущим временем (если оно передано) и возвращать весь список событий.

Пример вызова:
log("Загрузка данных")
log("Обработка завершена")
log("Сохранение файла")
for event in log():
    print(event)
Пример вывода:
Загрузка данных: 2025-03-24 14:06:29
Обработка завершена: 2025-03-24 14:06:29
Сохранение файла: 2025-03-24 14:06:29
"""
# from datetime import datetime
#
# def event_logger():
#     events = []
#
#     def log_event(text=""):
#         if text:
#             now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             events.append(f"{text}: {now}")
#         return events
#     return log_event
#
# log = event_logger()
# # print(log())
# log("Загрузка данных")
# log("Обработка завершена")
# # print(log())
# log("Сохранение файла")
# for event in log():
#     print(event)
"""
Рамка вокруг вывода
Создайте декоратор frame, который оборачивает результат функции рамкой из 50 символов -, выводя по строке до и после вызова функции.
Пример декорируемой функции:
def say_hello():
    print("Привет, игрок!")
Пример вывода:
--------------------------------------------------
Привет, игрок!
--------------------------------------------------
"""

# def frame(func):
#     def wrapper():
#         print("-" * 50)
#         func()
#         print("-" * 50)
#     return wrapper
#
# @frame
# def say_hello():
#     print("Привет, игрок!")
#
# say_hello()
#
#  # extra
# def frame(func):
#     def wrapper():
#         print("-" * 50)
#         func()
#         print("-" * 50)
#     return wrapper
#
# def say_hello():
#     print("Привет, игрок!")
#
# decorated_say_hello = frame(say_hello)
#
# say_hello()
# print()
# decorated_say_hello()
#
# # extra
# def frame(func):
#     def wrapper():
#         print("-" * 50)
#         func()
#         print("-" * 50)
#     return wrapper
#
# def say_hello():
#     print("Привет, игрок!")
#
# non_decorated_say_hello = say_hello
# say_hello = frame(say_hello)
#
# say_hello()
# print()
# non_decorated_say_hello()
#
# # extra
# def frame(func):
#     def wrapper():
#         print("-" * 50)
#         func()
#         print("-" * 50)
#     return wrapper
#
# def say_hello():
#     print("Привет, игрок!!!")
#
# def decorated_say_hello():
#     say_hello()
#
# @frame
# def not_decorated_say_hello():
#     say_hello()
#
# decorated_say_hello()
# print()
not_decorated_say_hello()