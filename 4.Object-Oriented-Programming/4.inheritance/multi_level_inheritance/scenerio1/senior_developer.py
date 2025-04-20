from junior_developer import Junior_Developer


# Subclass inheriting from Junior_Developer
class Senior_Developer(Junior_Developer):
    pass  # Inherits all attributes and methods from Junior_Developer


senior_obj = Senior_Developer(
    name="Jashim", employee_id=103, experience_level="Senior Developer"
)
print(senior_obj.display_info())
print(f"Salary: {senior_obj.salary_calculation()}")
