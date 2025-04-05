# Creating local variables in Python
def local_variable():
    local_var_str = "I love Python"
    print(local_var_str)


local_variable()

print("------------------")

# Can a local variable be used outside a function?
# print(local_var_str)  # local variable is not access from outside of local scope


# Create a global variable  in Python
def global_variable():
    print(global_var_str)


global_var_str = "This is Python global variable"
global_variable()
print(f"Outside Function: ", global_var_str)

print("------------------")


# Local and Global variables in Python
def fun_with_global_local_variable():
    local_string = "This is local string"
    print(local_string)


# Global Scope
global_string = "This is global string"
fun_with_global_local_variable()
print(global_string)

print("------------------")


# The global Keyword
def global_keyword():
    global local_string
    local_string += "Local String"
    print(local_string)

    local_string = "The local string is for global keyword"
    print(local_string)


local_string = "The global string! "
global_keyword()
print(local_string)

print("------------------")

num = 10


def f():
    print("Inside f()", num)


def g():
    num = 12
    print("Inside g()", num)


def h():
    global num
    num = 15
    print("Inside h()", num)


# Global scope
print("Global scope: ", num)
f()
print("Global scope: ", num)
g()
print("Global scope: ", num)
h()
print("Global scope: ", num)
