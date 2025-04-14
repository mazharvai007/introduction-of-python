from datetime import datetime


class Person:
    """
    In real life scenario: an object has two types of feature. 1. Static Feature 2. Dynamic Feature.\n
    But, in programming, an object has two types of features. 1. Attributes 2. Methods
    1. Attributes are like static feature
    2. Methods are like dynamic feature
    """

    # Constructor/Initializer - is very important for every class
    def __init__(self, first_name, last_name, email) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.join = datetime.now()

    # Dunder (Double underscore) / Magic method
    def __str__(self):
        return f"He is {self.first_name} {self.last_name}. His email is {self.email}. He joined out company as {self.join}"


nahid_obj = Person(first_name="Nahid", last_name="Islam", email="nahid@islam.com")
salman_obj = Person(first_name="Salman", last_name="Khan", email="salman@khan.com")

print(nahid_obj)
print(salman_obj)

print("-----------------------")

# First Name
print(nahid_obj.first_name)
print(salman_obj.first_name)

print("-----------------------")

# Last name
print(nahid_obj.last_name)
print(salman_obj.last_name)

print("-----------------------")

# Join Date
print(nahid_obj.join)
print(salman_obj.join)

print("-----------------------")

print(dir(nahid_obj))

print("-----------------------")

print(dir(salman_obj))

print("-----------------------")

print(nahid_obj.__dict__)
print("-----------------------")
print(salman_obj.__dict__)
