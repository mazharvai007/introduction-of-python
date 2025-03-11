print(2+2)
print(50-5*6)
print((50-5*6)/4)
print(8/5) # division always returns a floating point number

# The integer numbers (e.g. 2, 4, 20) have type int, the ones with a fractional part (e.g. 5.0, 1.6) have type float.

# Division (/) always returns a float. To do floor division and get an integer result (discarding any fractional result) you can use the // operator; to calculate the remainder you can use %

print(17/3) # classic division returns a float
print(17//3) # floor division discards the fractional part
print(17%3) # the % operator returns the remainder of the division
print(5*3+2) # result * divisor + remainder

# With Python, it is possible to use the ** operator to calculate powers
print(5**2) # 5 squared
print(2**7) # 2 to the power of 7

width = 20
height = 5*9
print(width * height)

print(4*3.75-1)

tax = 12.5/100
price = 100.50
print(price * tax)

# Fibonacci series
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b

while a < 1000:
    print(a, end=",")
    a, b = b, a + b
    
print(-(3**3))

i = 256*256
print("The value of i is:", i)

num1, num2 = 0, 1
while num1 < 1000:
    print(num1, end=",")
    num1, num2 = num2, num1 + num2

