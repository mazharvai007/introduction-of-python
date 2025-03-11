"""
List of Keywords in Python

True        False       None        and     
or          not         is          if      
else        elif        for         while
break       continue    pass        try
except      finally     raise       assert
def         return      lambda      yield
class       import      from        in
as          del         global      with
nonlocal    async       await

"""

# Getting list of all Python keywords
import keyword
# print("The list of keywords are: ")
# print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

"""
Value keywords: 

True, False, None, del
"""
print(False == 0)
print(True == 1)
print(True + True + True)
print(True + False + False)
print(None == 0)
print(None == [])

print("------------")

"""
Operator Keywords: 

and, or, not, in, is
"""
key1 = True
key2 = False
print(key1 and key2)
print(key1 or key2)
print(not key1)

print("------------")

# in keyword
print(3 in [1,2,3])

if "s" in "gray scale":
    print("S is part of gray-scale")
else:
    print("S is not part of gray-scale")

print("------------")

# is Keyword
print(2 is 2)

a = [1,2,3]
b = a
c = [1,2,3]
print(a is b)
print(a is c)

print("------------")

"""
Conditional keywords:

if elif else
"""
x = 0

if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
    
    print("------------")

"""
Iteration Keywords:
for, while, break, continue, pass
"""
for num in range(10):
    if num == 2:
        continue
    print(num)
    
print("------------")
    
count = 0
while count <= 5:
    count += 1
    if count == 3:
        break
    print(count)

print("------------")

n = 10
for i in range(n):
    pass

"""
Exception Handling Keywords:
try, except, finally, raise, assert
"""
num1, num2 = 4, 0

# tyr except finally
try:
    int_div = num1 // num2
    print(int_div)
except ZeroDivisionError:
    print("This is always zero")
finally:
    print("This is always executed")

print("The value of num1 / num2 is:")

print("------------")

# assert
# assert num2 != 0, "Divide by 0 error"
# print(num1 / num2)

# raise
# temp = "I am learning Python"
# if temp != "am":
#     raise TypeError("Both the string are different")

"""
del Keyword
"""
string = "I am learning JavaScript"
print(string)

# del string
# print(string)

print("------------")

"""
Structure Keywords:

def, class, return, lambda
"""

# def - declare for creating functions
def fun():
    print("Python is very funny!")
    
fun()

print("------------")

# class - is used to declare user defined classes
# class Human:
#     attar1: "Head"
#     attar2: "Eyes"
#     attar3: "Nose"
     
# return - is used to return something from the function
def funnyBoy():
    num3 = 3 # assign he value 3 to num3
    
    return num3 # return the value of num3
print(funnyBoy())

print("------------")

# yield - is used like return statement but it is used to return a generator
def doFun():
    yield 1 # yield the value 1, pausing the function here
    
    yield 2 # yield the value 2, pausing the function here
    
    yield 3 # yield the value 3, pausing the function here

for value in doFun():
    print(value)
    
print("------------")

# Lambda - is used to make inline returning functions without no statements allowed internally

num4 = lambda x: x * x * x + x
print(num4(3))

"""
Context Keywords:
with, as
"""
# with open("./test.txt", "w") as file:
#     file.write("Hello, Python!")

import math as mymath
print(mymath.factorial(5))

""" 
Import and Module:
Import, from
"""
from math import factorial
import math
print(math.factorial(10))
print(factorial(10))

""" 
Scope and Namespace:

Global, Nonlocal
"""

number1 = 15
number2 = 10

def add():
    # add global variables number1 and number2
    sum = number1 + number2
    print(sum)
add()

def funny():
    # local variable
    number3 = 20
    
    def gun():
        # Modify number3 in the enclosing scope (fun)
        nonlocal number3
        number3 += 30
        print(number3)
    gun()
funny()

""" 
Async Programming:
async, await
"""

import asyncio

# Define an asynchronous main function
async def main():
    await asyncFun()
    

# Define aother async function that prints a message
async def asyncFun():
    print("Hello, Async function of Python!")

# Run the main function using asyncio.run
asyncio.run(main())