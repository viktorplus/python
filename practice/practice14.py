"""Фильтр чисел
Создайте генератор, который принимает список чисел и выдаёт только числа, кратные 5.
Данные:"""

# def gen(numbers):
#     for n in numbers:
#         if n % 5 == 0:
#             yield n
#
#
# numbers = [12, 15, 33, 40, 55, 62, 75, 83, 90]
#
# for value in gen(numbers):
#     print(value)

"""Создайте генератор, который принимает число n и генерирует квадраты чисел от 1 до n включительно
Данные:
n = 10
Пример вывода:
1
4
9
16
25
36
49
64
81
100"""


# def sq(n):
#     for i in range(1, n + 1):
#         yield i * i
#
#
# n = 10
# for value in sq(n):
#     print(value)
    # 2 IRINA
"""def square_num(n):
   for num in range(1, n + 1):
       yield num ** 2

gen = square_num(10)
for square in gen:
   print(square)
n = 10"""

"""Генератор, аналогичный range()
Создайте генератор, который повторяет функциональность range(),
принимая start, stop, step и возвращая последовательность чисел.
Данные:
start = 2
stop = 10
step = 2
Пример вывода:
2
4
6
8"""


# def my_range(start, stop, step):
#     if step == 0:
#         raise ValueError("step не может быть 0")
#
#     current = start
#
#     if step > 0:
#         while current < stop:
#             yield current
#             current += step
#     else:
#         while current > stop:
#             yield current
#             current += step
#
#
# # Данные
# start = 2
# stop = 10
# step = 2
#
# for num in my_range(start, stop, step):
#     print(num)
# ириенко
'''def my_range(stop, start=2, step=1):
    current = start
    while (step > 0 and current < stop) or (step < 0 and current > stop):
        yield current
        current += step


start = 2
stop = 10
step = 2

for number in my_range(stop=stop, step=step):
    # for number in my_range(start, stop, step):
    print(number)'''

"""2. Генератор случайных дат

Создайте генератор, который генерирует случайные даты в пределах одного года.
Генератор должен принимать год в качестве аргумента и выдавать следующую случайную дату при каждом вызове, учитывая количество дней в месяце, а также високосные годы.

Пример вывода:
2025-02-14
2025-06-28
2025-09-09
..."""

# import random
#
# def is_lip_year(year):
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
#
# def date_generator(year):
#     day_in_month = {
#         1: 31,
#         2: 29 if is_lip_year(year) else 28,
#         3: 31,
#         4: 30,
#         5: 31,
#         6: 30,
#         7: 31,
#         8: 31,
#         9: 30,
#         10: 31,
#         11: 30,
#         12: 31,
#     }
#     while True:
#         ran_month = random.randint(1, 12)
#         ran_day = random.randint(1, day_in_month[ran_month])
#         yield f"{year}--{ran_month:02d}--{ran_day:02d}"
#
#
#
# year = int(input("Enter Year"))
# ran_date = date_generator(year)
# for i in range(7):
#     print(next(ran_date))
#
#     # Сергей
#     import random
#
#     year = int(input("Enter year: "))
#
#
#     def is_leap_year(year):
#         return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
#
#
#     def date_generator(year: int):
#         day_in_month = {
#             1: 31,
#             2: 29 if is_leap_year(year) else 28,
#             3: 31,
#             4: 30,
#             5: 31,
#             6: 30,
#             7: 31,
#             8: 31,
#             9: 30,
#             10: 31,
#             11: 30,
#             12: 31}
#
#         while True:
#             ran_month = random.randint(1, 12)
#             ran_day = random.randint(1, day_in_month[ran_month])
#             yield f"{year}-{ran_month:02d}-{ran_day:02d}"
#
#
#     ran_date = date_generator(year)
#     for i in range(7):
#         print(next(ran_date))


"""5. Система распределения задач

Программа будет состоять из двух частей, работающих независимо:
Добавление задач – пользователь вводит новые задачи, и они записываются в файл.
Распределение задач – другая программа читает задачи из файла и назначает их сотрудникам по очереди.
Запустите обе программы одновременно.
5.1 Добавление задач
Эта программа запрашивает задачи у пользователя и записывает их в файл tasks.txt. Она работает в бесконечном цикле, пока пользователь не введёт exit.

Данные:
Файл tasks.txt – каждая строка содержит одно задание.
Пример файла:
Подготовить отчёт
Провести собрание
Проверить документацию
Разработать новый модуль
Настроить сервер

Пример вывода:
Введите задачу: Подготовить отчёт 
Введите задачу: Провести собрание 
Введите задачу: Проверить документацию 
Введите задачу: Разработать новый модуль 
Введите задачу: Настроить сервер 
Введите задачу: exit

5.2 Распределение задач

Эта программа читает файл tasks.txt и назначает задачи сотрудникам по очереди.
Она использует генератор для постепенного чтения новых задач и назначения сотрудникам.
Дополнительно: если файл tasks.txt отсутствует, программа делает 5 попыток с паузой 3 секунды перед завершением.

Данные:
employees = ["Alice", "Bob", "Charlie"]

Пример вывода:
Alice выполняет: Подготовить отчёт
Bob выполняет: Провести собрание
Charlie выполняет: Проверить документацию
Alice выполняет: Разработать новый модуль
Bob выполняет: Настроить сервер
"""


