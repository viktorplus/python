"""Python Fundamentals 2025: Домашнее задание 42

Создание базы
Напишите программу, которая:
создаёт базу данных notes_app_<your_group>_<your_full_name>
выбирает эту базу через USE notes_app
выводит сообщение о результате"""

import pymysql

config = {
    'host': 'ich-edit.edu.itcareerhub.de',
    'user': 'ich1',
    'password': 'ich1_password_ilovedbs',
}

db_name = "notes_app"

with pymysql.connect(**config) as connection:
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        cursor.execute("SHOW DATABASES")
        dbs = [row[0] for row in cursor]
        if db_name in dbs:
            print(f"Database '{db_name}' created or already exists.")

        cursor.execute(f"USE {db_name}")

"""Добавление заметок
Продолжите предыдущую программу:
создайте таблицу notes с полями: id, title, content
вставьте одну заметку в таблицу
выполните commit() после вставки
выведите все заметки используя DictCursor"""

from pymysql.cursors import DictCursor

with pymysql.connect(**config, cursorclass=DictCursor) as connection:
    with connection.cursor() as cursor:
        cursor.execute(f"USE {db_name}")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                content TEXT
            )
        """)

        title = "Shopping list"
        content = "Eggs, milk, bread"

        cursor.execute(
            "INSERT INTO notes (title, content) VALUES (%s, %s)",
            (title, content)
        )
        connection.commit()

        # Вывод всех заметок
        cursor.execute("SELECT id, title, content FROM notes")
        notes = cursor.fetchall()

        print("\nAll notes:")
        for note in notes:
            print(f"{note['id']}. {note['title']} — {note['content']}")