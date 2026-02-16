"""Python Fundamentals 2025: Домашнее задание 26
Список файлов и папок
Напишите программу, которая принимает путь к директории через аргумент командной строки и выводит:
Отдельно список папок
Отдельно список файлов
Пример запуска
python script.py /home/user/documents
Пример вывода
Содержимое директории '/home/user/documents':
Папки:
- folder1
- folder2

Файлы:
- file1.txt
- file2.txt
- notes.docx
"""
import os
import sys

if len(sys.argv) != 2:
    print(f"Параметры запуска: python {sys.argv[0]} <path>")
    sys.exit(1)

list_dir = sys.argv[1]

if not os.path.isdir(list_dir):
    print("Директория не существует")
    sys.exit(1)

folders = []
files = []

for name in os.listdir(list_dir):
    path = os.path.join(list_dir, name)
    if os.path.isdir(path):
        folders.append(name)
    elif os.path.isfile(path):
        files.append(name)

print(f"Содержимое директории '{list_dir}':")
print("Папки:")
for f in folders:
    print(f"- {f}")

print("\nФайлы:")
for f in files:
    print(f"- {f}")


"""
Поиск и удаление файлов с указанным расширением
Напишите программу, которая:
Принимает путь к директории и расширение файлов через аргумент командной строки.
Рекурсивно ищет файлы с этим расширением во всех вложенных папках.
Спрашивает у пользователя, хочет ли он удалить найденные файлы.
Если пользователь подтверждает, удаляет их.
Пример запуска:
python script.py /home/user/PycharmProjects/project1 .log
Пример вывода
Найдены файлы с расширением '.log':
- logs/error.log
- logs/system.log
- logs/backup/old.log
- logs/backup/debug.log


Вы хотите удалить эти файлы? (y/n): y

Удаление завершено.

"""

import os
import sys

# Проверяем, передан ли аргумент
if len(sys.argv) != 3:
    print("Использование: python script.py <путь к папке> <расширение>")
    sys.exit(1)

path_to_folder = sys.argv[1]
extension = sys.argv[2]
found_files = []

# Рекурсивный поиск файлов
for root, _, files in os.walk(path_to_folder):
    for file in files:
        if file.endswith(extension):
            found_files.append(os.path.join(root, file))

# Если файлов нет, завершаем программу
if not found_files:
    print(f"Файлы с расширением '{extension}' не найдены.")
    sys.exit(0)

# Выводим список файлов
print(f"Найдены файлы с расширением '{extension}':")
for file in found_files:
    print("-", file)

# Спрашиваем у пользователя, хочет ли он их удалить
confirm = input("\nВы хотите удалить эти файлы? (y/n): ")
if confirm.lower() == "y":
    # Удаляем файлы
    for file in found_files:
        os.remove(file)
    print("Удаление завершено.")
else:
    print("Удаление отменено.")
