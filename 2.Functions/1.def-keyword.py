# from itertools import count


# def func():
#     print("Hello")
# func()

# Pyhon def syntax
# def my_name(name):
#     print("My name is", name)
# my_name("Mazhar")

# Example 1: Create function to find the addition, subtraction, multiplication, and division of two numbers

# num1 = 90
# num2 = 50

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# print("Results: ----------")
#
# def add_numbers(x, y):
#     return x + y
#
# result = add_numbers(num1, num2)
# print("Addition of", num1, "and", num2, 'is', result)
#
# def sub_numbers(x, y):
#     return x - y
#
# result = sub_numbers(num1, num2)
# print("Subtraction of", num1, "and", num2, "is", result)
#
# def multiply_numbers(x, y):
#     return x * y
#
# result = multiply_numbers(num1, num2)
# print("Multiplication of", num1, "and", num2, "is", result)
#
# def divide_numbers(x, y):
#     return x / y
# result = divide_numbers(num1, num2)
# print(f"Divide of {num1} and {num2} is {result}")


# Example 2: Create function with the first 10 price numbers
def find_prime_numbers(get_num):
    x_num = 2
    number_count = 0

    while number_count < get_num:
        for num in range(2, int(x_num**0.5) + 1):
            if x_num % num == 0:
                break
            else:
                print(x_num)
                number_count += 1

        x_num += 1

    print(get_num + x_num)


input_num = 10
find_prime_numbers(input_num)

print("--------------------")


# Passing function as argument
def fun(func, arg):
    return func(arg)


def square(x):
    return x**2


result = fun(square, 5)
print(result)

print("--------------------")


# Python def keyword example with *args
"""
Explanation:

- This function takes two parameters: func (a function) and x (a value). It applies the function func to the value x and returns the result.
- We call fun and pass the square function (without parentheses) and the number 5. The square function is applied to 5, and the result is printed.
"""


def fun_with_args(*args):
    for arg in args:
        print(arg)


fun_with_args(1, 2, 3, 4, 5)

print("--------------------")


# Python def keyword example with **kwargs
"""
Explanation:

- **kwargs collects the keyword arguments passed to example_function into a dictionary kwargs.
- Inside the function, you can iterate over the dictionary and print the key-value pairs.
"""


def fun_with_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


fun_with_kwargs(name="Alice", age=30, city="New York")


# Python def keyword example with the class
class Person:
    # constructor to initialize the person's name and age
    def __init__(self, name, age):
        self.name = name  # set the name attribute
        self.age = age  # set the age attribute

    # method to print a greeting message
    def greet(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


person1 = Person("Karim", 30)
person1.greet()

print(person1.name)
print(person1.age)
