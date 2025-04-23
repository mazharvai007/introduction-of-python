class Student:
    # Class attributes
    name = ""
    count: int = 0

    def __init__(self) -> None:
        self.count += 1


std1 = Student()
std1.name = "Tahsin"
print(std1)
print(std1.name)

std2 = Student()
std2.name = "Sahshin"
print(std2)
print(std2.name)

std3 = Student()


print(std1.count, std2.count, std3.count)


class Employee:
    # Class Attribute
    count = 0

    def __init__(self, name: str) -> None:
        # Object Attribute
        self.name = name
        print("-------------------")
        print(self.count)
        self.count = (
            self.count + 1
        )  # 1,2,3,4 <---- expected | Actual count creates as an object attribute
        print(self.count)
        print("-------------------")


e1 = Employee("Rafiq")
print(e1.name, e1.count)
print("-------------------")
e2 = Employee("Jamal")
print(e2.name, e2.count)
print("-------------------")
e3 = Employee("Ashik")
print(e3.name, e3.count)
print("-------------------")
e4 = Employee("Jashim")
print(e4.name, e4.count)
print("-------------------")

# print(e1.count, e2.count, e3.count, e4.count)  # 1 1 1 1


class Employee_One:
    count = 0

    def __init__(self, name) -> None:
        self.name = name
        Employee_One.count = Employee_One.count + 1


e1 = Employee_One("Rafiq")
print(e1.name, e1.count)
e2 = Employee_One("Jamal")
print(e2.name, e2.count)
e3 = Employee_One("Ashik")
print(e3.name, e3.count)
e4 = Employee_One("Jashim")
print(e4.name, e4.count)

# print(e1.count, e2.count, e3.count, e4.count)  # 4 4 4 4


# Methods (Object and class)
class Our_Employee:
    count = 0

    def __init__(self, name, salary, experience) -> None:
        self.name = name
        self.salary = salary
        self.experience = experience

        Our_Employee.count += 1

    # Object Method
    def get_designation(self):
        if self.experience <= 0:
            return "Freasher"
        elif self.experience <= 2:
            return "Junior Software Engineer"
        elif self.experience > 2 and self.experience <= 5:
            return "Mid Senior Software Engineer"
        else:
            return "Senior Software Engineer"

    # Class method - decorator
    # def total_employee():
    #     return Our_Employee.count

    @classmethod
    def total_employee(cls):
        return cls.count


e1 = Our_Employee(name="Jamal", salary=50000, experience=5)
e2 = Our_Employee(name="Hadi", salary=100000, experience=8)

print(Our_Employee.total_employee())
