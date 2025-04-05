# Basic Example of Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

print("----------------------")


# Base Case and Recursive Case
def fabonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fabonacci(n - 1) + factorial(n - 2)


print(fabonacci(10))

print("----------------------")


# Types of Recursion in Python
def tail_fact(n, acc=1):
    if n == 0:
        return acc
    else:
        return tail_fact(n - 1, acc * n)


print(tail_fact(10))

print("----------------------")


def nontail_fact(n):
    if n == 1:
        return 1
    else:
        return n * nontail_fact(n - 1)


print(nontail_fact(10))
