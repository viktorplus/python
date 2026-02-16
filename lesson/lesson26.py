# absolute_path = "C:\\Users\\User\\Documents\\file.txt"
# absolute_path = "C:\Users\User\Docu/ments\file.txt"
# absolute_path = "/home/user/documents/file.txt"

# import os
#
# # Получаем текущую рабочую директорию
# current_dir = os.getcwd()
# print(f"Текущая директория: {current_dir}")

# import os
#
# # Переход в директорию с использованием относительного пути
# # os.chdir("./subdirectory")  # Ошибка, если директории нет!
# print(f"Текущая директория: {os.getcwd()}")
#
# # Переход в родительскую директорию
# os.chdir("..")
# print(f"Текущая директория после перехода: {os.getcwd()}")
#
# # Переход в директорию с использованием абсолютного пути
# os.chdir("/home/tanya/itch/SQL")  # Замените путь на существующий
# print(f"Текущая директория: {os.getcwd()}")

#
# import os
#
# # Проверка существования файла
# # file_path = "example.txt"
# # или
# file_path = "example_folder/example.txt"
# if os.path.exists(file_path):
#     print(f"Файл '{file_path}' существует.")
# else:
#     print(f"Файл '{file_path}' не найден.")
#
# # Проверка существования директории
# directory_path = "example_folder"
# # или
# # directory_path = "parent_folder/child_folder"
# if os.path.exists(directory_path):
#     print(f"Директория '{directory_path}' существует.")
# else:
#     print(f"Директория '{directory_path}' не найдена.")

#
# import os
# # os.chdir("..")
# # Список содержимого текущей директории
# contents = os.listdir(".")
# print("Содержимое текущей директории:", contents)
#
# # Список содержимого указанной директории
# specific_dir = "parent_folder"
# if os.path.exists(specific_dir):
#     print(f"Содержимое директории '{specific_dir}':", os.listdir(specific_dir))

# import os
#
# dir_path = "example_folder"
# # os.mkdir("example_folder")
# if not os.path.exists(dir_path):
#     # Создание одной директории
#     os.mkdir("example_folder")
#     print(f"Директория '{dir_path}' создана.")
# else:
#     print(f"Директория '{dir_path}' существует.")
#
# # Создание вложенных директорий
# os.makedirs("parent_folder/child_folder", exist_ok=True)
# print("Вложенные директории 'parent_folder/child_folder' созданы.")

# # Создание нового пустого файла
# file_name = "example.txt"
# open(file_name, "w").close()
# print(f"Файл '{file_name}' создан или перезаписан.")

import os

file_path = "example.txt"
# # Проверяем, существует ли объект
# if os.path.exists(file_path):
#     # Проверяем, является ли файлом
#     if os.path.isfile(file_path):
#         print(f"'{file_path}' существует и это файл.")
#     else:
#         print(f"'{file_path}' существует, но это не файл.")
# else:
#     print(f"'{file_path}' не существует.")

# if os.path.isfile(file_path):
#     print(f"'{file_path}' существует и это файл.")
# else:
#     print(f"'{file_path}' существует, но это не файл.")


# import os

# # path = "example.txt"
# path = "parent_folder"
#
# # Проверяем, является ли файлом
# if os.path.isfile(path):
#     print(f"'{path}' существует и это файл.")
# # Проверяем, является ли директорией
# elif os.path.isdir(path):
#     print(f"'{path}' существует и это директория.")
#
# print(os.path.isfile(path))


# import os
#
# # Переименование файла
# old_file_name = "example.txt"
# new_file_name = "renamed.txt"
# if os.path.exists(old_file_name):
#     os.rename(old_file_name, new_file_name)
#     print(f"Файл переименован в '{new_file_name}'.")
# else:
#     print(f"Файл '{old_file_name}' не найден.")
#
# # Переименование директории
# old_dir_name = "example_folder"
# new_dir_name = "renamed_folder"
# if os.path.exists(old_dir_name):
#     os.rename(old_dir_name, new_dir_name)
#     print(f"Директория переименована в '{new_dir_name}'.")
# else:
#     print(f"Директория '{old_dir_name}' не найдена.")

import os

