# Scenerio


# def greet(name: str) -> str:
#     if not isinstance(name, str):
#         raise ValueError("Name must be a string")
#     return "Hello " + name


# greet(name="Python")
# greet(name=20)

"""
Pydantic is a class with validate data
"""

from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int


# Usages
# p1 = Person(name="Kamal", age=25)
# print(p1)
# print(p1.name)
# print(p1.age)
# print(p1.model_dump())

# p1_dict = {"name": "Rafiq", "age": 30, "email": "abc@gmail.com"}

# # **p1_dict -> name = "Rafiq" # usesonly in keyword argument

# my_validation = Person(**p1_dict)
# print(my_validation.model_dump())


def greet(person: Person) -> str:
    return "Hello ", person.name, ". Your age is ", person.age


p1_dict = {"name": "Rafiq", "age": 30, "email": "abc@gmail.com"}

person = Person(**p1_dict)
print(greet(person=person))
