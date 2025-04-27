"""
File Handeling:

Syntax:
f = open(filename, mode)

#Operation on 'f' based on mode
f.close()

# mode
- read
- write
- append
"""

file_name = "file_handling.txt"
file_open = open(file_name, "r")
content = file_open.read()
# content = file_open.readline()
# content = file_open.readlines()
print(content)

# f = open(file_name, "w")
# f.write("The file is reading\n")
# f.write("We are reading\n")
# f.close()

file_open.close()
