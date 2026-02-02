# def function_a():
#     print("Начало A")
#     function_b()
#     print("Конец A")
#
# def function_b():
#     print("Начало B")
#     function_c()
#     print("Конец B")
#
# def function_c():
#     print("Начало C")
#     print("Конец C")
#
# function_a()


# def countdown_iterative(n: int) -> None:
#     while n > 0:
#         print(n)
#         n -= 1
#     print("Конец!")
#
# countdown_iterative(5)


# def countdown(n: int) -> None:
#     # Базовый случай
#     if n <= 0:
#         print("Конец!")
#         return
#     print(n)
#     # Рекурсивный случай
#     countdown(n - 1)
#     print("-")
#
# countdown(5)


# def infinite_recursion():
#     infinite_recursion()
#
# infinite_recursion()


# def factorial(n: int) -> int:
#     if n == 0 or n == 1:  # Базовый случай
#         return 1
#     return n * factorial(n - 1)  # Рекурсивный случай
#
# print(factorial(5))
import math
# math.factorial()

# def binary_search(arr: list[int], target: int, left: int, right: int) -> int:
#     if left > right:  # Базовый случай: элемент не найден
#         return -1
#     mid = (left + right) // 2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] < target:
#         return binary_search(arr, target, mid + 1, right)  # Поиск в правой части
#     else:
#         return binary_search(arr, target, left, mid - 1)  # Поиск в левой части
# array = [1, 3, 5, 7, 9, 11, 13]
# # print(binary_search(array, 5, 0, len(array) - 1))
# # print(binary_search(array, 13, 0, len(array) - 1))
# print(binary_search(array, 8, 0, len(array) - 1))


# print(2 ** 100)


# def factorial_tail(n: int, accumulator: int = 1) -> int:
#     if n == 0 or n == 1:
#         return accumulator
#     return factorial_tail(n - 1, n * accumulator)
#
# print(factorial_tail(5))


# def print_numbers(n):
#     if n == 0:
#         return
#     print(n)
#     print_numbers(n - 1)
#
#
# def print_nums(n):
#     if n == 0:
#         return
#     print_nums(n - 1)
#     print(n)
#
# print(print_numbers(5))
# print(print_nums(5))


# original_list = [[1, 2], [3, 4]]
# # Поверхностная копия, вложенные коллекции скопированы как ссылки
# copy_lst = original_list.copy()
# # Добавляет в копию, не затрагивает вложенные элементы.
# copy_lst.append(99)
# # Изменяет копию списка, но затрагивает вложенные элементы.
# copy_lst[0][0] = "X"  # Влияет на оригинал!
# print("Оригинал:", original_list)
# print("Копия:", copy_lst)


# from copy import deepcopy, copy
# original_list = [[1, 2], [3, 4]]
# # Глубокая копия, для вложенных коллекций созданы дубликаты объектов
# copy_lst = deepcopy(original_list)
# []
# # Добавляет в копию, не затрагивает вложенные элементы.
# copy_lst.append(99)
# # Изменяет вложенные элементы, которые не связаны с изначальным списком.
# copy_lst[0][0] = "X"  # Не влияет на оригинал!
# copy_lst[1].append(5)  # Не влияет на оригинал!
# print("Оригинал:", original_list)
# print("Копия:", copy_lst)
#
#
# a = [5]
# original_list = ["text", [1, 2], a, {"el1": 1}, [3, 4, ["t"]]]
#
# copy_lst = deepcopy(original_list)
# a.append("____________________")
# print(original_list)
# print(copy_lst)


# Пример 1: Проверка типа переменной
x = 10
y = "Hello"
print(isinstance(x, int))
print(isinstance(y, str))
print(isinstance(y, int))

#  Пример 2: Проверка нескольких типов
# Можно передать кортеж классов, чтобы проверить принадлежность к нескольким типам.
value = 3.14
# Проверяем, является ли число целым или вещественным
if isinstance(value, (int, float)):
    print("Число")
else:
    print("Не число")


# values = {1, 2}
# # Проверяем, является ли число целым или вещественным
# if isinstance(values, list):
#     values.append(3)
# elif isinstance(values, set):
#     values.add(3)
# print(values)


# Пример 3: Фильтрация данных по типу
# С помощью isinstance() можно отбирать элементы нужного типа из списка.
data = [1, "hello", 2.5, True, "world", 42, []]
numbers = [x for x in data if isinstance(x, (int, float))]
print(numbers)















