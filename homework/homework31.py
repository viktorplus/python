"""Python Fundamentals 2025: Домашнее задание 31
1. Извлечение дат
Реализуйте программу, которая должна:
Найти в тексте все даты в форматах DD/MM/YYYY, DD-MM-YYYY и DD.MM.YYYY.

Данные:
text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."

Пример вывода:
15/03/2025
01.12.2024
09-09-2023
28/02/2022
"""

# import re
# text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."
# pattern = r"\b\d{2}[-/.]\d{2}[-/.]\d{4}\b"
# dates = re.findall(pattern, text)
#
# for d in dates:
#     print(d)

"""
2. Разделение списка тегов
Реализуйте программу, которая должна:
Прочитать строку с тегами, введёнными пользователем.
Разделить её на отдельные теги, независимо от того, чем они были разделены (запятые, точки с запятой, слэши или пробелы).
Удалить лишние пробелы и пустые значения.
Данные:
tag_input = "python, data-science / machine-learning; AI neural-networks"
Пример вывода:
['python', 'data-science', 'machine-learning', 'AI', 'neural-networks']"""

# import re
# tag_input = "python, data-science / machine-learning; AI  neural-networks;"
# # Разделение по , ; / и пробелам (один или несколько подряд)
# raw_tags = re.split(r"[\s,;/]+", tag_input)
# print(raw_tags)
# # Удаляем пустые элементы и лишние пробелы
# tags = [tag.strip() for tag in raw_tags if tag.strip()]
# print(tags)

# вариант 2

import re

tag_input = "python, data-science / machine-learning; AI  neural-networks;"
tags = [tag for tag in re.split(r"[\s,;/]+", tag_input) if tag]
print(tags)
