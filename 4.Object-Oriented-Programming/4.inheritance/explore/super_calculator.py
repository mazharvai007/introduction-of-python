class SuperCalculator:
    """Do addition, subtraction, multiplication, division, square, and cube."""

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

    def square(self):
        return self.a**2

    def cube(self):
        return self.b**3


my_calculator = SuperCalculator(45, 12)

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
