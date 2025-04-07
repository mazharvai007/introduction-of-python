def fun(*args):
    return sum(args)


print(fun(1, 2, 3, 4))
print(fun(5, 10, 15))

print("============================")


def fun(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


fun(a=1, b=2, c=3)

print("============================")


# *args- example 1
def myFun(*argv):
    for args in argv:
        print(args, end=" ")


myFun("Hello", "I", "am", "learning", "Python")

print("============================")


# *args- example 2
def myFun2(arg1, *argv):
    print(f"First Argument: {arg1}")

    for arg in argv:
        print(f"Argument *argv: {arg}")


myFun2("Hello", "I", "am", "learning", "Python")

print("============================")


# **kwargs - example 1
def myfun3(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


myfun3(str1="Are", str2="You", str3="Learning", str4="Python?")

print("============================")


# **kwargs - example 2
def myFun4(arg1, **kwargs):
    print(f"First Argument: {arg1}")

    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


myFun4("Hello,", str1="Are", str2="You", str3="Learning", str4="Python?")


# Using both *args and **kwargs
def myFun5(*args, **kwargs):
    print(f"Positional Arguments:{args}")
    print(f"Keywords Arguments {kwargs}")


myFun5(1, 2, 3, a=1, b=2, c=3)

print("============================")


# Positional Argument - Approach 1
def positional_args(*args):
    return args[0] + args[1] + args[2]


pa1 = positional_args(1, 2, 3)
print(pa1)

print("============================")


def positonal_args1(*args):
    sum = 0

    for num in args:
        if not isinstance(num, str):
            sum += num

    return sum


sum1 = positonal_args1("a", 2, 3, 1)
sum2 = positonal_args1(2, 3, 4)
sum3 = positonal_args1(2, 3, 4, 5)
sum4 = positonal_args1(2, 3, 4, 5, 6)
sum5 = positonal_args1(2, 3, 4, 5, 6, 7)
sum6 = positonal_args1(2, 3, 4, "5", 6, "7", 8, 9, 10)
sum7 = positonal_args1(2, 3, 4, "5", 6, "7", 8, 9, 10, 11.5, 12.9)

print(sum1, sum2, sum3, sum4, sum5, sum6, sum7)


print("============================")


# Example for **kwargs - Approach 1
def greet(**kwargs):
    print(kwargs.get("username"))
    print(kwargs.get("is_loggedin"))
    print(kwargs.get("is_subscribed"))
    print("============================")


greet()
greet(username="Kamal")
greet(username="Kamal", is_loggedin=True)
greet(username="Kamal", is_loggedin=True, is_subscribed=False)


# Approach 2 - Checked None type
def greet(**kwargs):
    if kwargs.get("username") is not None:
        print(kwargs.get("username"))

    if kwargs.get("is_loggedin") is not None:
        print(kwargs.get("is_loggedin"))

    if kwargs.get("is_subscribed") is not None:
        print(kwargs.get("is_subscribed"))

    print("============================")


greet()
greet(username="Sakib")
greet(username="Jashim", is_loggedin=True)
greet(username="Fasil", is_loggedin=True, is_subscribed=False)


# Approach 3 - Checked None type by improving the code
def greet(**kwargs):
    user_name = kwargs.get("username")
    is_loggedin = kwargs.get("is_loggedin")
    is_subscribed = kwargs.get("is_subscribed")

    if user_name is not None:
        print(kwargs.get("username"))

    if is_loggedin is not None:
        print(kwargs.get("is_loggedin"))

    if is_subscribed is not None:
        print(kwargs.get("is_subscribed"))

    print("============================")


greet()
greet(username="Sakib")
greet(username="Jashim", is_loggedin=True)
greet(username="Fasil", is_loggedin=True, is_subscribed=False)
