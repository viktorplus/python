"""Python Fundamentals 2025: Домашнее задание 21
Повторения букв
Реализуйте функцию, которая принимает текст и возвращает словарь с подсчётом количества каждой буквы, игнорируя регистр.
Данные:
text = "Programming is fun!"
Пример вывода:
{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}"""

# from collections import Counter
# text = "Programming is fun!"
#
# def text_to_dict (text):
#     return dict(Counter(text.replace('!', '').replace('.', '').replace(',', '').replace(' ', '').lower()))
#
# print(text_to_dict(text))

# вариант 2
# from collections import Counter
#
# def text_to_dict(text):
#     letters = [c.lower() for c in text if c.isalpha()]
#     # letters = [c for c in text.lower() if c.isalpha()]
#
#     return dict(Counter(letters))
#
# text = "Programming is fun!"
# print(text_to_dict(text))


"""Группировка студентов по классам
Создайте структуру для группировки студентов по классам.
Добавьте студентов в соответствующие группы.
Данные:
students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
Пример вывода:
{'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}"""

# from collections import defaultdict
# students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
#
# def group_by_class(students):
#     grouped = defaultdict(list)
#     for cls, name in students:
#         grouped[cls].append(name)
#     return dict(grouped)

# вариант без распаковки
# def group_by_class (students):
#     grouped = defaultdict(list)
#     for student in students:
#         grouped[student[0]].append(student[1])
#     return dict(grouped)

# вариант если обычный словарь с if
# def group_by_class(students):
#     grouped = {}
#     for cls, name in students:
#         if cls not in grouped:
#             grouped[cls] = []
#         grouped[cls].append(name)
#     return grouped

# вариант обычный словарь через setdefault
# def group_by_class(students):
#     grouped = {}
#     for cls, name in students:
#         grouped.setdefault(cls, []).append(name)
#     return grouped



# print(group_by_class(students))

