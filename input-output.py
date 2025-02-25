# name = input("Enter your name: ")
# print(name)

# By default, Python take string data type. I mean when users input something, it will be string.
# num = int(input("Enter a number: ")) # We typecast here for integer input value
# print(num)
# print(type(num))

# floatingInput = float(input("Input a floating point number: "))
# print(floatingInput)
# print(type(floatingInput))

# Outputs of Python
# Process 1
print("Hello,", "Mazhar")

# Process 2 - Multiple value output
num1 = 19
num2 = 30
print("The numbers are:", num1, num2)

# Process 3
language1 = "Python"
language2 = "Java"
print(language1)
print(language2) # After completing print, it's going to new line. How to solve it?

print(language1, end=" ")
print(language2)

# Process 4
country1 = "Bangladesh"
country2 = "Malaysia"

print("Country one is {} and country two is {}".format(country1, country2))
print("Country one is {1} and country two is {0}".format(country1, country2)) # Manage variable ordering by this way
print("Country one is {c1} and country two is {c2}".format(c1 = country2, c2 = country1)) # Custom ordering

# Process 5
print(f"Country one is {country1} and Country two is {country2}")

# Process 6
num3 = 102.1010120210
print("Number is: ", num3)
print(f"Number is: {num3:.1f}")
print(f"Number is: {num3:.2f}")
print(f"Number is: {num3:.3f}")

print("Number is: %.1f" % num3)
print("Number is: %.2f" % num3)
print("Number is: %.3f" % num3)
print("Number is: %.4f" % num3)


# Printing output by using print()
# print("Hello World!")

# Printing variables
# name = "Bob"
# print(name)
# print("Hello", name,"! You are welcome.")
# print("Hello", name + "! You are welcome.")
#
# name = "Alice"
# age = 25
# city = "New York"
# print(name, age, city)

# Output formatting
# amount = 150.75
# print("Amount: ${:.2f}".format(amount))

# Using end parameter
# print("Python", end="@")
# print("Learning")

# Using sep parameter with comma
# print("Apple", "Banana", "Lichi", sep=", ")
# print("Apples", "Mango", "Orange", sep=", ", end=" are fruits!\n")

# Date formatting
# print("16", "02","2025", sep="-")

# another formatting
# print("mazhar", "gmail.com", sep="@")

# Using f-sting
# name = "Kamal"
# age = 26
# print(f"Hello {name}, your age is {age}")

"""
Using % operator
%d = Integer
%f = Float
%s = String
%x = hexadecimal
%o = octal
"""
# taking input from user
# num = int(input("Enter a value: "))
# add = num + 5
# print("The sum is %d" %add)

# Take multiple input
# Take two inputs
# x, y = input("Enter two values: ").split()
# print("Number of x: ", x)
# print("Number of y: ", y)

# Take three inputs
# x, y, z = input("Enter three values: ").split()
# print("Value for x: ", x)
# print("Value for y: ", y)
# print("Value for z: ", z)

# Conditional input
# ageInput = input("Enter your age: ")
# convert to integer
# age = int(ageInput)

# Checking conditions
# if age < 0:
#     print("Please enter valid age")
# elif age < 18:
#     print("You are a young man")
# elif age >= 18 and age < 65:
#     print("You are an adult")
# else:
#     print("You are a senior citizen")

# Type Conversion/type casting
# name = input