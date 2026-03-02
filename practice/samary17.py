# 5. Журнал вызовов функции
# Создайте декоратор log_to_file, который будет записывать в файл все вызовы функции с её аргументами и результатом.
# Лог сохраняется в файл call_log.log, каждый вызов — на новой строке.
# Пример применения:
# @log_to_file
# def add(a, b):
# return a + b
#
# @log_to_file
# def greet_with_name(name, punctuation="!"):
# return f"Hello, {name}{punctuation}"
#
# @log_to_file
# def greet():
# return "Hello"
# Пример вывода (файл call_log.log):
# function: add | args: 5, 3; kwargs: None | return: 8
# function: greet_with_name | args: Alice; kwargs: punctuation='.' | return: Hello, Alice.
# function: greet | args: None; kwargs: None | return: Hello

# import logging
# logging.basicConfig(filename="app.log", level=logging.ERROR)
# logging.info("Сообщение")

# Пример вызова:
# try:
#     print(add(5, 3))
#     print(greet_by_name("Anna"))
#     print(add("one", 3))             # ошибка
#     print(greet_by_name("Anna", 0))  # ошибка
# except Exception as e:
#     print(e)
