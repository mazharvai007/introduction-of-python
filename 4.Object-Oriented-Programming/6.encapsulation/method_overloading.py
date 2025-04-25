# Polymorphism - method overloading


class Employee:
    def __init__(self, salary) -> None:
        self.salary = salary

    def get_salary(self):
        return self.salary


class SalesMan(Employee):
    def __init__(self, salary, incentive) -> None:
        super().__init__(salary)
        self.incentive = incentive

    # Redefine method (method overloading)
    # def get_salary(self):
    #     return self.salary + self.incentive

    # Method overloading
    def get_salary(self):
        return super().get_salary() + self.incentive


e1 = Employee(salary=10000)
s1 = SalesMan(salary=8000, incentive=500)

print(e1.get_salary())
print(s1.get_salary())
