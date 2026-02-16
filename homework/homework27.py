"""Python Fundamentals 2025: Домашнее задание 27
Фильтрация по ключевому слову
Напишите программу, которая ищет в файле все строки, содержащие указанное пользователем слово, и сохраняет их в новый файл.
Имя нового файла формируется как <keyword>_<original_filename>.
Если файл не существует, программа должна вывести ошибку.
Если совпадения не найдены, новый файл не создаётся.
Используйте файл system_log.txt.
Пример ввода:
Введите имя файла для поиска: system_log.txt
Введите ключевое слово: error
Пример вывода:
Строки, содержащие 'error', сохранены в error_system_log.txt."""

import os

input_filename = input("Введите имя файла для поиска: ")
keyword = input("Введите ключевое слово: ").lower()
# Формирование имени выходного файла
dir_name, base_name = os.path.split(input_filename)
output_filename = os.path.join(dir_name, f"{keyword}_{base_name}")


try:
    with open(input_filename, "r", encoding="utf-8") as infile:
        matched_lines = [line for line in infile if keyword in line.lower()]

        if matched_lines:
            with open(output_filename, "w", encoding="utf-8") as outfile:
                outfile.writelines(matched_lines)

            print(f"Строки, содержащие '{keyword}', сохранены в '{output_filename}'.")
        else:
            print(f"Совпадений с '{keyword}' не найдено. Файл не создан.")

except FileNotFoundError:
    print(f"Ошибка: Файл '{input_filename}' не найден.")

"""Поиск и удаление дубликатов
Напишите программу, которая удаляет дублирующиеся строки из файла и сохраняет результат в новый файл.
Имя нового файла формируется как unique_<original_filename>.
Если файл не существует, программа должна вывести ошибку.
Исходный порядок строк должен сохраниться.
Если в файле нет дубликатов, создаётся точная копия файла.
Используйте файл movies_to_watch.txt.
Пример ввода:
Введите имя файла: movies_to_watch.txt
Пример вывода:
Дубликаты удалены. Уникальные строки сохранены в unique_movies_to_watch.txt."""

import os

input_filename = input("Введите имя файла: ")
dir_name, base_name = os.path.split(input_filename)
output_filename = os.path.join(dir_name, f"unique_{base_name}")

try:
    with (open(input_filename, "r", encoding="utf-8") as infile,
          open(output_filename, "w", encoding="utf-8") as outfile):
        seen = set()
        for line in infile:
            if line not in seen:
                seen.add(line)
                outfile.write(line)
        print(f"Дубликаты удалены. Уникальные строки сохранены в '{output_filename}'.")
except FileNotFoundError:
    print(f"Ошибка: Файл '{input_filename}' не найден.")