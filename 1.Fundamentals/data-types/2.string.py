"""
String - collection of characters
String is a sequence of characters enclosed in single quotes, double quotes, or triple quotes.
"""

str1 = "Hello"
str2 = "Hello"
str3 = """Hello
World"""

print(str1)
print(str2)
print(str3)

"""
Properties of String
1. Immutable
2. Slicing
3. Indexing
4. Concatenation
5. Repetition
"""
print(str1[2])
print(str1.index("l"))
print(str1.count("l"))
print(str1[2:4])
print(str1[:4])
print(str1[1:])
print(str3[1:8:2])

"""
In-built functions:

1. upper
"""
print(str1.upper())
print(str3.title())
print(str3.capitalize())

print(str3.find("world"))  # -1
print(str3.find("World"))  # 6
print(str3.find("World", 7))
print(str3.replace("World", "Python"))

str4 = str3.split("\n")
print(str4)

str5, str6 = str3.split("\n")
print(str5, str6)

print(type(str4))
print(type(str5), type(str6))

str7 = "Hello I love Python"
str8, *str9 = str7.split(",")
print(str8, str9)

str10 = str7.split(" ")
print(str10[0])
print(str10[1])
print(str10[2])
print(str10[3])

print("-".join(str7))

print("-----------")

my_country = "Bangladesh"
print("I live in" + " " + my_country + ".")

# String formatting
print(f"I live in {my_country}.")
print("I live in {}".format(my_country))
print("I live in %s" % my_country)
print("I live in {0}".format(my_country))
print("I live in {country}".format(country=my_country))
