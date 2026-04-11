import mysql.connector
import pandas as pd

# print(__name__)
config = {'host': 'ich-db.edu.itcareerhub.de',
          'user': 'ich1',
          'password': 'password',
          'database': 'sakila',
          # 'use_pure': True,
          }

#
# # with pymysql.connect(**config) as connection:
# with mysql.connector.connect(**config) as connection:
#     with connection.cursor() as cursor:
#     # with connection.cursor(dictionary=True) as cursor:
#         cursor.execute("SELECT * FROM country")
#         data = cursor.fetchmany(5)
#         # columns = [col[0] for col in cursor.description]
#         for country in data:
#             print(country)
#         cursor.fetchall()  # new
#
# with mysql.connector.connect(**config) as connection:
#     df = pd.read_sql("SELECT * FROM country", connection)
#     print(df.head())
#     print(df)


with mysql.connector.connect(**config) as connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM film WHERE title LIKE '%LION%'")
        for film in cursor.fetchall():
            print(film)

        cursor.execute("SELECT count(*) FROM film WHERE title LIKE '%LION%'")
        print(cursor.fetchone()[0])