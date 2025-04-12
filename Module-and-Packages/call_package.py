# Approach 1
from calculator import add, sub, mul, div

result = add.addition_number(20, 10)
print(result)

result = sub.substruction_number(30, 15)
print(result)

result = mul.multiplication_number(5, 6)
print(result)

result = div.division_number(10, 5)
print(result)

print("===========================")

# Approach 2
# from calculator.add import addition_number
# from calculator.sub import substruction_number
# from calculator.mul import multiplication_number
# from calculator.div import division_number

# result = addition_number(5, 6)
# print(result)

# result = substruction_number(6, 5)
# print(result)

# result = multiplication_number(6, 5)
# print(result)

# result = division_number(15, 5)
# print(result)

print("===========================")

# Approach 3 - from __init__
from calculator import (
    addition_number,
    substruction_number,
    multiplication_number,
    division_number,
)

result = addition_number(10, 5)
print(result)

result = substruction_number(10, 5)
print(result)

result = multiplication_number(10, 5)
print(result)

result = division_number(10, 5)
print(result)
