class Employee:
    """
    This is a base class of company structure
    """

    def __init__(self, name: str, employee_id: int) -> None:
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        """
        It will display the employee information
        """
        return f"The name of Employee is {self.name}, and the id is {self.employee_id}"
