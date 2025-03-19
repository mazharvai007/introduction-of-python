# Declaring variables
from typing import Final

a = "Python"

# We should write clean code to understand for anyone like this
language = "Python"

# Rules 1: A variable name must start with a letter or the underscore character
age = 27

# Rules 2: A variable name can not start with a number like this
# 1hello = ""

# Rules 3: A variable name can only contain alpha-numeric (A-Za-z0-9) characters and underscore
first_name = "Abdur"
lastName = "Rahim"

# Rules 4: Variable names are case-sensitive
name = "Python"
NAME = "Python"
Name = "Python"

# Rules 5: We can not use reserved keywords as a variable
# We can find reserved keywords this way

# print(help("keywords"))

# Object Identity (Reference of variable or how python store variable in the memory)
num1 = 10
num2 = 20
num3 = 10

print(id(num1)) # 94854763578064
print(id(num2)) # 94854763578384
print(id(num3)) # 94854763578064

variable1: Final = 10
print(variable1)

variable2 = 12
print("Address of variable:", id(variable2))
print(variable2)

variable2 = "Test"
print(variable2)