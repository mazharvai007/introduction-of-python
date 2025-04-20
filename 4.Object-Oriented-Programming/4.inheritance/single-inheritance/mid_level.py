from software_developer import Software_Developer


# Child class of Base class
class Mid_Level(Software_Developer):
    pass


mid_level_obj = Mid_Level("Shoshi", age=26, exp_level=3)

print(mid_level_obj.salary_calculation())
print(mid_level_obj.employee_info())
