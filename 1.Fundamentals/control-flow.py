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
# num_value = int(input("Please enter an integer: "))
# if num_value < 0:
#     num_value = 0
#     print("Negative changed to zero")
# elif num_value == 0:
#     print("Zero")
# elif num_value == 1:
#     print("Single")
# else:
#     print("More")

# Ternary condition
# value_if_true if condition else value_if_false
nid = True
(
    print("You are eligible to vote")
    if age >= 18 and nid == True
    else print("You are not eligible for vote.")
)

marks = 68
(
    print("A+")
    if marks >= 80
    else (
        print("A")
        if marks >= 70
        else (
            print("B")
            if marks >= 60
            else (
                print("C")
                if marks >= 50
                else print("D") if marks >= 33 else print("Fail")
            )
        )
    )
)

print("----------------")

# Even - Odd number checking

# get_number = int(input("Please enter a number: "))

# if get_number % 2 == 0:
#     print(f"{get_number} is an even number")
# else:
#     print(f"{get_number} is an odd number")

# print("----------------")

"""
Find the greatest number

Input two numbers from users

check condition with one is big
"""

# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))

# if number1 == number2:
#     print(f"{number1} and {number2} are equal")
# elif number1 >= number2:
#     print(f"{number1} is greater than {number2}")
# else:
#     print(f"{number2} is greater than {number1}")

# print("----------------")

# Vowel or Consonent
character = input("Enter a character: ")

# Approach 1

if character == "a" or character == "A":
    print(f"{character} is vowel")
elif character == "e" or character == "E":
    print(f"{character} is vowel")
elif character == "i" or character == "I":
    print(f"{character} is vowel")
elif character == "o" or character == "O":
    print(f"{character} is vowel")
elif character == "u" or character == "U":
    print(f"{character} is vowel")
else:
    print(f"{character} is consonent")

# Approach 2

if (
    character == "a"
    or character == "A"
    or character == "e"
    or character == "E"
    or character == "i"
    or character == "I"
    or character == "o"
    or character == "O"
    or character == "u"
    or character == "U"
):
    print(f"{character} is vowel")
else:
    print(f"{character} is consonent")
