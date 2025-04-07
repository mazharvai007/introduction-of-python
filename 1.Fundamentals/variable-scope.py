"""Variable Scope (Global and Local)"""

user_name = "This is Global Scope"


# Approach 1
def scope_function(user_name):
    print(user_name)


scope_function("This is local scope")


print(user_name)

print("=======================")

# Approach 2
scope_function(user_name)

print("=======================")


# Approach 3
x = 6


def greet(user_name):
    """the global x will be accessible from outside of the function if it is calling below the function calling"""
    global x
    x = 10

    print(user_name)


print(x)  # 6
greet("Karim")
print(x)  # 10
x = 7
print(x)  # 7
