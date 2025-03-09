"""
Conditional Statement

if

elif

else
"""

age = 61

if age < 0:
    print("You are a minor!")
elif age < 18:
    print("You are too young!")
elif age >= 18 and age <= 60:
    print("You are an adult")
else:
    print("You are a senior citizen")
    
    
# The most well-known conditional statement is if
num_value = int(input("Please enter an integer: "))
if num_value < 0:
    num_value = 0
    print("Negative changed to zero")
elif num_value == 0:
    print("Zero")
elif num_value == 1:
    print("Single")
else:
    print("More")