print('spam eggs')
print("Paris rabbit got your back :)! Yay!")
print('1975')

print("-------")

# To quote a quote, we need to escape it by preceding it with a backslash (\). Alternatively, we can use double quotes to quote a single quote.
print('doesn\'t')
print("doesn't")
print('"Yes," they said.')
print("\"Yes,\" they said.")
print('"Isn\'t," they said.')

string = 'First line, \nSecond line.'
print(string)

print("-------")

# If you don't want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:
print('C:\some\name')
print(r'C:\some\name')

print("-------")

# String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. End of lines are automatically included in the string, but it's possible to prevent this by adding a \ at the end of the line.
print("""\
    Usage: thingy [OPTIONS]
    -h                        Display this usage message
    -H hostname               Hostname to connect to
    """)

print("-------")

# Strings can be concatenated (glued together) with the + operator, and repeated with *:
print(3 * 'un' + 'ium'
      )
print('Py' 'thon')

print("-------")

# This only works with two literals though, not with variables or expressions:
prefix = 'Py'
# prefix 'thon'
# ('un' * 4)  'ium'

# If you want to concatenate variables or a variable and a literal, use +:
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

print(prefix + 'thon')

print("-------")

# Strings can be indexed (subscripted), with the first character having index 0. There is no separate character type; a character is simply a string of size one:
word = "Python"
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[5])

print("-------")

# Indices may also be negative numbers, to start counting from the right:
print(word[-1])
print(word[-2])
print(word[-3])
print(word[-4])
print(word[-5])
print(word[-6])

print("-------")

# In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters, slicing allows you to obtain substring:
print(word[0:2])
print(word[0:4])
print(word[2:5])

print("-------")

# Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.
print(word[:2])
print(word[:5])
print(word[2:])
print(word[4:])
print(word[-2:])
print(word[:-2])

print("-------")

# Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s:
print(word[:2] + word[2:])
print(word[:4] + word[4:])

print("-------")

# Attempting to use an index that is too large will result in an error:
# print(word[7])

# print("-------")

# However, out of range slice indexes are handled gracefully when used for slicing:
print(word[4:42])
print(word[42:])

print("-------")

# Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string results in an error:
# print(word[0] = "J")
print(word[0] == "J")
# print(word[2:] = "Jy")
print(word[2:] == "Jy")
print(word[2:] == "py")
print(word[2:] == "Py")
print(word[2:] == "thon")

print("-------")

# If you need a different string, you should create a new one:
print("J" + word[1:])
print(word[:2] + "Py")
print(word[:2] + "Jy")

print("-------")

# The built-in function len() returns the length of a string:
print(len(word))