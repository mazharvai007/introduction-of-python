class Intern:
    def __init__(self, exp_level) -> None:
        self.exp_level = exp_level

    def calculation_salary(self):
        base_salary = 10000
        actual_salary = base_salary * self.exp
        return actual_salary


class Junior:
    def __init__(self, exp_level) -> None:
        self.exp_level = exp_level

    def calculation_salary(self):
        base_salary = 10000
        actual_salary = base_salary * self.exp
        return actual_salary


class Mid_level:
    def __init__(self, exp_level) -> None:
        self.exp_level = exp_level

    def calculation_salary(self):
        base_salary = 10000
        actual_salary = base_salary * self.exp
        return actual_salary


class Senior:
    def __init__(self, exp_level) -> None:
        self.exp_level = exp_level

    def calculation_salary(self):
        base_salary = 10000
        actual_salary = base_salary * self.exp
        return actual_salary


intern_obj = Intern(exp_level=1)
junior_obj = Junior(exp_level=2)
mid_level_obj = Mid_level(exp_level=3)
senior_obj = Senior(exp_level=4)
