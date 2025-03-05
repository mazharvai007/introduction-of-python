student_name = input("Enter Student name: ")
age = int(input("Enter Age: "))
roll_number = int(input("Enter Roll Number: "))
math = int(input("Enter Marks in Math: "))
science = int(input("Enter Marks in Science: "))
english = int(input("Enter Marks in English: "))

total_marks = math + science + english
average_marks = total_marks // 3

print("Student Report:")
print("------------------")

print("Name:", student_name)
print("Age:", age)
print("Roll Number:", roll_number)
print("Total Marks:", total_marks)
print("Average:", average_marks)