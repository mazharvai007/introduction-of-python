class Software_Developer:
    """
    This is a base class of Multi-level Inheritance

    What is Multi-level Inheritance?
    - A class derived from a class which is also derived from another class

    """

    # This is an essential method of the class and here we are receiving inputs from users
    def __init__(self, name: str, employee_id: int, experience_level: str) -> None:
        self.name = name
        self.employee_id = employee_id
        self.experience_level = experience_level

    # Display Info
    def display_info(self):
        """It is displaying information of an employee"""

        return f"Developer Name: {self.name}\nEmployee ID: {self.employee_id}\nExperience Level: {self.experience_level}"

    # Salary Calculation
    def salary_calculation(self):
        """We are calculating salary based on the employee experience level"""

        if self.experience_level == "Intern":
            return 20000  # Base salary for Interns
        elif self.experience_level == "Junior Developer":
            return 50000  # Base salary for Junior Developer
        elif self.experience_level == "Senior Developer":
            return 80000  # Base salary for Senior Developer
        elif self.experience_level == "Team Leader":
            return 120000  # Base salary for Team Leader
        else:
            return 0  # Default salary if experience level is unknown or invalid
