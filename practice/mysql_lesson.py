import pymysql  # подключаем библиотеку для работы с MySQL

# config = {
#     'host': 'ich-db.edu.itcareerhub.de',
#     'user': 'ich1',
#     'password': 'password',
#     'database': 'hr'
# }
#
# connection = pymysql.connect(**config)  # распаковка словаря как аргументы
#
# if connection.open:
#     print("Connection successful!")
#
# cursor = connection.cursor()
# cursor.execute("select * from employees")
# for row in cursor:
#     print(row)
#
#
#
# cursor.close()
# connection.close()


with pymysql.connect(  # открываем соединение с базой данных
    host='ich-db.edu.itcareerhub.de',  # адрес сервера БД
    user='ich1',  # имя пользователя
    password='password',  # пароль
    database='hr'  # имя базы данных
) as connection:  # connection закроется автоматически после выхода из блока with
    with connection.cursor() as cursor:  # создаём курсор для выполнения SQL-запросов
        cursor.execute("SELECT department_name FROM departments")  # выполняем SQL-запрос
        for num, name in enumerate(cursor, 1):  # перебираем все строки результата
            print(f"P{num}. {name[0]}")  # выводим каждую строку

    with connection.cursor() as cursor:
        print(f"{num}. {name[0]}")
        name = input("Enter department name: ")
        cursor.execute(
            query="""
                SELECT e.first_name, e.last_name, j.job_title
                FROM employees as e
                JOIN departments as d
                    ON e.department_id = d.department_id
                JOIN jobs as j
                    ON e.job_id = j.job_id
                WHERE department_name = %s
            """,
            args=(name,)
        )
        for num, (f_name, l_name, job_name) in enumerate(cursor):
            print(f"{name}: {f_name} {l_name} - {job_name}")