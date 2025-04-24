# Property method: We will take that methods those does not take any input from outside


class Our_Employee:
    count = 0

    def __init__(self, name, salary, experience) -> None:
        self.name = name
        self.salary = salary
        self.experience = experience

        Our_Employee.count += 1

    # Object Method
    def get_designation(self):
        if self.experience <= 0:
            return "Fresher"
        elif self.experience <= 2:
            return "Junior Software Engineer"
        elif self.experience > 2 and self.experience <= 5:
            return "Mid Senior Software Engineer"
        else:
            return "Senior Software Engineer"

    # Property
    @property
    def designation(self):
        if self.experience <= 0:
            return "Fresher"
        elif self.experience <= 2:
            return "Junior Software Engineer"
        elif self.experience > 2 and self.experience <= 5:
            return "Mid Senior Software Engineer"
        else:
            return "Senior Software Engineer"

    # Salary Increment
    def increment_salary(self, increment_amount):
        self.salary = self.salary + increment_amount


e0 = Our_Employee(name="Rahat", salary=15000, experience=1)
print(e0.get_designation())  # call the method
print(e0.designation)  # designation is a property

e0.increment_salary(increment_amount=1000)
print("--------------------------------")

e1 = Our_Employee(name="Jamal", salary=50000, experience=5)
print(e1.get_designation())  # call the method
print(e1.designation)  # designation is a property
e1.increment_salary(increment_amount=2000)
print("--------------------------------")

e2 = Our_Employee(name="Hadi", salary=100000, experience=8)
print(e2.get_designation())  # call the method
print(e2.designation)  # designation is a property
e2.increment_salary(increment_amount=3000)
print("--------------------------------")

e3 = Our_Employee(name="Jony", salary=150000, experience=12)
print(e3.get_designation())  # call the method
print(e3.designation)  # designation is a property
e3.increment_salary(increment_amount=4000)
print("--------------------------------")

""" 
Self Study:

[*] read about property getter setter
"""
