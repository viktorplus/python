"""Python Fundamentals 2025: Домашнее задание 41

Список всех стран
Используя базу данных world, выведи названия всех стран из таблицы country. Каждое название должно отображаться с новой строки и иметь номер."""

import pymysql

config = {'host': 'ich-db.edu.itcareerhub.de',
          'user': 'ich1',
          'password': 'password',
          'database': 'world',
          }

with pymysql.connect(**config) as connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT Name FROM country")
        countries = [row[0] for row in cursor]
        for i, name in enumerate(countries, start=1):
            print(f"{i}. {name}")


"""Города выбранной страны
Добавьте к предыдущей программе возможность выбора страны. Пользователь введёт название или номер из выведенного списка. Далее выведите все города этой страны и их численность населения, также с нумерацией.
"""

import pymysql

config = {'host': 'ich-db.edu.itcareerhub.de',
          'user': 'ich1',
          'password': 'password',
          'database': 'world',
          }

with pymysql.connect(**config) as connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT Name FROM country")
        countries = [row[0] for row in cursor]
        countries_dict = dict(enumerate(countries, start=1))
        print(countries_dict)
        for i, name in countries_dict.items():
            print(f"{i}. {name}")

        selected_country = input("Enter country or order number: ")
        if selected_country.isdigit():
            selected_country = countries_dict[int(selected_country)]
            print(f"Selected country is {selected_country}")

        cursor.execute("""
            SELECT city.Name, city.Population
            FROM city
            JOIN country ON city.CountryCode = country.Code
            WHERE country.Name = %s
        """, (selected_country,))

        results = cursor.fetchall()
        for i, (city_name, population) in enumerate(results, start=1):
            print(f"{i}. {city_name} — {population}")