ls = [10, 1, 25, 75, 30, 15]
print(ls)

"""
Sort
- Ascending order (From smaller to larger)
- Descending order (From larger to smaller)
"""

# Sorting a list - Ascending order
as_sort = sorted(ls)
print(as_sort)

print("==============================")

# Sorting a list - Descending order - Approach 1
desc_list = reversed(sorted(ls))
rev_list = list(desc_list)
print(rev_list)

print("==============================")

# Sorting a list - Descending order - Approach 2
new_ls = sorted(ls, reverse=True)
print(new_ls)

# Sort based on sort key
# person_list = [
#     {"name": "Jahin", "age": 5},
#     {"name": "John", "age": 25},
#     {"name": "Khan", "age": 15},
#     {"name": "Jahan Ali", "age": 18},
# ]

person_list = [("Jahin", 12), ("Karim", 5), ("Rafiq", 18), ("Kamal", 22)]

SORT_KEY = 1
for item in person_list:
    # print(item["age"])
    print(item[SORT_KEY])

print(person_list)


print("==============================")

# Get sort key value
new_list = [
    ("Sakib", 40000, 25),
    ("Jahin", 50000, 20),
    ("Kamal", 43000, 18),
    ("Rafiq", 15000, 15),
]


def get_sort_key_value(ls, key):
    for item in ls:
        print(item[key])


get_sort_key_value(ls=new_list, key=2)

print("==============================")

# sorted list - based on name
lambda_list = sorted(new_list, key=lambda new_list: new_list[0])
print(lambda_list)

print("==============================")

# sorted list - based on salary
reverse_lambda_list = sorted(new_list, key=lambda new_list: new_list[1], reverse=True)
print(reverse_lambda_list)

print("==============================")

# sorted list - based on age
reverse_lambda_list = sorted(new_list, key=lambda new_list: new_list[2], reverse=False)
print(reverse_lambda_list)
