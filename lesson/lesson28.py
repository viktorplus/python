# e = enumerate([1, 2, 3])
# print(list(e))
# print(list(e))
#
# e = zip([1, 2, 3], [1, 2, 3])
# print(e)
# print(list(e))
# print(list(e))
#
# numbers = [10, 20, 30]  # Обычный список
# iterator = numbers.__iter__()  # Получаем итератор
#
# print(iterator)  # Итератор для списка
# print(list(iterator))  # Преобразование в список
#
# print(list(iterator))  # Второй раз список будет пустой
#
# print([1, 2, 3].__str__())
# print([1, 2, 3])
import sys

# numbers = [10, 20, 30]
# iterator = numbers.__iter__()  # Создаём итератор
# # iterator[2]
# print(iterator.__next__())  # Получаем нулевой элемент
# print(iterator.__next__())  # Получаем первый элемент
# print("-" * 30)  # Можно прерваться на другие действия
# # print(iterator.__next__())  # Получаем второй элемент
# print(list(iterator))


# numbers = [1, 2, 3]  # Итерируемый объект
# iterator = iter(numbers)  # Вызывает numbers.__iter__()
#
# print(next(iterator))  # Вызывает iterator.__next__()
# print(next(iterator))  # Вызывает iterator.__next__()
# print(next(iterator))  # Вызывает iterator.__next__()


# import sys
#
# # Список из 1 000 000 чисел
# numbers_list = [x for x in range(1_000_000)]
# print("Размер списка:", sys.getsizeof(numbers_list), "байт")
#
# # Итератор, из списка
# numbers_iterator = numbers_list.__iter__()
# print("Размер итератора:", sys.getsizeof(numbers_iterator), "байт")
#
# # Итератор, из списка
# numbers_zipiterator = zip(numbers_list, numbers_list)
# print("Размер итератора:", sys.getsizeof(numbers_zipiterator), "байт")

#
# numbers = [1, 2, 3]
# iterator = iter(numbers)  # Создаём итератор
# iterator2 = iter(numbers)  # Создаём итератор
# # numbers[0] = "new"
# #
# #
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))  # Последний элемент
# numbers.append(4)
# print(next(iterator))  # Последний элемент
# print(list(iterator))
# print(list(iterator2))
# print(list(iterator2))
# # # print(next(iterator))  # Ошибка StopIteration

# numbers = [1, 2, 3]
# iterator = iter(numbers)
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# # None вместо StopIteration
# print(next(iterator, None))
# # 0 вместо StopIteration
# print(next(iterator, 0))


# [].__iter__()
# "".__iter__()
# "".__next__()
# iterator.__next__()

# numbers = [10, 20, 30]  # Итерируемый объект
# iterator = iter(numbers)  # Создание итератора
#
# while True:
#     try:
#         num = next(iterator)  # Получаем следующий элемент
#         print(num)
#     except StopIteration:
#         break  # Завершаем цикл при окончании элементов

# import itertools
#
# counter = itertools.count(start=1)
#
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
#
# # for n in counter:
# #     print(n)


#
# import itertools
#
# cycler = itertools.cycle(["A", "B", "C"])
#
# print(next(cycler))
# print(next(cycler))
# print(next(cycler))
# print(next(cycler))  # A (повторяется)
# print(next(cycler))  # B (повторяется)

#
# import itertools
#
# merged = itertools.chain([1, 2, 3], [[100, 200], 300])
# print(merged)
# l = list(merged)
# print(l)
# print(itertools.chain(l))

#
# import itertools
#
# pairs = itertools.product([1, 2, 3], ["A", "B", "C"])
# print(pairs)
# print(list(pairs))
#
# import itertools
#
# letters = ["A", "B", "C"]
#
# # Все возможные перестановки
# perms = itertools.permutations(letters)
# print(list(perms))
#
# # Все возможные перестановки длины 2
# perms = itertools.permutations(letters, 2)
# print(list(perms))


# # Генерирует квадраты чисел от 0 до 4
# squares = (x ** 2 for x in range(5))
#
# print(squares)  # Объект генератора
# print(type(squares))  # Объект генератора
#
# print(next(squares))
# print(next(squares))
# print(next(squares))
# print("-----------")
# print(next(squares))
# print(next(squares))

amount = 0
squares = (x ** 2 for x in range(500000))
list_squares = [x ** 2 for x in range(500000)]
print(sys.getsizeof(squares))
print(sys.getsizeof(list_squares))

# for num in squares:
#     print(num)
