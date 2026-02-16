# # Можно указать просто "r", а не mode="r"
# file = open("data/example.txt", "r", encoding="utf-8")  # Открываем файл для чтения
# content = file.read()  # Читаем содержимое файла
# print(content)
# file.close()  # Закрываем файл вручную


# with open("example.txt") as file:
#     content = file.read()
#     print(content)
#
# # content = file.read()


# with open("example.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#     print(type(content))
#     print(content)


# with open("example.txt", "r", encoding="utf-8") as file:
#     content = file.read(10)  # Читаем первые 10 символов
#     print(content)


# with open("example.txt", "r", encoding="utf-8") as file:
#     print(file.readline(), end="")
#     print(file.readline(), end="")
#     print(file.readline(), end="")


# with open("example.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
#     print(type(lines))
#     print(lines)
#     print(len(lines))
#     print(*lines, sep="")


# with open("users.txt", "w", encoding="utf-8") as file:
#     file.write("ID: 201 | Name: John | Age: 25 | Status: Active\n")
#     file.write("ID: 201 | Name: John | Age: 25 | Status: Active\n")

# data = [
#     "ID: 202 | Name: Alice | Age: 30 | Status: Inactive\n",
#     "ID: 203 | Name: Bob | Age: 27 | Status: Active\n"
# ]
#
# with open("users.txt", "w", encoding="utf-8") as file:
#     file.writelines(data)

# with open("users2.txt", "a", encoding="utf-8") as file:
#     file.write("Дополнительная строка\n")

# with open("users.txt", "r+", encoding="utf-8") as file:
#     content = file.read()  # Читаем текущие данные
#     file.write("\nДобавленный текст")  # Записываем новые данные


# try:
#     with open("new_file.txt", "x", encoding="utf-8") as file:
#         file.write("Этот файл создан в режиме 'x'.\n")
# except FileExistsError:
#     print("Файл уже существует.")
#


with (open("example.txt", "r", encoding="utf-8") as infile,
      open("output.txt", "w", encoding="utf-8") as outfile):
    for line in infile:
        outfile.write(line.upper())  # Записываем в верхнем регистре
