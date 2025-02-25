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