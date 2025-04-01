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
        for num in range(2, int(x_num ** 0.5) + 1):
            if x_num % num == 0:
                break
            else:
                print(x_num)
                number_count += 1

        x_num += 1

    print(get_num + x_num)

input_num = 10
find_prime_numbers(input_num)
