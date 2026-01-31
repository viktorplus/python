# import os
#
# # Объединение нескольких компонентов
# current_dir = os.getcwd()
# print(current_dir)
# sub_dir = "docs"
# file_name = "data.txt"
# full_path = os.path.join(current_dir, sub_dir, file_name)
# print(f"Путь: {full_path}")

import sqlite3
import pandas as pd

# Подключение к SQLite (файл будет создан в текущей рабочей папке, если его нет)
conn = sqlite3.connect("weather.db")

data = {
    "date": ["2026-01-01","2026-01-02","2026-01-03","2026-01-04","2026-01-05","2026-01-06","2026-01-07"],
    "temp_day":   [1, 0, 5, 8, 0, 2, 4],
    "temp_night": [0,-1, 2, 3,-1, 0, 1],
    "daylight_h": [7.5, 7.4, 7.3, 7.2, 7.1, 7.0, 6.9],
    "wind":       [0, 1.5, 2.1, 2, 0.5, 1.2, 3.0],
    "humidity":   [55, 60, 65, 54, 50, 70, 58],
    "pressure":   [1001, 1002, 1003, 1000, 1005, 1004, 1002],
}

df = pd.DataFrame(data)

# Запись данных в таблицу
df.to_sql("myweather", conn, if_exists="replace", index=False)

# 1) Все данные
print("1) Все данные:")
print(pd.read_sql_query('SELECT * FROM myweather;', conn), end="\n\n")

# 2) Данные за последние 3 дня относительно MAX(date)
print("2) Последние 3 дня (от MAX(date)):")
print(pd.read_sql_query("""
SELECT *
FROM myweather
WHERE "date" >= date((SELECT MAX("date") FROM myweather), '-2 day')
ORDER BY "date" DESC;
""", conn), end="\n\n")

# 3) Средняя температура ночью
print("3) Средняя температура ночью:")
print(pd.read_sql_query("""
SELECT AVG(temp_night) AS avg_temp_night
FROM myweather;
""", conn), end="\n\n")

# 4) День(дни) с максимальной влажностью (если ничья — вернёт несколько строк)
print("4) День(дни) с максимальной влажностью:")
print(pd.read_sql_query("""
SELECT "date", humidity
FROM myweather
WHERE humidity = (SELECT MAX(humidity) FROM myweather);
""", conn), end="\n\n")

# 5) Один день с максимальной влажностью (ровно 1 строка)
print("5) Один день с максимальной влажностью (TOP 1):")
print(pd.read_sql_query("""
SELECT "date", humidity
FROM myweather
ORDER BY humidity DESC
LIMIT 1;
""", conn), end="\n\n")

conn.close()
