# import sys
#
# list_comp = [x**2 for x in range(10**6)]  # Списковое включение
# gen_expr = (x**2 for x in range(10**6))  # Генераторное выражение
#
# print("Размер списка:", sys.getsizeof(list_comp), "байт")
# print("Размер генератора:", sys.getsizeof(gen_expr), "байт")


# words = ["apple", "Banana", "cherry", "Apricot"]
#
# print(any(word[0].isupper() for word in words))  # Есть слово с заглавной буквы
# print(all(len(word) > 3 for word in words))  # Все слова длиннее 3 букв
#


# def generate_values():
#     print("Начало работы")
#     yield 1  # Приостанавливаем выполнение и возвращаем 1
#     print("Продолжение работы")
#     yield 2  # Приостанавливаем выполнение и возвращаем 2
#     print("Завершение работы")
#     return "---------"
#
# # Создаём генератор, но код внутри функции пока не выполняется
# gen = generate_values()
#
# print(next(gen))  # Начало работы → 1
# print(next(gen))  # Продолжение работы → 2
# try:
#     print(next(gen)) # Завершение работы → StopIteration, так как нет третьего yield
# except StopIteration as e:
#     print(e.value)

# def count_up_to(n):
#     count = 1
#     while count <= n:
#         yield count  # Возвращаем текущее значение и "замораживаем" выполнение
#         count += 1   # После следующего вызова next() продолжится отсюда
#
# gen = count_up_to(5)
#
# for number in gen:
#     print(number)


# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# # print(next(gen))  # StopIteration

# def infinite_counter():
#     count = 1
#     while True:  # Бесконечный цикл
#         yield count
#         count += 1
#
#
# gen = infinite_counter()
#
# for number in gen:
#     if number > 5:  # Условие выхода
#         break  # Принудительная остановка генератора
#     print(number)
#
# print()
#
# # Вызов next 10 раз
# for _ in range(10):
#     print(next(gen))


# def task_assigner(employees):
#     while True:
#         for employee in employees:
#             yield employee
#
#
# # Список сотрудников
# team = ["Alice", "Bob", "Charlie"]
#
#
# # Создаём генератор распределения задач
# assigner = task_assigner(team)
#
#
# # Назначаем 7 задач
# for i in range(7):
#     print(f"Task {i + 1} assigned to: {next(assigner)}")
#
# print(f"Task {7 + 1} assigned to: {next(assigner)}")


# def sensor_data(data):
#     for value in data:
#         yield value
#
# numbers = [10, 20, 30, 40, 50]
# gen = sensor_data(numbers)
#
# for element in gen:
#     print("Получено значение:", element)
#
#     # Завершаем генератор, когда получено нужное значение
#     if element >= 30:
#         print("Значение найдено, закрываем генератор.")
#         gen.close()
#
# # next(gen)  # Вызовет ошибку

#
# def letters():
#     # yield "ABC"
#     yield from "ABC"
#
# gen = letters()
#
# print(next(gen))  # A
# print(next(gen))  # B
# print(next(gen))  # C


# # Умеет работать с одним объектом
# def process_values(data):
#     for value in data:
#         yield value * 2
#
# # Собирает несколько объектов
# def main_generator(*sequences):
#     # Делегирует обработку каждого объекта вспомогательному генератору
#     for seq in sequences:
#         yield from process_values(seq)
#
# # Используем несколько источников данных
# data1 = [1, 2, 3]
# data2 = [10, 15]
#
# for result in main_generator(data1, data2):
#     print(result)
