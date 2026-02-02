# 10 / 0

# try:
#     result = 10 / int(input("Введите число: "))  # Возникает ZeroDivisionError
#     # Следующий код не достижим при ошибке
#     print("Деление выполнено успешно!")
#     print(result)
# except ZeroDivisionError:
#     print("Ошибка: деление на ноль!")
# except ValueError:
#     print("Ошибка: не числовые данные!")

# try:
#     result = 10 / 0
# # Возникает ZeroDivisionError
# except IndexError:
#     print("Индекс вне диапазона!")
# # Пропускается
# except KeyError:
#     print("Ключ не существует!")
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# # Пропускается
# except Exception:
#     print("Ошибка обработки!")
# # Выполнится, так как `Exception`
# # перехватывает `ZeroDivisionError`
#
# while True:
#     try:
#         user_input = input("Введите ненулевое число: ")
#         result = 10 / int(user_input)
#         print(f"Результат: {result}")
#         break
# # Выход из цикла, если ошибок не было
#     except (ZeroDivisionError, ValueError):
# # Просим пользователя повторить ввод
#         print("Ошибка! Введите корректное ненулевое число.")



# try:
#     user_input = input("Введите ненулевое число: ")
#     result = 10 / int(user_input)
#     print(f"Результат: {result}")
# # Выход из цикла, если ошибок не было
# except (ZeroDivisionError, ValueError):
# # Просим пользователя повторить ввод
#     print("Ошибка! Введите корректное ненулевое число.")
#
# print(f"Результат: {result}")


# try:
#     # Попытка преобразования строки в число
#     number = int("abc")
# except (ZeroDivisionError, ValueError) as e:
#     # Выводим текст исключения
#     print(f"Произошла ошибка: {e}")


# try:
# # Преобразование строки в число
#     number = int(input("Введите число: "))
# except ValueError:
# # Обработка некорректного ввода
#     print("Ошибка! Введите корректное число.")
# else:
# # Выполняется только если исключения не было
#     print(f"Вы ввели число: {number}")

#
# try:
#     # Попытка преобразовать строку в число и выполнить деление
#     number = int(input("Введите число: "))
#     result = 10 / number
# except ValueError:
#     # Обработка некорректного ввода
#     print("Ошибка: введено некорректное значение.")
# except ZeroDivisionError:
#     # Обработка деления на ноль
#     print("Ошибка: деление на ноль.")
# else:
#     # Выполняется только если исключений не было
#     print(f"Результат деления: {result}")
# finally:
#     # Завершающие действия
#     print("Программа завершена.")


# number = -1
# if number < 0:
#     raise ValueError("Число не может быть отрицательным")
# 10 / 0

# while True:
#     try:
#         # Ввод числа пользователем
#         number = int(input("Введите положительное число: "))
#         if number < 0:
#             raise ValueError("Число не может быть отрицательным")
#         print(f"Вы ввели корректное число: {number}")
#         break  # Завершаем цикл, если число корректное
#     except ValueError as e:
#         # Обработка некорректного ввода
#         print(f"Ошибка: {e}. Попробуйте снова.")


#
# try:
#     print("До исключения", end=" | ")
#     raise ValueError("Ошибка!")
#     print("После исключения", end=" | ")
# except ValueError as e:
#     pass

#
# import logging
#
# # Вывод различных сообщений
# logging.debug("Отладочное сообщение")
# logging.info("Информационное сообщение")
# logging.warning("Предупреждение!")
# logging.error("Ошибка!")
# logging.critical("Критическая ошибка!")


# import logging
#
# # Настройка логирования с записью в файл
# logging.basicConfig(filename="app.log", level=logging.INFO)
#
# logging.info("Программа запущена")
# logging.warning("Низкий уровень памяти")
# logging.error("Ошибка подключения к базе данных")



# import logging
#
# logging.basicConfig(filename="app.log", level=logging.ERROR)
#
# try:
#     result = 10 / 0
# except ZeroDivisionError as e:
#     logging.error(f"Ошибка: {e}")

# import logging
# logger = logging.getLogger(__name__)
#
# # Настройка формата логов
# logging.basicConfig(
#     filename="app.log",
#     # format="%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s",
#     level=logging.DEBUG
# )


# import logging
#
# root = logging.getLogger()
# root.name = "my_root"
# # root.name = __name__
#
# logging.basicConfig(
#     # filename="app.log",
#     level=logging.DEBUG,
#     format="%(levelname)s:%(name)s:%(message)s"
# )
#
# logging.info("Сообщение")


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
        temp = []
        for x in obj:
            temp.append(deep_copy(x))
        return temp
    elif isinstance(obj, dict):
        temp = {}
        for key, value in obj.items():
            temp[key] = deep_copy(value)
        return temp
    elif isinstance(obj, set):
        temp = set()
        for x in obj:
            temp.add(deep_copy(x))
        return temp
    elif isinstance(obj, tuple):
        temp = []
        for x in obj:
            temp.append(deep_copy(x))
        return tuple(temp)
    else:
        return obj

from copy import deepcopy
baselist = [1, 2, "stroka"]
result = deep_copy(original_data)
# result.append(55)
result[0].append(55)
print(result)
print(original_data)