# # Удаление файла
# file_to_delete = "renamed.txt"
# if os.path.exists(file_to_delete):
#     os.remove(file_to_delete)
#     print(f"Файл '{file_to_delete}' удалён.")
# else:
#     print(f"Файл '{file_to_delete}' не найден, удаление невозможно.")
#
# # Удаление пустой директории
# empty_dir_to_delete = "subdirectory"
# if os.path.exists(empty_dir_to_delete):
#     os.rmdir(empty_dir_to_delete)
#     print(f"Пустая директория '{empty_dir_to_delete}' удалена.")
# else:
#     print(f"Директория '{empty_dir_to_delete}' не найдена или не пуста.")


# import os
#
# path = "/directory/subdirectory/example.txt"
#
# # Разделение пути на директорию и файл
# directory, file = os.path.split(path)
# print(f"Директория: {directory}, Файл: {file}")
#
# # Получение только имени файла
# print(f"Имя файла: {os.path.basename(path)}")
#
# # Получение только директории
# print(f"Директория: {os.path.dirname(path)}")

#
# import os
#
# # Относительный путь
# relative_path = "example.txt"
#
# # Преобразование в абсолютный путь
# absolute_path = os.path.abspath(relative_path)
# print(f"Абсолютный путь: {absolute_path}")


# import os
#
# # Объединение нескольких компонентов
# current_dir = os.getcwd()
# print(current_dir)
# sub_dir = "docs"
# file_name = "data.txt"
# full_path = os.path.join(current_dir, sub_dir, file_name)
# print(f"Путь: {full_path}")

# import os
# # Рекурсивный обход директории
# for root, dirs, files in os.walk("."):
#     print(f"Текущая директория: {root}")
#     print(f"Поддиректории: {dirs}")
#     print(f"Файлы: {files}")
#     print("-" * 50)

# import os
#
# # Поиск всех .txt файлов
# for root, dirs, files in os.walk("."):
#     for file in files:
#         if file.endswith(".txt"):
#             print(f"Найден файл: {os.path.join(root, file)}")


# import sys
#
# # Вывод всех аргументов командной строки
# print("Все аргументы:", sys.argv)
# # Работа с первым аргументом (если он передан)
# if len(sys.argv) > 1:
#     print(f"Переданный аргумент: {sys.argv[1]}")
# else:
#     print("Аргументы не переданы.")

# import sys
# if len(sys.argv) > 1:
#     for i, arg in enumerate(sys.argv[1:], start=1):
#         print(f"Аргумент {i}: {arg}")
# else:
#     print("Аргументы не переданы.")

# import os
# import sys
#
# # Проверяем, передан ли аргумент
# if len(sys.argv) != 2:
#     print("Использование: python script.py <расширение>")
#     sys.exit(1)
#
# extension = sys.argv[1]
#
# # Удаляем файлы с указанным расширением
# for file_name in os.listdir("."):
#     if file_name.endswith(extension):
#         os.remove(file_name)
#         print(f"Удалён файл: {file_name}")

# import sys
# import os
#
# # Проверяем, передан ли аргумент
# if len(sys.argv) != 2:
#     print("Использование: python script.py <директория>")
#     sys.exit(1)
# print(sys.argv)
# directory = sys.argv[1]
#
# # Проверяем существование директории
# if not os.path.isdir(directory):
#     print(f"Директория '{directory}' не существует.")
#     sys.exit(1)
#
# # Выводим содержимое директории
# print(f"Содержимое директории '{directory}':")
# for item in os.listdir(directory):
#     print(f"- {item}")


import sys
import logging

# Проверяем количество аргументов
if len(sys.argv) != 2:
    print("Использование: python script.py <режим>")
    print("<режим> - debug или release")
    sys.exit(1)

# Получаем режим работы
mode = sys.argv[1]

# Проверяем корректность режима
if mode not in ["debug", "release"]:
    print("Ошибка: режим должен быть 'debug' или 'release'.")
    sys.exit(1)

# Настройка логирования
log_level = logging.DEBUG if mode == "debug" else logging.INFO
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=log_level
)
# Пример событий во время выполнения программы
logging.info("Инициализация программы")
logging.debug("Чтение конфигурации")
logging.debug("Подключение к базе данных")
logging.info("Обработка данных")
logging.critical("Критическая ошибка: соединение с базой данных потеряно!")
logging.info("Завершение работы программы")



