"""
Data Types:

Numeric = int, float, complex
Sequence Type = string, list, tuple
Mapping Type = dict
Boolean = bool
Set type = set, frozenset
Binary Types = bytes, bytearray, memoryview
"""

val = 50
print(val)

val = 60.5
print(val)

val = "Hello, Python!"
print(val)

val = ["Python", "for", "Data", "Science"]
print(val)

val = ("Python", "for", "Machine", "Learning")
print(val)

""" 
Numeric Data Types:
int, float, complex
"""

# Integer
int_num = 5
print(type(int_num))

# Floating Number
float_num = 50.50
print(type(float_num))

# Complex
complex_num = 2 + 4j
print(type(complex_num))

print("-------------")

""" 
Sequence Data Types:
string, list, tuple
"""

# String Data Type
string = "Welcome to Python a largest snack at South Asia region"
print(string)
print(type(string))
print(string[1])
print(string[2])
print(string[3])

print("-------------")

# List Data Type
list_type = []
list_type = [1, 2, 3]
print(list_type)
print(type(list_type))

list_type = ["Welcome", "to", "Python", "a", "largest", "snack", "at", "South-Asia", "region"]
print(list_type)
print(len(list_type) - 3)

# From First
print(list_type[0])
print(list_type[1])
print(list_type[2])
print(list_type[3])
print(list_type[4])
print(list_type[5])
print(list_type[6])
print(list_type[7])
print(list_type[8])

# From Last
print(list_type[-1])
print(list_type[-2])
print(list_type[-3])
print(list_type[-4])
print(list_type[-5])
print(list_type[-6])
print(list_type[-7])
print(list_type[-8])
print(list_type[0])

print("-------------")

# Tuple Data Type
tup1 = ()
print(tup1)

tup2 = ("Learn", "for")
print(tup2)

tup3 = tuple("Welcome to Python a largest snack at South Asia region")
print(tup3)

tup4 = tuple(["Welcome", "to", "Python", "a", "largest", "snack", "at", "South-Asia", "region"])
print(tup4)

print(tup2[1])
print(tup3[10])
print(tup4[2])

print("-------------")

"""
Boolean Data Type:
bool
"""
print(type(True))
print(type(False))
# print(type(true))

"""
Set data type
"""
set1 = set()
set1 = set("I am coding in Python")
print(set1)

set2 = set(["Welcome", "to", "Python", "a", "largest", "snack", "at", "South-Asia", "region"])
print(set2)

for char in set1:
    print(char, end='')
print("coding" in set1)

print("-------------")

""" 
Dictionary Data Type
"""
dict1 = {}
dict1 = {1: "I", 2: "Coding", 3: "in", 4:"Python"}
print(dict1)

# Creating dictionary using dict() constructor
dict2 = dict(dict1)
print(dict2)

dict3 = dict({1: "Python", "is": "is", 3: "a", 4: "snack"})
print(dict3)

# Accessing an element using key
print(dict1[2])
print(dict2[3])
print(dict3['is'])

# Accessing an element using get
print(dict3.get(4))