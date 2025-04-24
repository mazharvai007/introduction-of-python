# Inheritance
from datetime import datetime


# Parent class / Base class / Super class
class User:
    def __init__(self, email) -> None:
        self.email = email
        self.joined_at = datetime.now()

    def joined(self):
        return self.joined_at.strftime("%d-%m-%y")


# Child class / Derived class
class UserBio(User):
    def __init__(self, email, profile_image, bio) -> None:
        super().__init__(
            email=email
        )  # Super constructor which is inherit from User class
        self.profile_image = profile_image
        self.bio = bio

    def intro(self):
        return f"He is the member of MiabsLab and {self.bio}"


class Employee(User):
    def __init__(self, email, salary) -> None:
        super().__init__(email)
        self.salary = salary


# user1 = User("user1@gmail.com")
# print(user1.email)
# print(user1.joined())

# user1_bio = UserBio(
#     email="userbio@gmail.com", profile_image="u1.jpg", bio="A simple engineer"
# )
# print(
#     user1_bio.email,
#     user1_bio.bio,
#     user1_bio.profile_image,
#     user1_bio.joined(),
#     user1_bio.joined_at,
# )

# print(user1_bio.intro())

employee1 = Employee("john@gmail.com", salary=50000)
print(employee1.email, employee1.salary)
