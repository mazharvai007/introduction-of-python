def add(a, b):
    return a + b  # returning sum of a and b


def is_true(a):
    return bool(a)  # returning boolean of a


print("--------------------")


# Calling function
result = add(3, 2)
print(result)

result = is_true(result)
print(result)

print("--------------------")


# Returning Multiple Values
def person():
    name = "Kamal"
    age = 30
    return name, age


name, age = person()
print(name)
print(age)

print("--------------------")


# Returning List
def return_list(n):
    return [n**2, n**3]


result = return_list(4)
print(result)

print("--------------------")


# Function returning another function
def first_class_citizen(msg):
    def higher_order_function():
        return f"Message: {msg}"

    return higher_order_function


result = first_class_citizen(
    "This is first class citizen including higher order function"
)
print(result())
