# Polymorphism


class Employee:
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 4000


class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return 2000


def print_salary(employee: Employee):
    print(f"Salary: {employee.calculate_salary()}")


# Usages
full_time = FullTimeEmployee()
part_time = PartTimeEmployee()

print(full_time.calculate_salary())
print(part_time.calculate_salary())
