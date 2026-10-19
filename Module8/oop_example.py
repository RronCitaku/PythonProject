class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return  2 * (self.width + self.height)

my_rectangle = Rectangle(2,5)

area = my_rectangle.calculate_area()
perimeter = my_rectangle.calculate_perimeter()
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")