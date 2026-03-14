# Создайте класс City, представляющий город с координатами.
# У каждого города есть поля name, latitude, longitude.
# Добавьте строковое представление объекта.
# Добавьте метод distance(city1, city2), который возвращает кортеж (latitude, longitude) между двумя городами.
# Проверьте расстояние между двумя городами.
# Пример вывода: 
# City: Berlin (52.52, 13.4)
# City: Paris (48.85, 2.35)
# Distance: 14.72
#
# Доработайте класс City.
# Добавьте метод from_string(data), который создаёт объект из строки вида "Rome:41.89,12.51".
# Проверьте создание нового объекта через этот метод и выведите его.
# Пример вывода: 
# City: Rome (41.89, 12.51)

class City:
    def __init__(self, name, latitude, longitute):
        self.name = name
        self.latitude = latitude
        self.longitute = longitute

    @classmethod
    def from_string(cls, string_data):
        name, other = string_data.split(':')
        latitude, longtitude = other.split(',')
        return cls(name=name, latitude=latitude, longitute=longtitude)

    @staticmethod
    def distance(city1, city2):
        return round(city1.latitude - city2.latitude, 6), round(city1.longitute - city2.longitute, 6)

    def __str__(self):
        return f"{self.name}: {self.latitude}, {self.longitute}"

city1 = City('Berlin', 52.52, 13.4)
city2 = City('Paris', 48.85, 2.35)



print(City.from_string("Rome:41.89,12.51"))



# Создайте класс Student, представляющий студента.
# У каждого объекта должно быть имя и дата рождения.
# Дата передаётся как строка (YYYY-MM-DD) и сохраняется в виде объекта datetime.date.
# Добавьте проверку возраста — студенту должно быть не менее 16 лет, иначе выбрасывается ValueError.


# Каждому студенту должен автоматически присваиваться уникальный номер - student_id, начиная с 1.
#
# Добавьте строковое представление объекта.
# Пример вывода:
# Student: Alice, birth_date: 2005-05-10, ID: 1

#
# from datetime import date, datetime
#
#
# class Student:
#     def __init__(self, student_name, birthday):
#         birthday_date = datetime.strptime(birthday, "%Y-%m-%d").date()
#         age = Student.calculate_age(birthday_date)
#         Student.validate_age(age)
#         self.name = student_name
#         self.birthday = birthday_date
#
#
#     @staticmethod
#     def calculate_age(birthday):
#         today = datetime.now()
#         age = today.year - birthday.year
#         if (birthday.month, birthday.day) < (today.month, today.day):
#             age -= 1
#         return age
#
#
#     @staticmethod
#     def validate_age(age):
#         if age < 16:
#             raise ValueError("Возраст должен быть не менее 16 лет")
#
#
#
# student1 = Student("Nina", "2000-02-12")
# # print(student1.calculate_age("2013-02-12"))
# print(student1.name)