# Get employee input from user
name = input("Enter Employee Name: ")
base_salary = int(input("Enter Base Salary: "))
performance_rating = input(
    "Enter Employee Performance Rating (Excellent, Good, Needs Improvement): "
)
experience = int(input("Enter Experience of the Employee: "))
is_manager = bool(
    input("If promoted to managerial position added 5% bonus (True/False): ")
)
is_part_time = bool(input("If he do part-time, deducted 50% bonus (True/False): "))

# Employee Data
# employee1 = {
#     "name": "Karim",
#     "base_salary": 50000,
#     "performance_rating": "Excellent",
#     "experience": 7,
#     "is_manager": False,
#     "is_part_time": False,
# }

employee1 = {
    "name": name,
    "base_salary": base_salary,
    "performance_rating": performance_rating,
    "experience": experience,
    "is_manager": is_manager,
    "is_part_time": is_part_time,
}

# Experience Levels
employee_experience = int(employee1.get("experience"))

# Approach 1
# employee_level = ""
#
# if employee_experience > 6:
#     employee_level = "Senior"
# elif employee_experience >= 3 and employee_experience <= 6:
#     employee_level = "Mid-Level"
# else:
#     employee_level = "Junior"
#
# print(employee_level)

# Approach 2
if employee_experience > 6:
    employee1["level"] = "Senior"
# elif employee_experience >= 3 and employee_experience <= 6:
elif 3 <= employee_experience <= 6:
    employee1["level"] = "Mid-Level"
else:
    employee1["level"] = "Junior"

# print(employee1)

# Performance Rating and Bonus Percentage
performance_rating = employee1.get("performance_rating")

if performance_rating == "Excellent":
    if employee1["level"] == "Senior":
        employee1["bonus_percentage"] = 20
    elif employee1["level"] == "Mid-Level":
        employee1["bonus_percentage"] = 15
    elif employee1["level"] == "Junior":
        employee1["bonus_percentage"] = 10
elif performance_rating == "Good":
    if employee1["level"] == "Senior":
        employee1["bonus_percentage"] = 15
    elif employee1["level"] == "Mid-Level":
        employee1["bonus_percentage"] = 10
    elif employee1["level"] == "Junior":
        employee1["bonus_percentage"] = 5
elif performance_rating == "Needs Improvement":
    if employee1["level"] == "Senior":
        employee1["bonus_percentage"] = 10
    elif employee1["level"] == "Mid-Level":
        employee1["bonus_percentage"] = 5
    elif employee1["level"] == "Junior":
        employee1["bonus_percentage"] = 0
else:
    print("This is not list in the performance rating")

# Bonus Calculation
total_bonus = (employee1["bonus_percentage"] / 100) * employee1["base_salary"]

# Promoted Managerial position bonus over total bonus
if employee1["is_manager"]:
    total_bonus += (5 / 100) * total_bonus

# Reduce 50% bonus from total bonus if the employee is part-time
if employee1["is_part_time"]:
    total_bonus -= (50 / 100) * total_bonus

employee1["total_bonus"] = total_bonus

print(employee1)
