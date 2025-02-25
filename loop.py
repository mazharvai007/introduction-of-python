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
myList = [1, 2, 3, 4, 5, 10]

for value in myList:
    if value % 2 != 0:
        continue
    else:
        print(value)
        
# Pass        