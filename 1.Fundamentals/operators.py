"""
Operator - represent action (+, =)
Arithmetic Operators (+, -,  *, /, %, **(exponent))
Comparison Operators (==, !=, >, >=, <, <=)
Logical Operators (and, or, not)
Bitwise Operators
Assignment Operators (=, +=, -=, *=, /=)
Membership Operators (in, not in)

Operand - helps operators to do action (sum, num1, num2)

sum = num1 + num2

Here (+, =) sings are operator
And (sum, num1 and num2) are operand

What is goal of operator? It's tells us to do an action
"""

""" 
Arithmetic Operators
"""
num1 = 15
num2 = 10

# Addition
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Exponentiation:", num1 ** num2)

print("-----------")

"""
Comparison Operators
"""
print(num1 > num2)  # true
print(num1 < num2)  # false
print(num1 == num2)  # false
print(num1 != num2)  # true
print(num1 >= num2)  # true
print(num1 <= num2)  # false

print("-----------")

""" 
Logical Operators
"""
a = True
b = False

print(a and b)
print(a or b)
print(not a)

# Or (Truth/False Table)
# ----------------------

# Condition 1 | Condition 2 | Condition and Condition 2
# ------------------------------------------------------
# True        | True        | True
# ------------------------------------------------------
# True        | False       | True
# ------------------------------------------------------
# False       | True        | True
# ------------------------------------------------------
# False       | False       | False
# ------------------------------------------------------

# And (Truth/False Table)
# ------------------------

# Condition 1 | Condition 2 | Condition and Condition 2
# ------------------------------------------------------
# True        | True        | True
# ------------------------------------------------------
# True        | False       | False
# ------------------------------------------------------
# False       | True        | False
# ------------------------------------------------------
# False       | False       | False
# ------------------------------------------------------

# Not (Opposite)
# -----------------
#
# Condition 1 | Not Condition 1
# ------------------------------
# True        | False
# ------------------------------
# False       | True
# ------------------------------

user_age = 10
user_gender = "M"

condition1 = user_age >= 25
condition2 = user_gender == "M"

decision = condition1 and condition2
print(decision)

decision = condition1 or condition2
print(decision)

decision = not condition2
print(decision)

is_subscribed = False
is_member_user = True

condition = is_subscribed or is_member_user
print(condition)

print("-----------")

"""
Bitwise Operators

Bitwise NOT (^)
Bitwise SHIFT (<<, >>)
Bitwise AND (&)
Bitwise XOR (~)
Bitwise OR (|)
"""
print(num1 & num2)
print(num1 | num2)
print(~num1)
print(num1 ^ num2)
print(num1 >> num2)
print(num1 << num2)
print(num1 >> 2)
print(num1 << 2)

print("-----------")

""" 
Assignment Operator
"""
num3 = num1
num4 = num2
print(num3)
print(num4)
num4 += num3
print(num4)
num4 -= num3
print(num4)
num4 *= num3
print(num4)
num4 <<= num3
print(num3)

print("-----------")

"""
Identity Operators
"""
print(num3 is not num4)
print(num3 is num4)

print("-----------")

""" 
membership operators
"""

myList = [1, 2, 3, 4, 5, 10]
num4 = 60

if num1 not in myList:
    print("Num1 is NOT present in given list")
else:
    print("Num1 is present in given list")

if num2 in myList:
    print("Num2 is present in given list")
else:
    print("Num2 is NOT present in given list")

isPresentNum = num4 in myList
print(isPresentNum)

isNotPresentNum = num4 not in myList
print(isNotPresentNum)

print("-----------")

""" 
Ternary Operator
"""
minimum = num1 if num1 < num2 else num2
print(minimum)

print("-----------")

"""
Precedence and Associativity Operators
"""
expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 10

if name == "Alex" or name == "John" and age >= 2:
    print("Welcome baby boy")
else:
    print("Good Bye!!!")

print(100 / 10 * 10)  # 100
print(5 - 2 + 3)  # 6
print(5 - (2 + 3))  # 0
print(2 ** 3 ** 2)  # 512

sum1 = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
remainder = num1 % num2

print("Sum:", sum1)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
print("Remainder:", remainder)

if num1 > num2:
    print("The first number is greater")
elif num1 < num2:
    print("The second number is greater")
else:
    print("The numbers are equal")

comparison_1 = num1 == num2
print(comparison_1)

num1 = num2
comparison_1 = num1 == num2
print(comparison_1)

test = 5
test += 5
test += 5

print(test)

username = "Karim"
checked = username is None
print(checked)

username = None
checked = username is None
print(checked)

is_logged_in = True
checked = is_logged_in is True
print(checked)

checked = is_logged_in is False
print(checked)

print("-----------")
