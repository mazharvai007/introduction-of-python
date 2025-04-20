from employee import Employee


class Manager(Employee):
    def display_department(self, department_name: str):
        """
        It will display the employee department where he is working.
        """

        return f"He is working on {department_name} department."


manager_obj = Manager(name="Shahin", employee_id=101)
print(manager_obj.display_info())
print(manager_obj.display_department(department_name="Manager"))
