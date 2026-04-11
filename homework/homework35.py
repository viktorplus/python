"""Python Fundamentals 2025: Домашнее задание 35

Счётчик экземпляров
Создайте класс User, представляющий пользователя.
При создании должны указываться логин (username) и пароль (password).
У класса должно быть поле total_users, хранящее общее количество созданных пользователей.
При каждом создании нового объекта User, счётчик должен увеличиваться.
Добавьте метод get_total(), возвращающий количество пользователей.
Проверьте, что счётчик работает.
"""
class User:
    total_users = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password
        User.total_users += 1

    @classmethod
    def get_total(cls):
        return cls.total_users

u1 = User("alice", "secret")
u2 = User("bob", "qwe")
u2 = User("bob", "pass")

print(f"Total users: {User.get_total()}")
"""
Проверка данных пользователя
Доработайте класс User.
Добавьте валидации полей при создании.
Имя должно быть непустой строкой.
Пароль должен быть строкой длиной не менее 5 символов.
Если данные некорректны — выбрасывайте ValueError.
Добавьте строковое представление объекта.
Проверьте работу класса с разными значениями.
"""

class User:
    total_users = 0

    def __init__(self, username, password):
        self.validate_username(username)
        self.validate_password(password)
        self.username = username
        self.password = password
        User.total_users += 1

    @classmethod
    def get_total(cls):
        return cls.total_users

    @staticmethod
    def validate_username(value):
        if not (isinstance(value, str) and len(value.strip()) > 0):
            raise ValueError(f"Invalid username: '{value}'.")

    @staticmethod
    def validate_password(value):
        if not (isinstance(value, str) and len(value) >= 5):
            raise ValueError(f"Invalid password: '{value}'.")


    def __str__(self):
        return f"User: {self.username}"


user1 = User("alice", "secret")
print(user1)
try:
    user2 = User("bob", "qwe")  # вызовет ошибку
except ValueError as e:
    print(e)

print(f"Total users: {User.get_total()}")