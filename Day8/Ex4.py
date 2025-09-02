import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area method")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter method")

    def __repr__(self):
        return "Shape()"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __repr__(self):
        return f"Circle(radius={self.radius})"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

circle = Circle(5)
rectangle = Rectangle(4, 6)

print(circle)
print(f"Circle area: {circle.area():.2f}")
print(f"Circle perimeter: {circle.perimeter():.2f}\n")

print(rectangle)
print(f"Rectangle area: {rectangle.area():.2f}")
print(f"Rectangle perimeter: {rectangle.perimeter():.2f}")
