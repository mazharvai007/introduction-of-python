# Person
class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name}, I'm {self.age} years old"


person1 = Person("Abdul Karim", 35)
person2 = Person("Abdur Rahim", 25)

print(person1.introduce())
print(person2.introduce())
