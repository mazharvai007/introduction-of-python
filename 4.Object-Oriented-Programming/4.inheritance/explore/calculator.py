# class Calculator:
#     """Do addition, subtraction, multiplication, and division."""

#     def addition(sef, a, b):
#         return a + b

#     def subtraction(self, a, b):
#         return a - b

#     def multiplication(self, a, b):
#         return a * b

#     def division(self, a, b):
#         try:
#             return a / b
#         except ZeroDivisionError:
#             return "It is impossible to divide by zero."


# my_calculator = Calculator()

# temp = my_calculator.addition(12, 78)
# print(temp)

# temp = my_calculator.subtraction(78, 12)
# print(temp)

# temp = my_calculator.multiplication(78, 12)
# print(temp)

# temp = my_calculator.division(78, 12)
# print(temp)

# temp = my_calculator.division(78, 0)
# print(temp)


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


my_calculator = Calculator(83, 20)

temp = my_calculator.addition()
print(temp)

temp = my_calculator.subtraction()
print(temp)

temp = my_calculator.multiplication()
print(temp)

temp = my_calculator.division()
print(temp)

temp = my_calculator.division()
print(temp)
