"""
Python program to show use of + operator for different purpose
"""

print(1 + 2)

# Concatenate two string
print("I" + "am" + "Learning" + "Python")

# Multiply two numbers
print(2 * 3)

# Repeating the string
print("Python" * 4)


# How does operator overloading actually work?


# Example 1
class A:
    def __init__(self, a) -> None:
        self.a = a

    # Adding two objects
    def __add__(self, other):
        return self.a + other.a


ob1 = A(1)
ob2 = A(2)
ob3 = A("Learning")
ob4 = A("Python")

print(ob1 + ob2)
print(ob3 + ob4)

# Actual working when binary operator is used
print(A.__add__(ob1, ob2))
print(A.__add__(ob3, ob4))

# And can also be understand as:
print(ob1.__add__(ob2))
print(ob3.__add__(ob4))


# Example 2
class Complex:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    # Adding two objects
    def __add__(self, other):
        return self.a + other.a, self.b + other.b


complex_obj1 = Complex(3, 4)
complex_obj2 = Complex(5, 6)
add_objects = complex_obj1 + complex_obj2
print(add_objects)


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        # print(self.x, self.y)  # 1 2
        # print("---------------")
        # print(other.x, other.y)  # 3 4
        # print("---------------")
        # print(self.x, other.x)  # 1 3
        # print("---------------")
        # print(self.y, other.y)  # 2 4
        # print("---------------")

        return self.x + other.x, self.y + other.y  # 4 6


p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2

print(p3)  # tuple (4 6)
