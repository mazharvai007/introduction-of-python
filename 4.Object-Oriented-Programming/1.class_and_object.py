"""
Class and Object:

- A class in programming is a blueprint or template for creating objects that share common attributes (data) and behaviors
- It serves as a blueprint for creating instances, or objects, which are individual instances or that class
"""


# Student
class Student:
    # Constructor/initialization method. It is essential for a class
    def __init__(self, name: str, id: int) -> None:
        self.name = name
        self.id = id

    def info(self):
        return self.name, self.id


std1 = Student(name="Tahsin", id=101)
print(std1.name)
std1.name = "Rafique"
print(std1.name)
print(std1.info())

std2 = Student(name="Sahsin", id=102)
print(std2.name)
std2.name = "Kader"
print(std2.name)
print(std2.info())
