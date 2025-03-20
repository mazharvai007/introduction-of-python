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
elif age >= 18 and age < 61:
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

# Ternary condition
# value_if_true if condition else value_if_false
nid = True
print("You are eligible to vote") if age >= 18 and nid == True else print("You are not eligible for vote.")

marks = 68
print("A+") if marks >= 80 else print("A") if marks >= 70 else print("B") if marks >= 60 else print("C") if marks >= 50 else print("D") if marks >= 33 else print("Fail")
