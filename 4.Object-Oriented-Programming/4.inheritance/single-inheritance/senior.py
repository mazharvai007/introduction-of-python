from software_developer import Software_Developer


# Child class of Base class
class Senior(Software_Developer):
    pass


senior_obj = Senior("Jamal", age=28, exp_level=4)
print(senior_obj.salary_calculation())
print(senior_obj.employee_info())
