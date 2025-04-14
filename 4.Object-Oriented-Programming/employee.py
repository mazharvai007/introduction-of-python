from datetime import datetime


class Employee:
    """
    This is employee class where we will get all information of an employee
    """

    # Constructor/Initializer - is very important for every class
    def __init__(self, name: str, age: int, salary: int) -> None:
        # Arributes
        self.name = name
        self.age = age
        self.salary = salary

    # Year of Birth method
    def get_year_of_birth(self):
        """
        User input his/her age (ex. 35)\n
        This method will return his/her birth of year
        """
        # current_year - self.age =? year
        current_year = datetime.now().year
        return current_year - self.age  # return year of birth


employee1 = Employee(name="Sakib", age=35, salary=30000)

# print(employee1)
# print(employee1.name)
# print(employee1.age)
# print(employee1.salary)

# print(date.today())

print(employee1.get_year_of_birth())

""" 
Home Work:

Take user's birthdate as this format (dd-mm-yyyy), otherwise give error
- get_current_age() method
- return current_age
    string: "20years 20days"
"""
