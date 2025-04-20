from software_developer import Software_Developer

# Single Inheritance


# Child class of Base class
class Intern(Software_Developer):
    pass


intern_obj = Intern(name="Nishan", age=22, exp_level=1)

print(intern_obj.employee_info())
print(intern_obj.salary_calculation())
