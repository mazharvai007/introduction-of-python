"""
Operator - represent action (+, =)
Arithmetic Operators (+, -,  *, /, %, **(exponent))
Comparison Operators (==, !=, >, >=, <, <=)
Location Operators (and, or, not)
Assignment Operators (=, +=, -=, *=, /=)
Membership Operators (in, not in)

Operand - helps operators to do action (sum, num1, num2)

sum = num1 + num2

Here (+, =) sings are operator
And (sum, num1 and num2) are operand

What is goal of operator? It's tells us to do an action
"""

# Example of membership operators
myList = [1, 2, 3, 4, 5, 10]
num4 = 60

isPresentNum = num4 in myList
print(isPresentNum)

isNotPresentNum = num4 not in myList
print(isNotPresentNum)