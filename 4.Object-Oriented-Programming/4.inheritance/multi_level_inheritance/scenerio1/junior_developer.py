from software_developer import Software_Developer

# Subclass inheriting from Software_Developer


class Junior_Developer(Software_Developer):
    pass  # Inherits all attributes and methods from Software_Developer


junior_obj = Junior_Developer(
    name="Kamal", employee_id=102, experience_level="Junior Developer"
)
print(junior_obj.display_info())
print(f"Salary: {junior_obj.salary_calculation()}")
