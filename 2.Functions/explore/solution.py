from functools import singledispatch


# Solution 1 for Example Problem 1


@singledispatch  # Decorator
def greet(value):
    return "The value type does not support here"


@greet.register(int)
def handle_int(value):
    return value + 10


@greet.register(str)
def handle_str(value):
    value = "Hello " + value
    return value


print(greet(10))
print(greet("Python"))  # Hello Python
print(greet({"name": "John", "age": 15}))

# Solution 2 for Decorator function with looses it's signature
from functools import wraps


def decorator(func):
    @wraps(func)  # wraps -> preserved function signature
    def wrapper(*args, **kwargs):
        print("Start Function")
        func(*args, **kwargs)
        print("End Function")
        print("-----------------")

    return wrapper


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

# Base number with power - here power will be fixed for some rasons
from functools import partial


def calculate(base_number, power):
    return base_number**power


square = partial(calculate, power=2)
cube = partial(calculate, power=3)
quard = partial(calculate, power=4)


# Square
print(square(5))
print(square(10))
print(square(25))

print("----------------------")

# Cube
print(cube(40))
print(cube(75))
print(cube(100))

print("----------------------")

# Quard
print(quard(40))
print(quard(75))
print(quard(100))

print("----------------------")
# Fifth
print(calculate(10, 5))

# Solution for sleep of n time by caching as it is taking n time for sleep.
from functools import lru_cache
from time import sleep


@lru_cache
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

print("->>>>>>>>>>>>>>>>>")

print(sleep_func("Python"))
print("---------------")
print(sleep_func("JavaScript"))
print("---------------")
print(sleep_func("Rafiq"))

print("->>>>>>>>>>>>>>>>>")

print(sleep_func("Kamal"))
print(sleep_func("Jamal"))
print(sleep_func("Zia"))

print("->>>>>>>>>>>>>>>>>")

print(sleep_func("Python"))
print("---------------")
print(sleep_func("JavaScript"))
print("---------------")
print(sleep_func("Rafiq"))

print("->>>>>>>>>>>>>>>>>")


print(sleep_func("React"))
print(sleep_func("Vue"))
print(sleep_func("Angular"))
