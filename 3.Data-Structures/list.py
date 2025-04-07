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
