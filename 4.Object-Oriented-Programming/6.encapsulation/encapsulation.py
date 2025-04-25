"""
Encapsulation --> Access modifier

Access Modifier:
- Public Attribute / Public Method
- Protected Attribute / Protected Method
- Private Attribute / Private Method
"""

# Base class / Parent class
from datetime import datetime


class User:
    def __init__(self, email) -> None:
        self.email = email

        # Private attribute
        self.__joined_at = datetime.now()

    # Protected method
    def _joined(self):
        return self.__joined_at.strftime("%d-%m-%y")


# Child class
class UserBio(User):
    def __init__(self, email, profile_image, bio) -> None:
        # Super constructor
        super().__init__(email)
        self.profile_image = profile_image
        self.bio = bio

    def intro(self):
        # print(self.__joined_at)  # do no access private attribute outside of the class directly
        return f"He is the member of MiabsLab and joined at {self._joined()}"


# ub1 = UserBio(
#     email="ub1@gmail.com", profile_image="ub1.png", bio="Junior Software Engineer"
# )
# print(ub1.intro())

# Access Modifier
u1 = User("u1@gmail.com")
print(u1._joined())  # Forbidden in OOP Philosophy (use of protected)
# print(u1.__joined_at)  # Use of private got error
print(
    u1._User__joined_at
)  # We can access private attributes outside of the class by this way
