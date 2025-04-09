# Example Function - Problem 1
def greet(value):
    if isinstance(value, int):
        value += 10
        return value

    if isinstance(value, str):
        value = "Hello " + value
        return value

    return "The value type does not support here"


print(greet(10))  # 20
print(greet("Python"))  # Hello Python
print(greet({"name": "John", "age": 15}))

print("===================================")


# Example Function - Problem 2
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Start Function")
        func(*args, **kwargs)
        print("End Function")
        print("-----------------")

    return wrapper


# Using a decorator, main function looses it's signature
@decorator
def my_sum(n):
    """
    The function gives the sum up to `n`
    """
    sum = 0
    for i in range(1, n + 1):
        sum += i

    return f"{n} => {sum}"


print(my_sum.__name__)
print(my_sum.__doc__)

print("===================================")


# Base number with power
def calculate(base_number, power):
    return base_number**power


# Square
print(calculate(5, 2))
print(calculate(10, 2))
print(calculate(25, 2))

print("----------------------")

# Cube
print(calculate(40, 3))
print(calculate(75, 3))
print(calculate(100, 3))

print("----------------------")

# Quard
print(calculate(40, 4))
print(calculate(75, 4))
print(calculate(100, 4))

print("===================================")

# Sleep for n times

from time import sleep


def sleep_func(name):
    print(f"for {name}")

    print("Task - 1")
    print("Task - 2")

    sleep(2)

    return f"Hello, {name}"


print(sleep_func("Python"))
print("---------------")
print(sleep_func("JavaScript"))
print("---------------")
print(sleep_func("Rafiq"))

print("===================================")

# Type Hint / Type annotation


def type_hint_func(name: str) -> str:
    return f"Hello {name}"


print(type_hint_func("Python"))
print(type_hint_func(5))


def power_calculate(base_number: int | float, power: int | float) -> int | float:
    """
    This is power calculation function
    It received base number and power as integer or float
    """
    return base_number**power


print(power_calculate(5, 10))
