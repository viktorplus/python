"""Python Fundamentals 2025: Домашнее задание 34
Класс Rectangle

Создайте класс Rectangle, который описывает прямоугольник.
У каждого объекта должны быть два поля: width и height.
Добавьте метод get_area(), который возвращает площадь прямоугольника.
Создайте объект прямоугольника с произвольными значениями.
Выведите его площадь.
Измените ширину и высоту.
Выведите новую площадь.

"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

r = Rectangle(4, 5)
print("Площадь:", r.get_area())

r.width = 5
r.height = 7
print("Новая площадь:", r.get_area())

"""
Класс Counter
Реализуйте класс Counter, который представляет собой простой счётчик.
Счётчик должен начинаться с нуля.
Предусмотрите методы для увеличения и уменьшения значения на единицу, при этом при каждой операции должно отображаться новое значение счётчика.
Добавьте метод, возвращающий текущий результат.
Проверьте работу счётчика, выполнив несколько операций.

"""

class Counter:
    def __init__(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1
        print(f"Значение увеличено, текущее: {self.value}")

    def decrement(self):
        self.value -= 1
        print(f"Значение уменьшено, текущее: {self.value}")

    def get(self):
        return self.value

c = Counter()
print(f"Текущее значение: {c.get()}")
c.increment()
c.increment()
c.increment()
c.decrement()
print(f"Текущее значение: {c.get()}")