# def square(x):
#     return x * x
#
# def cube(x):
#     return x * x * x
#
# def apply_function(func, value):
#     return func(value)  # Вызываем переданную функцию внутри другой функции
#
# result_square = apply_function(square, 5)  # Передаём функцию square без вызова (скобок)
# result_cube = apply_function(cube, 5)  # Передаём функцию cube без вызова (скобок)
# print(result_square)
# print(result_cube)
#
# # result = apply_function(square(5), 5)  # Ошибка!

# def add(x, y):
#     return x + y
#
# def multiply(x, y):
#     return x * y
#
# # Функции можно хранить в списках, словарях и передавать их динамически
# operations = {
#     "+": add,
#     "*": multiply
# }
# choice = input("Выберите операцию (+, *): ")
# # Из словаря получена функция и скобки с аргументами запускают её
# print(operations[choice](10, 5))

# def process_data(func, data):
#     return func(data)
#
# # Можно передавать не только пользовательские функции, но и встроенные
# result = process_data(abs, -10)
# print(result)

# ------------------------------------------------------


# # Функция принимает число x и возвращает его квадрат
# square = lambda x: x ** 2
# print(square(4))
# print(square(5))
#
# # Аналог с def
# def square(x):
#     return x ** 2
# print(square(4))
# print(square(5))


# # Функция принимает два аргумента и возвращает их сумму
# add = lambda x, y: x + y
# print(add(3, 5))
# print(add(8, 9))
#
# # Аналог с def
# def add(x, y):
#     return x + y
# print(add(3, 5))
# print(add(8, 9))

# def apply_func(func, numbers):
#     return [func(num) for num in numbers]
#
# # result = apply_func(lambda x: x + 10, [5, 8, 3])
# # print(result)
#
# print(apply_func(lambda x: x ** 2, [2, 3, 4]))
# print(apply_func(lambda x: x ** 4, [2, 3, 4]))

# print(list(map(lambda x: x ** 2, [2, 3, 4])))


# def add(x, y):
#     return x + y
#
# print((lambda func, a, b: func(a, b))(add, 3, 4))

#
# numbers = [1, 2, 3, 4]
#
# # Каждый элемент списка возводится в квадрат
# squared = map(lambda x: x ** 2, numbers)
# print(squared)
# for i in squared:
#     print(i)
#
# print(list(squared))  # [1, 4, 9, 16]
# print(list(squared))  # [1, 4, 9, 16]



# numbers = [1, 2, 3, 4]
#
# # Каждый элемент списка возводится в квадрат
# squared = list(map(lambda x: x ** 2, numbers))
# print(squared)
# print(*squared)

# a = [1, 2, 3]
# b = [4, 5, 6]
# # Каждая пара элементов списков суммируется
# result = map(lambda x, y: x + y, a, b)
# print(list(result))  # [5, 7, 9]

#
# group_numbers = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# # К каждому кортежу применяется функция sum
# result = map(sum, group_numbers)
# print(list(result))  # [6, 15, 24]


# result = map(int, input().split())
# # print(list(result))
# print(sum(result))



# numbers = [1, 2, 4, 5, 7, 9, 10, 11]
# # Из списка выбираются только чётные числа
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# print(list(even_numbers))  # [2, 4, 10]
# print(numbers)


# data = [0, 1, False, True, '', 'Python', [], [1, 2, 3]]
# # Из списка выбираются только те элементы, которые оцениваются как True
# even_numbers = filter(None, data)
# print(even_numbers)
# print(list(even_numbers))


# from functools import reduce

# numbers = [1, 2, 3, 4]
# # Умножение всех элементов списка последовательно
# result = reduce(lambda x, y: x * y, numbers)
# print(result)  # 24
#
#
# numbers = [1, 2, 3, 4]
# # Умножение всех элементов списка, начиная с 10
# result = reduce(lambda x, y: x * y, numbers, 10)
# print(result)  # 240

# words = [
#     'mango', 'grape', 'apple', 'Strawberry',
#     'Banana', 'pineapple', 'kiwi', 'blueberry'
# ]
#
# result = sorted(
#     words,
#     key=lambda word: (word[0].lower(), word[-1])
# )
#
# print(result)
#
# # или лямбда
# words = [
#     'mango', 'grape', 'apple', 'Strawberry',
#     'Banana', 'pineapple', 'kiwi', 'blueberry'
# ]
#
# def sort_key(word):
#     return (word[0].lower(), word[-1])
#
# result = sorted(words, key=sort_key)
# print(result)