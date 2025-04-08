# Lambda Function
# Syntax: lambda (parameters) : returning value


# basic function
def my_square(n):
    return n**2


print(my_square(2))  # 4

# lambda function
lambda n: n**2

# Assign a variable
my_square = lambda n: n**2

print(my_square(3))  # 9

# Multiple variable with lambda function
my_sum = lambda a, b: a + b
print(my_sum(5, 6))  # 11
