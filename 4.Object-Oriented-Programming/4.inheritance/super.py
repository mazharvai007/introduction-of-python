"""
Super()

Definition:
- Accessing Parent Class
- It ensures that you are  accessing the next class in the method resolution order (MRO)
- This helps in maintaining a consistent and predictable behavior in your code.

"""


class Parent:
    def __init__(self, name) -> None:
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}"


class Child(Parent):
    def __init__(self, name, age) -> None:
        super().__init__(name)  # Calling parents constructor (__init__) method
        self.age = age

    def greet(self):
        parent_greeting = super().greet()  # Calling parents greet method
        return f"{parent_greeting} and I am {self.age} years old"


# Example uses
child_obj = Child("John", 30)
print(child_obj.greet())


# Assignment for Super
# How to utilize super() without inheritance? If possible to utilize how to do?
# How to work super() with Multiple Inheritance?
