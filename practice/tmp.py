# Сегодня
#
# Teacher 14 9:10
# pip install mysql-connector-python
# Сообщения, адресованные в "Групповой чат конференции", также будут отображаться в групповом чате конференции в рамках коллективного чата
#
# Dmytro Klymov 9:36
# скинь пожалуйста файл
#
# Teacher 14 10:00
# Выведите фильмы, в названии которых содержится слово “LION”, посчитайте количество таких фильмов.
# Выведите названия всех фильмов в категории “Horror”. (Подсказка: join таблиц film и film_category и фильтр по category_id)
# Выведите названия фильмов с названием категории.
# Выведите 10 самых длинных фильмов. 
# Выведите количество фильмов по категориям.
# Выведите категории, в которых больше 20 фильмов.
# Выведите названия фильмов, названия категорий и среднюю продолжительность фильма в каждой категории. Используйте оконные функции. 
# Измените предыдущий запрос так, чтобы помимо названия фильма и категории, выводился также ранг по длине фильма.
#
# David Narkevych 10:27
# index
#
# Viktoriia 10:29
import mysql

with mysql.connector.connect(**config) as connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM film WHERE title LIKE '%LION%'")
        for film in cursor.fetchall():
            print(film)

        cursor.execute("SELECT count(*) FROM film WHERE title LIKE '%LION%'")
        print(cursor.fetchone()[0])
