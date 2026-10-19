from abc import ABC, abstractmethod

from Module9.polymorphism.inheritance_polymorphism import circle


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

circle_1 = Circle(7)
square_1 = Square(10)

print(circle_1.area())
print(square_1.area())