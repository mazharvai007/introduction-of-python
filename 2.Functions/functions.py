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
