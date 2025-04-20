from software_developer import Software_Developer


# Child class of Base class
class Junior(Software_Developer):
    pass


junior_obj = Junior("Kamal", age=24, exp_level=2)
print(junior_obj.salary_calculation())
print(junior_obj.employee_info())
