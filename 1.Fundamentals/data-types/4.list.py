# Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.

squares = [1, 4, 9, 16, 25]
print(squares)

print("------")

# Like strings (and all other built-in sequence types), lists can be indexed and sliced:
print(squares[0])  # 1 indexing returns the item
print(squares[-1])  # 25 indexing returns the last item
print(squares[-3:])  # [9,16,25] slicing returns a new list

print("------")

# Lists also support operations like concatenation:
squares = squares + [36, 49, 64, 81, 100]
print(squares)

print("------")

# Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:
cubes = [1, 8, 27, 65, 125]  # something's wrong here
print(cubes)
print(4**3)  # the cube of 4 is 64
cubes[3] = 64  # replace the wrong value
print(cubes)

print("------")

# You can also add new items at the end of the list, by using the append() method (we will see more about methods later):
cubes.append(216)  # add the cube of 6
print(cubes)
cubes.append(7**3)  # and the cube of 7
print(cubes)

print("------")

# Simple assignment in Python never copies data. When you assign a list to a variable, the variable refers to the existing list. Any changes you make to the list through one variable will be seen through all other variables that refer to it:
rgb = ["Red", "Green", "Blue"]
print(rgb)
colors = rgb
print(colors)
print(id(rgb) == id(colors))  # True they reference the same object
rgb.append("Orange")
print(rgb)

print("------")

# All slice operations return a new list containing the requested elements. This means that the following slice return a shallow copy of the list:
correct_rgba = colors[:]
correct_rgba[-1] = "Pink"
print(correct_rgba)
print(colors)

print("------")

# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
letters = ["a", "b", "c", "d", "e", "f", "g"]
print(letters)
letters[2:5] = ["C", "D", "E"]  # replace some values
print(letters)
letters[2:5] = []  # now remove them
print(letters)
letters[:] = []  # clear the list by replacing all the elements with an empty list
print(letters)

print("------")

# The built-in function len() also applies to lists:
letters = ["a", "b", "c", "d"]
print(len(letters))

print("------")

# It is possible to nest lists (create lists containing other lists), for example:
list1 = ["a", "b", "c", "d", "c", "e", "d"]
list2 = [1, 2, 3]
nested_list = [list1, list2]
print(nested_list)
print(nested_list[0])
print(nested_list[0][0])
print(nested_list[0][1])
print(nested_list[0][2])
print(nested_list[1])
print(nested_list[1][0])
print(nested_list[1][1])
print(nested_list[1][2])

print("------")

# remove duplicate
convert_set = set(list1)
# print(convert_set)
convert_list = list(convert_set)
print(convert_list)

print("------")

# Set
set_1 = {10, 20, 30, 40, 50}
print(set_1)

list3 = nested_list
list3.append(4)
print(list3)

print(id(nested_list))
print(id(list3))

print("------")

fruits = ["apple", "banana", "cherry"]
print(fruits)
print(type(fruits))
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])

print("------")

persons = [
    ["Rahim", "Karim", "Rahman"],
    [25, 30, 35],
    ["rahim@gmail.com", "karim@gmail.com", "rahman@gmail.com"],
    [10000, 20000, 30000],
]
print(persons)
print(persons[0])
print(persons[0][0])
print(persons[0][1])
print(persons[0][2])
print(persons[1])
print(persons[1][0])
print(persons[1][1])
print(persons[1][2])
print(persons[2])
print(persons[2][0])
print(persons[2][1])
print(persons[2][2])

"""
Home work

My name is ....., I am .... years old. I get ...... tk per month. My email adderess is ..... 
"""

print(
    f"My name is {persons[0][0]}. I am {persons[1][0]} years old. I get {persons[3][0]} TK per month. My email address is {persons[2][0]}"
)
print(
    f"My name is {persons[0][1]}. I am {persons[1][1]} years old. I get {persons[3][1]} TK per month. My email address is {persons[2][1]}"
)
print(
    f"My name is {persons[0][2]}. I am {persons[1][2]} years old. I get {persons[3][2]} TK per month. My email address is {persons[2][2]}"
)

print("=========================")

demo_variable = [[1, 2, 3], [4, 5, 6, 0], [7, 8, 9]]
for row in range(len(demo_variable)):
    for col in range(len(demo_variable[row])):
        print(demo_variable[row][col], end="")
    print(end="\n")
