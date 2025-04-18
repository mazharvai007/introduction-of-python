class Student:
    # constructor/initialization (init) is essential for a class
    def __init__(self, name: str, id: int) -> None:
        self.name = name
        self.id = id

    def info(self):
        return self.name, self.id


std1 = Student(name="Tahsin", id=101)
print(std1)
print(std1.name)
print(std1.id)
print(std1.info())

std2 = Student(name="Sahsin", id=102)
print(std2)
print(std2.name)
print(std2.id)
print(std2.info())
