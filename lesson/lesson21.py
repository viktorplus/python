# import time
#
# current_time = time.time()
# print(current_time)

# import time
#
# time.sleep(2)  # Задержка на 2 секунды
# print("2 секунды спустя...")


# import time
# start_time = time.time()
# # Создание объекта range
# # range(0, 1000000, 1)
# range_million = range(1000000)
# end_time = time.time()
# print(f"Время создания range: {end_time - start_time:.10f} секунд")
#
# start_time = time.time()
# # Создание объекта списка
# # 0, 1, 2, 3, 4, 5, 6, ...
# lst = [x for x in range(1000000)]
# end_time = time.time()
# print(f"Время создания list: {end_time - start_time:.10f} секунд")


# # Импорт класса из модуля collections
# from collections import OrderedDict
# # Создание пустого OrderedDict
# od = OrderedDict()
# # Добавление элементов аналогично работе со словарем
# od["a"] = 1
# od["b"] = 2
# od["c"] = 3
# print(od)


# from collections import OrderedDict
# od = OrderedDict()
# od["a"] = 1
# od["b"] = 2
# od["c"] = 3
# od["d"] = 4
# # Удаление последнего элемента
# print(od.popitem())
# print(od)
# # Удаление первого элемента
# print(od.popitem(last=False))
# print(od)

# from collections import OrderedDict
# queue = OrderedDict()
# queue["first"] = 1
# queue["second"] = 2
# queue["third"] = 3
# # Удаляем элементы с начала очереди
# while queue:
#     print(queue.popitem(last=False))


# from collections import OrderedDict
# queue = OrderedDict()
# queue["task1"] = "low priority"
# queue["task2"] = "medium priority"
# queue["task3"] = "low priority"
# queue["task4"] = "high priority"
# queue["task5"] = "medium priority"
# # Собираем ключи для перемещения
# keys_to_end = [key for key, value in queue.items() if "low" in value]
# keys_to_start = [key for key, value in queue.items() if "high" in value]
# # Перемещаем задачи с низким приоритетом в конец
# for key in keys_to_end:
#     queue.move_to_end(key)
# # Перемещаем задачи с высоким приоритетом в начало
# for key in keys_to_start:
#     queue.move_to_end(key, last=False)
# print(queue)


# from time import time, sleep
# from functools import lru_cache
# # Функция с временной задержкой для имитации сложных вычислений
# @lru_cache(maxsize=1)
# def compute_square(n):
#     print(f"Вычисляю квадрат числа {n}...")
#     sleep(2)  # Имитация долгой операции
#     return n * n # Измерение времени выполнения
#
#
# start_time = time()
# print(f"Результат: {compute_square(2)}")  # Вычисляет
# print(f"Время: {time() - start_time:.2f} секунд\n")
# start_time = time()
# print(f"Результат: {compute_square(3)}")  # Вычисляет
# print(f"Время: {time() - start_time:.2f} секунд\n")
# start_time = time()
# print(f"Результат: {compute_square(3)}")  # Использует кэш
# print(f"Время: {time() - start_time:.2f} секунд\n")
# # print(f"Результат: {compute_square(4)}")  # Вычисляет
# # print(f"Результат: {compute_square(5)}")  # Вычисляет
# #
# # start_time = time()
# # print(f"Результат: {compute_square(2)}")  # Использует кэш
# # print(f"Время: {time() - start_time:.2f} секунд\n")

#
# from collections import defaultdict
#
# dd = defaultdict(int)
# print(dd['missing'])  # Добавлено значение 0
# print(dd['missing2'])  # Добавлено значение 0
# print(dd['missing3'])  # Добавлено значение 0
# print(dd)


# from collections import defaultdict
#
# # Словарь с числовым значением по умолчанию
# dd = defaultdict(int)
# # Присваивает ключу базовое значение int
# print(dd['a'])
# # Обновляет имеющийся ключ
# dd['a'] += 1
# print(dd['a'])
# # Присваивает ключу базовое значение int и обновляет его
# dd['b'] += 10
# print(dd['b'])
# print(dd)

# from collections import defaultdict
#
# # Словарь с пустым списком по умолчанию
# dd = defaultdict(list)
# # Присваивает ключу базовое значение list и обновляет его
# dd['a'].append(1)
# # Обновляет список по имеющемуся ключу
# dd['a'].append(2)
# # Присваивает ключу базовое значение list и обновляет его
# dd['b'].append(10)
# print(dd)


# from collections import defaultdict
#
# # Пользовательская функция для значения по умолчанию
# def default_value():
#     return "default"
#
# dd = defaultdict(default_value)
# print(dd['missing_key'])
# print(dd)
#
# # Обычный словарь
# my_dict = {}
# if 'a' not in my_dict:
#     my_dict['a'] = []
# my_dict['a'].append(1)
#
# defaultdict
# from collections import defaultdict
# dd = defaultdict(list)
# dd['a'].append(1)

# from collections import defaultdict
#
# dd = defaultdict(list)
# dd['x'].append(1)
# dd['y'].extend([2, 3])
# print(dd['z'])
# print(dd)


# 1. Подсчёт символов в строке:
# from collections import Counter
# text = "hello world"
# counter = Counter(text)
# print(counter)
# # 2. Подсчёт слов в списке:
# from collections import Counter
# words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
# counter = Counter(words)
# print(counter)
# # 3. Создание Counter из словаря:
# from collections import Counter
# data = {"apple": 3, "banana": 2, "cherry": 1}
# counter = Counter(data)
# print(counter)

from collections import Counter
# counter = Counter("banana")
# print(counter.most_common(2))

#
# counter = Counter({"a": 3, "b": 1, "c": 0})
# iter_count = counter.elements()
# print(list(iter_count))


# counter = Counter("banana")
# counter.subtract("an")
# print(counter)

# counter = Counter("banana")
# counter.update("nan")
# print(counter)

# counter = Counter("banana")
# counter.subtract({"a": 3})
# print(counter)

# c1 = Counter("banana")
# c2 = Counter("apple")
# print(c1)
# print(c2)
# print(c1 + c2)
#
#
# c1 = Counter("banana")
# c2 = Counter("an")
# print(c1 - c2)
#
#
# c1 = Counter("banana")
# c2 = Counter("aan")
# print(c1 & c2)
#
#
# c1 = Counter("banana")
# c2 = Counter("anc")
# print(c1 | c2)
# print("".join(c1.elements()))


