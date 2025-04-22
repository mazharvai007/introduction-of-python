class Calculator:
    """This is Base/Parent Class. It will do addition, subtraction, multiplication, and division."""

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "It is impossible to divide by zero."


class Super_Calculator(Calculator):
    """This is a child class of Calculator (parent/base) class. We will override few methods"""

    def addition(self, a, b, c):
        return a + b + c

    def square(self, a):
        return a**2

    def cube(self, b):
        return b**3


my_calculator = Super_Calculator()

calc = my_calculator.addition(10, 20, 30)
print(calc)

calc = my_calculator.square(10)
print(calc)

calc = my_calculator.cube(20)
print(calc)
