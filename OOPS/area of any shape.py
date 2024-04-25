import math

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def __init__(self, name, side_length):
        super().__init__(name, side_length, side_length)

# Main program
circle = Circle("Circle", 5)
rectangle = Rectangle("Rectangle", 4, 6)
square = Square("Square", 3)

shapes = [circle, rectangle, square]

for shape in shapes:
    print(f"\nShape: {shape.name}")
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
