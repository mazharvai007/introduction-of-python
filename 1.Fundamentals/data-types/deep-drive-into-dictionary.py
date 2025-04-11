"""
Dictionary Methods:

- get(key, default_value)
- keys()
- values()
- items()
- update(dictionary)
- setdefault(key, default_value)
- pop(key, default_value)
- del
- clear
- unpack(**) -> {**variable_name}
"""

dc = {
    "name": "Salman",
    "age": 35,
    "profession": "Student",
    "email": "salman@gmail.com",
}

# get(key, default_value)

# print(dc["email"])  # It will throw key error

print(dc.get("email", "example@gmail.com"))
print(dc)

print("=====================")

# keys()

get_keys = dc.keys()  # provided keys in a list
print(get_keys)

print("-----------------")

# Approach 1
keys_list = list(get_keys)  # convert keys as a list
print(keys_list)

print("-----------------")

# Approach 2
print(list(dc.keys()))  # convert keys as a list

print("=====================")

# values()

dc_values = dc.values()
print(dc_values)

print("-----------------")

# Approach 1 - convert values of list to a list
print(list(dc_values))

# Approach 2 - get all values in a list
print(list(dc.values()))

print("=====================")

# items()

print(dc.items())  # provides a list of tuple

print("-----------------")

# Iterate dictionary
for item in dc.items():
    print(item)  # provides tuple

print("-----------------")

for key, value in dc.items():
    print(key, ":", value)

print("=====================")

# update(dictionary)
update_dc = {
    "bio": "This is a bio",
    "expertise": "Technical Support / WordPress / Joomla / Python / Django",
}

dc.update(update_dc)

print(dc)

print("=====================")

# setdefault(key, default_value)
set_default_value = dc.setdefault("university", "UAP")
print("Set Default Value:", set_default_value)
print("Main Dictionary:", dc)

print(dc.get("university"))

print("-----------------")

# Check key in dictionary and update
if "city" in dc:
    dc["city"] = "Dhaka"
else:
    dc.setdefault("city", "Dhaka")

print(dc)

# pop(key, default_value)
get_pop = dc.pop("bio")
print(get_pop)

print(dc)
# del - use it to delete enter dictionary
# del dc

# print(dc)

# clear

dc.clear()

print(dc)

print("=====================")

# unpack(**) -> {**variable_name}

dc1 = {**dc}  # the dc1 is unpacked by the {**variable}

dc1["name"] = "Nahid"

print(dc)
print(dc1)
