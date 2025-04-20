"""
Method Overriding - in inheritance refers to the ability of a subclass to provide a specific implementation of a method that is already defined in its superclass
"""


class Shape:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

        print(self.length, self.width)

    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width) -> None:

        self.length = length
        self.width = width
        print(f"Rectangle Override: {self.length, self.width}")

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius

        print(f"Circle Override: {self.radius}")

    def area(self):
        return self.radius**2 * 3.1416


class Triangle(Shape):
    def __init__(self, length, width, height) -> None:
        super().__init__(
            length, width
        )  # Using super() for getting access Parent Class constructor (__init__) method
        self.height = height

        print(f"Override Parent Constructor Method {self.length, self.width}")

    def area(self):
        return self.length * self.width * self.height


rect_obj = Rectangle(10, 5)
print(rect_obj.area())

circle_obj = Circle(20)
print(circle_obj.area())

triangle_obj = Triangle(15, 15, 15)
print(triangle_obj.area())
