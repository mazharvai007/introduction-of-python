class Calculator:
    """Do addition, subtraction, multiplication, and division."""

    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return "It is impossible to divide by zero."


class Super_Calculator(Calculator):
    """Child class of Calculator. Do square and cube."""

    def square(self):
        return self.a**2

    def cube(self):
        return self.b**3


my_calculator = Super_Calculator(20, 15)

calc = my_calculator.addition()
print(calc)

calc = my_calculator.subtraction()
print(calc)

calc = my_calculator.multiplication()
print(calc)

calc = my_calculator.division()
print(calc)

calc = my_calculator.square()
print(calc)

calc = my_calculator.cube()
print(calc)


class Custom_Error(Exception):
    """Just for example."""

    def __init__(self, message) -> None:
        self.message = message


try:
    raise Custom_Error("This is a custom error")
except Custom_Error as error:
    print(error)
