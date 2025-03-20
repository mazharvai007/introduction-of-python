# Print 5 hash in a row
for row in range(0, 5, 1):
    print("#", end="")
print(end="\n")

print("-------")

# Full square shape - 5 x 5 pattern
for row in range(0, 5, 1):
    for col in range(0, 5, 1):
        print("#", end="")
    print(end="\n")

print("-------")

# Right half pyramid
for row in range(0, 5, 1):
    for col in range(row + 1): # When row is 1 the column is 0, that is why, added the 1 in the column condition. now it will print exact #
        print("#", end="")
    print(end="\n")

print("-------")

# Reverse right half pyramid
for row in range(0, 5, 1):
    for col in range(0, 5 - row, 1): # starts from 0 - each iteration the hash will be decreased
        print("#", end="") # number of hash in a row
    print(end="\n") # create new line after each row

print("-------")

# Right pascal's triangle - sideways triangle
for row in range(0, 5, 1):
    for col in range(0, abs(5 - row), 1):
        print("#", end="")
    print(end="\n")