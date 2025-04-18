# Animal
class Animal:
    # Constructor
    def __init__(self, name):
        self.name = name

    def speek(self):
        pass


class Dog(Animal):
    def speek(self):
        return f"{self.name} says - Ghew Ghew Ghew"


dog1 = Dog("Buddy")
print(dog1.speek())
