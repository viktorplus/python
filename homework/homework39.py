"""Python Fundamentals 2025: Домашнее задание 39

Фигуры и площади
Создайте абстрактный класс Shape.
В классе должен быть метод area(), который возвращает площадь фигуры.
Реализуйте два класса:
Circle, который принимает радиус.
Rectangle, который принимает ширину и высоту.

# Пример использования
shapes = [Circle(3), Rectangle(4, 5)]
for shape in shapes:
    print(f"Area: {shape.area():.2f}")"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Пример использования
shapes = [Circle(3), Rectangle(4, 5)]
for shape in shapes:
    print(f"Area {shape.__class__.__name__}: {shape.area():.2f}")


"""Проверка размеров фигур
Доработайте фигуры:
Добавьте проверку в конструкторы Circle и Rectangle, чтобы значения были положительными.
Если передано отрицательное или нулевое значение, выбрасывайте пользовательское исключение InvalidSizeError."""


from abc import ABC, abstractmethod
import math

class InvalidSizeError(ValueError):
    """Raised when shape dimensions are invalid."""
    pass

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise InvalidSizeError("Radius must be positive.")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise InvalidSizeError("Width and height must be positive.")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

c = Circle(3)
print(f"Area: {c.area():.2f}")
try:
    Rectangle(4, -5)
except InvalidSizeError as e:
    print("Error:", e)


# extra
from abc import ABC, abstractmethod
import math

class InvalidSizeError(ValueError):
    """Raised when shape dimensions are invalid."""
    pass

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise InvalidSizeError("Radius must be positive.")
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise InvalidSizeError("Width and height must be positive.")
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

c = Circle(3)
print(f"Area: {c.area:.2f}")
try:
    Rectangle(4, -5)
except InvalidSizeError as e:
    print("Error:", e)

    
