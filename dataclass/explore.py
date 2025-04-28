from dataclasses import dataclass


@dataclass
class Person:
    name: str


p1 = Person(name="Rajon")
print(p1)
