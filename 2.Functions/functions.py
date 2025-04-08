# base function
def greet():
    """A function that simple print Hello"""

    print("Hello, Welcome to Python Function")


greet()

print("-----------------------")


# Input and Output - Arguments and parameter
def input_output(name):
    """User input a name, the function will return output based on the user input"""

    print(f"Hello, {name}")


# Approach 1 - Function call with input
input_output(name="Python")

# Approach 2
input_output("Karim")

print("-----------------------")


# Function with multiple parameters/arguments
def multiple_arguments(name="John", age=20):
    """user input multiple arguments"""

    print(f"Hello {name}, you are {age} years old.")


multiple_arguments()
multiple_arguments("Rafiq", 18)
multiple_arguments(name="Ratul", age=15)
multiple_arguments(age=25, name="Rasel")

print("-----------------------")


# function with optional parameter
def person(name, email, age=None):
    """user can input name, email and age, here the age is optional parameter. Here checked age data type and None"""

    if age is not None and isinstance(age, int) and age >= 18:
        print(
            f"Hello {name}, you are getting permission for vote. You must use your {email} when you are voting"
        )
    else:
        print(
            f"{name} are under 18, and your email {email} is not registered on our system. You are unable for vote now."
        )

    # print(f"I am {name}, and my email is {email}")
    # print(f"I am {name}, I am {age} years old, and my email is {email}")


person("Karim", "karim@gmail.com", "B")
person("Jamal", "jamal@gmail.com", 17)
person("Rafique", "rafique@gmail.com", age=20)

print("-----------------------")


# Percentage Calculation
def get_percentage(amount=None, percentage=None):
    """User input amount and percentage, it will be returned with floating value"""

    if (
        amount is not None
        and percentage is not None
        and isinstance(amount, int)
        and not isinstance(amount, float)
        and isinstance(percentage, int)
        and not isinstance(percentage, float)
    ):

        return (amount * percentage) / 100
    else:
        return "Enter integer value for amount and percentage"


percentage_amount = get_percentage()
print(percentage_amount)
percentage_amount = get_percentage(amount=50000, percentage=30)
print(percentage_amount)
percentage_amount = get_percentage(amount=30000.50, percentage=25.5)
print(percentage_amount)

print("-----------------------")


# Number calculation by power
def number_calculate(number):
    square = number**2
    cube = number**3

    # return f"Square: {square}, and Cube: {cube}"
    return (square, cube)


number_calc = number_calculate(3)
print(number_calc)

print("-----------------------")


# function as an argument
def square(number):
    return number**2


def cube(number):
    return number**3


def quard(number):
    return number**4


def helper_func(fun_name, number):
    return fun_name(number)


my_square = helper_func(fun_name=square, number=3)
print("Square:", my_square)

my_cube = helper_func(fun_name=cube, number=3)
print("Cube:", my_cube)

my_quard = helper_func(fun_name=quard, number=3)
print("Quard", my_quard)

print("-----------------------")


# A function returning a function
def outer_func():
    print("Outer Function")

    def inner_func():
        print("Inner Function")

    return inner_func


# Approach 1
outer_func()  # print outer function
print("-----------------------")
outer_func()()  # print inner function

print("-----------------------")

# Approach 2
func_as_func = outer_func
func_as_func()
print("-----------------------")
func_as_func()()

print("-----------------------")
# Approach 3
func_as_func = outer_func()
func_as_func()

print("-----------------------")


# Decorator
def sum_func(n):
    sum = 0

    for i in range(1, n + 1, 1):
        sum += i
    print(sum)
    return sum


print("Calling the function")
print(sum_func(5))
print("Function is finished!")


print("Calling the function")
print(sum_func(10))
print("Function is finished!")

print("Calling the function")
print(sum_func(15))
print("Function is finished!")


print("-----------------------")


# Make Decorator Function - Approach 1
def decorator_funcion(func):

    def wrapper_func():
        print("Calling the function")
        print(func)
        print("Function is finished!")

    return wrapper_func()


decorator_funcion(sum_func(5))
print("-----------------------")
decorator_funcion(sum_func(10))

print("============================")


def decorator_helper_func():
    print("I am decorator helper function")


# Make Decorator Function - Approach 2
def decorator_function(func):
    def wrapper_func():
        print("Calling the function")
        func()
        print("Function is finished!")

    return wrapper_func


my_decorator = decorator_function(decorator_helper_func)
my_decorator()

print("================================")


# decorator function with parameter
def decorator_with_parameter(func):
    def wrapper_func(num):
        print("Calling the function")
        func(num)
        print("Function is finished!")
        print("------------------------")

    return wrapper_func


my_decorator = decorator_with_parameter(sum_func)
my_decorator(5)
my_decorator(10)
my_decorator(15)
my_decorator(20)


# Handle multiple arguments with decorator function
def addition(num1, num2):
    print(num1 + num2)


def multiple_params_with_decorator(func):
    def wrapper_func(*args, **kwargs):
        print("Calling the function")
        func(*args, **kwargs)
        print("Function is finished!")
        print("------------------------")

    return wrapper_func


my_decorator_args1 = multiple_params_with_decorator(sum_func)
my_decorator_args1(3)
my_decorator_args1(5)

my_decorator_args2 = multiple_params_with_decorator(addition)
my_decorator_args2(10, 15)
my_decorator_args2(15, 25)

# decorator with sting


def decorator_str():
    print("I am decorator string")


my_decorator_args3 = multiple_params_with_decorator(decorator_str)
my_decorator_args3()

print("------------------------")


# Shortcut
def decorator_shortcut(func):
    def wrapper_func(*args, **kwargs):

        print("Calling the decorator shortcut function")
        func(*args, **kwargs)
        print("Shortcut Function is finished!")
        print("------------------------")

    return wrapper_func


@decorator_shortcut
def greetings():
    print("Welcome to Python")


greetings()


@decorator_shortcut
def multiplication(a, b):
    print(a * b)


multiplication(5, 6)
