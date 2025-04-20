from software_developer import Software_Developer

# Subclass inheriting from Software_Developer


class Intern(Software_Developer):
    pass  # Inherits all attributes and methods from Software_Developer


intern_obj = Intern(name="Jakir", employee_id=101, experience_level="Intern")

print(intern_obj.display_info())
print(f"Salary: {intern_obj.salary_calculation()}")
