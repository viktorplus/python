import pymysql

config = {
    'host': 'ich-db.edu.itcareerhub.de',
    'user': 'ich1',
    'password': 'password',
    'database': 'sakila',
}

with pymysql.connect(**config) as connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM film WHERE title LIKE %s", ("%LION%",))
        films = cursor.fetchall()

        for film in films:
            print(film)

        print("Количество:", len(films))