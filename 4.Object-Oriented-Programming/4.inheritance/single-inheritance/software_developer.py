class Software_Developer:
    """
    This is a Base Class of Single Inheritance

    What is Single Inheritance?\n
    - A child class inherits from one parent class (One base class and one child/derived class)
    """

    def __init__(self, name: str, age: int, exp_level: int) -> None:
        self.name = name
        self.age = age
        self.exp_level = exp_level

    def salary_calculation(self):
        base_salary = 10000
        actual_salary = base_salary * self.exp_level
        return actual_salary

    def employee_info(self):
        return f"My name is {self.name}. I am {self.age} years old. I have {f"{self.exp_level} year" if self.exp_level == 1 else f"{self.exp_level} years"} experience of Python/Django development."
