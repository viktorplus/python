"""Python Fundamentals 2025: Домашнее задание 33

Среднее время выполнения
Создайте декоратор measure_time, который измеряет и выводит среднее время выполнения функции за 5 вызовов.
Функция может быть любой: например, сортировка списка, чтение из файла или расчёты.
Пример:
@measure_time
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

Пример вывода:
Среднее время выполнения для 5 вызовов: 0.21 секунд Результат: 49999995000000"""



import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        total_time = 0
        result = None
        repeats = 5
        for _ in range(repeats):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            total_time += (end - start)
        average = total_time / repeats
        print(f"Среднее время выполнения для {repeats} вызовов: {average:.2f} секунд")
        return result
    return wrapper

@measure_time
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

print("Результат:", compute())

"""Среднее время выполнения с количеством вызовов

Доработайте декоратор measure_time, чтобы он принимал параметр repeats — количество вызовов функции.
Декоратор должен выполнять функцию указанное число раз и выводить среднее время выполнения.
Пример вывода:
Среднее время выполнения для 10 вызовов: 0.21 секунд Результат: 49999995000000
"""

import time

def measure_time(repeats=5):
    def decorator(func):
        def wrapper():
            total_time = 0
            result = None
            for _ in range(repeats):
                start = time.time()
                result = func()
                end = time.time()
                total_time += (end - start)
            average = total_time / repeats
            print(f"Среднее время выполнения для {repeats} вызовов: {average:.2f} секунд")
            return result
        return wrapper
    return decorator

@measure_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

print("Результат:", compute())