"""Python Fundamentals 2025: Домашнее задание 25
Деление без ошибок
Напишите функцию, которая выполняет деление двух чисел, введенных пользователем, и обрабатывает возможные ошибки.
Пример вывода:
Введите делимое: 345
Введите делитель: 5a
Ошибка: Введено некорректное число.
"""

# def division():
#     m = input("Введите делимое: ")
#     n = input("Введите делитель: ")
#     try:
#         return m / n
#     except ValueError:
#         print("Ошибка: Введено некорректное число.")
#     except ZeroDivisionError:
#         print("Ошибка: Нельзя делить на ноль")
#
# result = division()
# if result is not None:
#     print(result)

"""Логирование ошибок
Перенаправьте в предыдущей задаче вывод ошибок в файл errors.log в соответствии с форматом ниже.
Пример вывода:
2025-02-23 22:38:53,686 - ERROR - test.py - 16 - Ошибка: Введено некорректное число."""

import logging

logging.basicConfig(
    filename="errors.log",
    format="%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s",
    level=logging.ERROR,
)

def division():
    m = input("Введите делимое: ")
    n = input("Введите делитель: ")

    try:
        m = float(m)
        n = float(n)
        return m / n

    except ValueError:
        msg = "Ошибка: Введено некорректное число."
        print(msg)
        logging.error(msg)

    except ZeroDivisionError:
        msg = "Ошибка: Нельзя делить на ноль."
        print(msg)
        logging.error(msg)

result = division()
if result is not None:
    print(result)
