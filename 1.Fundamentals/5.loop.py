"""
Loop

- For Loop
A range of input

- While Loop
start =
end =
condition =
step

break - When a condition meets the requirement, then the break will work.
ex. If I want to break the loop after reaching my condition the loop will be break

continue - Skip the current iteration that will not fulfill the requirement
pass - If we do not have any statement, then we can use the pass to avoid the error

start, end, condition, step - the four steps are essential for any kind of loops
"""

# For Loop
# numberOfCases = int(input("Enter a value: "))

# for value in range(numberOfCases):
#     num1= int(input("Num1: "))
#     num2 = int(input("Num2: "))
#     result = num1 + num2
#     print(result)

# While Loop
# start = 1
# end = numberOfCases
# step = 1
#
# while start <= end:
#
#     num1= int(input("Num1: "))
#     num2 = int(input("Num2: "))
#     result = num1 + num2
#     print(result)
#
#     start += step

# Break
# for value in range(numberOfCases):
#     if value == 2:
#         print("Condition is fulfill")
#         break

# Continue
# myList = [1, 2, 3, 4, 5, 10]

# for value in myList:
#     if value % 2 != 0:
#         continue
#     else:
#         print(value)
        
# Pass        

# For Statements

# Measure some stings:
words = ["Cat", "Dog", "Window", "King", "Mazhar"]
for word in words:
    print(word, len(word))
    
# Create a sample collection
users = {"Halim": "active", "Hana": "inactive", "Omer": "active"}

# Strategy: Iterate over a copy
inactive_users = {}
for user, status in users.copy().items():
    if status == "inactive":
        inactive_users[user] = status
        del users[user]

# print(inactive_users)
# print(users) 
    
# Strategy: Crate a new collection
active_users = {}
for user, status in users.items():
    if status == "active":
        active_users[user] =  status
        
# print(active_users) 

"""
range() function
"""

# If we do need to iterate over a sequence of numbers, we can use built-in range() function that comes handy. It will generate arithmetic progressions

for i in range(5):
    print(i)

# The given end point is never part of the generated sequence; range(10) will generate 10 values, the legal indices for items of a sequence of length 10. It is possible to let the range start at another number, or to specify a different increment (even negative sometimes this is called "steps")
list1 = list(range(5, 10))
print(list1)

list2 = list(range(0, 10, 3))
print(list2)
  
list3 = list(range(-10, -100, -30))
print(list3)

# To iterate over the indices of a sequence, we can combine range() and len() functions
text_list = ["Kamal", "had", "a", "little", "lamb"]
for i in range(len(text_list)):
    print(i, text_list[i])

for i in enumerate(text_list):
    print(i)

increment = 1
while increment <= 10:
    print(increment)
    increment += 1

# my_string = "Learning Python"
my_string = "abcd"
for s in enumerate(my_string):
    print(s)

x = 0
while len(my_string) != x:
    print(my_string[x])
    # my_string = my_string[1:]
    # print(my_string)

    x += 1

# print(len(my_string))

# Step 1: x = 0, len(my_string) = 4, 0 != 4, print(mystring[0]) = a, x = 1
# Step 2: x = 1, len(my_string) = 4, 1 != 4, print(mystring[1]) = b, x = 2
# Step 3: x = 2, len(my_string) = 4, 2 != 4, print(mystring[2]) = c, x = 3
# Step 4: x = 3, len(my_string) = 4, 3 != 4, print(mystring[3]) = d, x = 4
# Step 5: x = 4, len(my_string) = 4, 4 != 4 // while the condition is false, then the iteration is closed.

# Break
for i in range(1, 11, 2):
    if i == 5:
        break
    print(i)

for i in range(1, 11, 1):
    if i == 4 or i == 9:
        continue
    print(i)

print("-------------")

# Nested Loop
for i in range(10):
    print("For i:", i)
    for j in range(2):
        print("For j:", j)

# Iteration of the loop
# Step 1: i: 0, j: 0, 1
# Step 2: i: 1, j: 0, 1
# Step 3: i: 2, j: 0, 1
# Step 4: i: 3, j: 0, 1
# Step 5: i: 4, j: 0, 1
# Step 6: i: 5, j: 0, 1
# Step 7: i: 6, j: 0, 1
# Step 8: i: 7, j: 0, 1
# Step 9: i: 8, j: 0, 1
# Step 10: i: 9, j: 0, 1

print("-------------")

# 1
# 22
# 333
# 4444
# 55555

row = 5
for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(i, end="")
    print(end="\n")

# Iteration of the loop
