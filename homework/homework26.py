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

#!/usr/bin/env python3
# script.py

import argparse
from pathlib import Path


def list_dir_contents(dir_path: Path) -> None:
    """Показывает содержимое директории: отдельно папки и отдельно файлы (без рекурсии)."""
    if not dir_path.exists():
        raise FileNotFoundError(f"Директория не найдена: {dir_path}")
    if not dir_path.is_dir():
        raise NotADirectoryError(f"Это не директория: {dir_path}")

    folders = []
    files = []

    for entry in dir_path.iterdir():
        if entry.is_dir():
            folders.append(entry.name)
        elif entry.is_file():
            files.append(entry.name)

    folders.sort(key=str.lower)
    files.sort(key=str.lower)

    print(f"Содержимое директории '{dir_path}':")

    print("Папки:")
    if folders:
        for name in folders:
            print(f"- {name}")
    else:
        print("(нет)")

    print("\nФайлы:")
    if files:
        for name in files:
            print(f"- {name}")
    else:
        print("(нет)")


def normalize_ext(ext: str) -> str:
    """Нормализует расширение: 'log' -> '.log', '.LOG' -> '.log'."""
    ext = ext.strip()
    if not ext:
        raise ValueError("Расширение пустое.")
    if not ext.startswith("."):
        ext = "." + ext
    return ext.lower()


def find_files_by_extension(dir_path: Path, ext: str) -> list[Path]:
    """Рекурсивно ищет файлы по расширению (case-insensitive)."""
    if not dir_path.exists():
        raise FileNotFoundError(f"Директория не найдена: {dir_path}")
    if not dir_path.is_dir():
        raise NotADirectoryError(f"Это не директория: {dir_path}")

    ext = normalize_ext(ext)
    found: list[Path] = []

    for p in dir_path.rglob("*"):
        if p.is_file() and p.suffix.lower() == ext:
            found.append(p)

    found.sort(key=lambda x: str(x).lower())
    return found


def ask_yes_no(prompt: str) -> bool:
    """Да/нет вопрос. Принимает: y/yes/д/да, n/no/н/нет."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in {"y", "yes", "д", "да"}:
            return True
        if answer in {"n", "no", "н", "нет"}:
            return False
        print("Введите 'y/yes/да' или 'n/no/нет'.")


def delete_files(files: list[Path], base_dir: Path) -> None:
    """Удаляет файлы, печатает результат. Пути выводит относительно base_dir."""
    deleted = 0
    failed = 0

    for f in files:
        rel = f.relative_to(base_dir)
        try:
            f.unlink()
            print(f"Удалён: {rel}")
            deleted += 1
        except Exception as e:
            print(f"НЕ удалён: {rel} ({e})")
            failed += 1

    print(f"\nИтог: удалено {deleted}, ошибок {failed}.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Список папок/файлов или поиск и удаление файлов по расширению."
    )
    parser.add_argument("path", help="Путь к директории")
    parser.add_argument(
        "extension",
        nargs="?",
        help="Расширение для поиска (например .log или log). Если не указано — просто листинг.",
    )

    args = parser.parse_args()
    dir_path = Path(args.path).expanduser().resolve()

    if args.extension is None:
        list_dir_contents(dir_path)
        return

    ext = normalize_ext(args.extension)
    files = find_files_by_extension(dir_path, ext)

    if not files:
        print(f"Файлы с расширением '{ext}' не найдены в '{dir_path}'.")
        return

    print(f"Найдены файлы с расширением '{ext}':")
    for f in files:
        print(f"- {f.relative_to(dir_path)}")

    if ask_yes_no("\nУдалить найденные файлы? (y/n): "):
        delete_files(files, dir_path)
    else:
        print("Удаление отменено.")


if __name__ == "__main__":
    main()
