# """ 1. Подсчёт частоты слов в файле
#
# Напишите программу, которая подсчитывает, сколько раз каждое слово встречается в файле (не учитывая регистр).
# Программа запрашивает имя файла и количество популярных слов для вывода.
# Если указанный файл не существует, программа должна вывести ошибку.
# Используйте файл text.txt. """
#
# from collections import Counter
#
# def word_counter(file_name, count):
#     with open(file_name, "r", encoding="utf-8") as file:
#         content = file.read()
#         content = content.replace('!', ' ').replace(',', ' ').replace('.', ' ')
#         return Counter(content.split()).most_common(count)
#
# try:
#     print(word_counter("Praktikum/text.txt", 3))
# except FileNotFoundError as e:
#     print(e)

