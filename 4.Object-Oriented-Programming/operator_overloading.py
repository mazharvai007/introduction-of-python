# Operator Overloading
class Employee:

    def __init__(self, name, salary, experience) -> None:
        self.name = name
        self.salary = salary
        self.experience = experience

    # def __eq__(self, value: other) -> bool:
    #     return self.experience == other.experience

    def __add__(self, amount):
        self.amount = amount


e1 = Employee(name="Nahid", salary=20000, experience=2)
e2 = Employee(name="Salman", salary=50000, experience=8)
e3 = Employee(name="Imrul", salary=35000, experience=5)

# print(e1 == e2)
# print(e2 == e3)
# print(e1 == e3)

# e1 = 15000

# print(e1.salary)

"""If an object has attribute then set a default value fro that attribute"""


class Pet:
    def __init__(self, price) -> None:
        self.price = price


p1 = Pet(100000)
location = getattr(p1, "location", False)

if location is False:
    setattr(p1, "location", "Dhaka")

print(p1.location)

""" 
Self Study

- read property of getter and setter
- __hash__ mthod
"""
