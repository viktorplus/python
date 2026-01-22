# def greet(name):
#     """
#     Функция принимает имя и возвращает строку приветствия.
#
#     :param name: Имя пользователя.
#     :return: Приветственное сообщение.
#     """
#     return f"Hello, {name}!"


# def greet(name):
#     """
#
#     :param name:
#     :return:
#     """
#     return f"Hello, {name}!"
#
# help(sum)


# def greet(name):
#     """
#     Функция принимает имя и возвращает строку приветствия.
#
#     :param name: Имя пользователя.
#     :return: Приветственное сообщение.
#     """
#     return f"Hello, {name}!"
#
# help(greet)

# help(str)
# help()
#
# l = []


# def add(a: int, b: int, l: list, c) -> int:
#     return a + b
#
# # num: int = 10
# num: int = int(input('Enter a number: '))
#
# print(add("1", "2"))

# def get_info() -> tuple[str, float]:
#    # Первый элемент str, второй элемент float
#     return "Bob", 4.91
# def variable_tuple() -> tuple[int, ...]:
#    # Кортеж произвольной длины, но только целые числа
#     return 5, 8, 2
# В Python 3.9+ (рекомендуется)
# def process_numbers(numbers: list[int]) -> list[int]:
#     return [n ** 2 for n in numbers]
#
# # В Python <3.9 (старый стиль)
# from typing import List
#
# def process_numbers_old(numbers: List[int]) -> List[int]:
#     return [n ** 2 for n in numbers]


# from typing import Any
#
# def process_data(data: Any) -> str:
#     """Принимает данные любого типа и возвращает строку с их представлением."""
#     return f"Данные: {data}"
#
# print(process_data(42))
# print(process_data("Hello"))
# print(process_data([1, 2, 3]))

# from typing import Union
#
# def calculate(value: Union[int, float]) -> float:
#     """Принимает число (целое или дробное) и возвращает его квадрат."""
#     return value ** 2
#
# print(calculate(5))
# print(calculate(2.5))


# from typing import Optional
#
# def get_user_name(user_id: int) -> Optional[str]:
#     """Возвращает имя пользователя или None, если пользователь не найден."""
#     users = {1: "Alice", 2: "Bob"}
#     return users.get(user_id)  # Может вернуть None
#
# print(get_user_name(1))
# print(get_user_name(3))

# def calculate(value: int | float | None) -> float:
#     """Принимает число (целое или дробное) и возвращает его квадрат."""
#     return value ** 2
#
# print(calculate(5))
# print(calculate(2.5))


# from typing import Callable
#
# def add(x: int, y: int) -> int:
#     return x + y
#
# def multiply(x: int, y: int) -> int:
#     return x * y
#
# def execute_function(func: Callable[[int, int], int],
#                      nums1: list[int],
#                      nums2: list[int]) -> list[int]:
#     return [func(a, b) for a, b in zip(nums1, nums2)]
#
# print(execute_function(add, [1, 2, 3], [4, 5, 6]))
# print(execute_function(multiply, [1, 2, 3], [4, 5, 6]))

# [1, 2, 3]
# [4, 5, 6]
# [(1, 4), (2, 5), (3, 6)]
# [5, 7, 9]

#
# def modify_value(n: int) -> None:
#     """Изменяет значение переменной внутри функции (не влияет на оригинал)."""
#     print(f"До изменения в функции: {n}, id: {id(n)}")
#     n += 1  # Создаётся новый объект
#     print(f"После изменения в функции: {n}, id: {id(n)}")
#
# num = 10
# modify_value(num)
# print(f"Вне функции: {num}, id: {id(num)}")

# def modify_list(lst: list) -> None:
#     """Добавляет элемент в список (изменяет оригинальный объект)."""
#     print(f"До изменения в функции: {lst}, id: {id(lst)}")
#     lst.append(99)  # Изменение оригинального списка
#     print(f"После изменения в функции: {lst}, id: {id(lst)}")
#
# my_list = [1, 2, 3]
# modify_list(my_list)
# print(f"Вне функции: {my_list}, id: {id(my_list)}")

def safe_modify_list(lst: list) -> list:
    """Работает с копией списка, оставляя оригинальный неизменным."""
    copy_lst = lst.copy()
    copy_lst.append(99)
    return copy_lst

original_list = [1, 2, 3]
new_list = safe_modify_list(original_list)
print(f"Оригинал: {original_list}")
print(f"Копия: {new_list}")





