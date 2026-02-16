"""Python Fundamentals 2025: Домашнее задание 28
План по дням недели
Напишите программу, которая помогает планировать дела.
Программа должна бесконечно выводить план на следующий день недели, пока пользователь нажимает 'Enter'.
Данные:
# Расписание дел на неделю

Пример ввода:
Нажмите 'Enter' для получения плана:
Monday: Gym, Work, Read book
Нажмите 'Enter' для получения плана:
Tuesday: Meeting, Work, Study Python
...
Нажмите 'Enter' для получения плана:
Sunday: Family time, Rest
Нажмите 'Enter' для получения плана:
Monday: Gym, Work, Read book
Нажмите 'Enter' для получения плана: q
"""

weekly_schedule = {
    "Monday": ["Gym", "Work", "Read book"],
    "Tuesday": ["Meeting", "Work", "Study Python"],
    "Wednesday": ["Shopping", "Work", "Watch movie"],
    "Thursday": ["Work", "Call parents", "Play guitar"],
    "Friday": ["Work", "Dinner with friends"],
    "Saturday": ["Hiking", "Rest"],
    "Sunday": ["Family time", "Rest"]
}
#
# iterator = iter(weekly_schedule.items())
#
# while True:
#     input("Нажмите 'Enter' для получения плана: ")
#     for day, tasks in iterator:          # for идёт по итератору
#         print(f"{day}: {', '.join(tasks)}")
#         break                            # показываем только 1 день за Enter
#
#     else:
#         # итератор закончился (for дошёл до конца без break) — начинаем неделю заново
#         iterator = iter(weekly_schedule.items())

# # вариант 2
#
# iterator = iter(weekly_schedule.items())
#
# while True:
#     input("Нажмите 'Enter' для получения плана: ")
#
#     try:
#         day, tasks = next(iterator)
#     except StopIteration:
#         iterator = iter(weekly_schedule.items())
#         day, tasks = next(iterator)
#
#     print(f"{day}: {', '.join(tasks)}")
#
# вариант 3
# import itertools
#
# cycled = itertools.cycle(weekly_schedule.items())
# while True:
#     input("Enter — следующий день: ")
#     day, tasks = next(cycled)
#     print(f"{day}: {', '.join(tasks)}")



""" Объединение списков продуктов
Напишите функцию, которая принимает несколько списков с названиями продуктов и возвращает генератор, содержащий все продукты в нижнем регистре.
Выведите содержимое генератора.
Данные:

Пример вывода:
apple
banana
orange
carrot
tomato
cucumber
milk
cheese
yogurt
"""

# import itertools
#
# def merge_list(*lists):
#     return (item.lower() for item in itertools.chain(*lists))
#
# fruits = ["Apple", "Banana", "Orange"]
# vegetables = ["Carrot", "Tomato", "Cucumber"]
# dairy = ["Milk", "Cheese", "Yogurt"]
#
# gen = merge_list(fruits, vegetables, dairy)
#
# for product in gen:
#     print(product)




""" Комбинации одежды
Напишите функцию, которая принимает списки типов одежды, цветов и размеров, а затем генерирует все возможные комбинации
в формате "Clothe - Color - Size".
Данные:

Пример вывода:
T-shirt - Red - S
T-shirt - Red - M
T-shirt - Red - L
T-shirt - Blue - S
...
Jacket - Black - L
"""
import itertools

def outfit_combinations(clothes, colors, sizes):
    return (f"{clothe} - {color} - {size}" for clothe, color, size in itertools.product(clothes, colors, sizes))

clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

for combo in outfit_combinations(clothes, colors, sizes):
    print(combo)


