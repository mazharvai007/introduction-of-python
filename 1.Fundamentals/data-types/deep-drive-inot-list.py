"""
List methods:

- slice
- len()
- append(value)
- extend(list)
- insert(index, value)
- remove(value) --> first occurrence
- pop()
- pop(index)
- clear()
- enumerate()
- index(value) --> first occurrence
- count(value)
- sort()
- reverse()
- unpack(*variable) -> [*variable_name]

# Reference URL: https://colab.research.google.com/drive/12tUElYT3wZidZ2u1LLgvl5-PYr6M3INA?usp=sharing
"""

# slice
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
get_slice = ls[2:7]
print(get_slice)

# len()
print(len(ls))

# append(value)
ls.append(100)
print(ls)

# extend(list)
ls1 = [10, 20, 30]
ls2 = [50, 60, 70]

ls1.extend(ls2)
print(ls1)

# insert(index, value)
ls2.insert(0, 40)
print(ls2)

ls1.insert(0, 5)
print(ls1)

# remove(value) --> first occurrence
ls1.remove(60)
print(ls1)

if 70 in ls1:
    ls1.remove(70)

print(ls1)

# pop()
ls1.pop()

# pop(index)
ls1.pop(1)

# clear()
ls1.clear()
print(ls1)

# enumerate()
for index, value in enumerate(ls):
    print(f"Index - {index} | Value - {value}")

# index(value) --> first occurrence
ls.index(5)
ls.index(10)

# count(value)
ls1 = ["Mango", "Banana", "Lichy", "Mango", "Apple"]
ls1.count("Mango")
ls.count(100)

# sort()
ls1.sort()
print(ls1)

# reverse()
ls.reverse()
print(ls)

ls3 = [{"name": "Rafiq"}, {"name": "Jabbar"}, {"name": "Kite"}, {"name": "Abrar"}]
ls3.reverse()
print(ls3)

# unpack()
unpack_ls1 = [1, 2, 3]
unpack_ls2 = unpack_ls1

unpack_ls2[0] = 100

print(unpack_ls1)
print(unpack_ls2)

print(id(unpack_ls1))
print(id(unpack_ls2))

# applies unpack
unpack_ls3 = [*unpack_ls1]  # the unpack_ls1 is unpacked by [*variable]
unpack_ls3[1] = 500

print(unpack_ls1)
print(unpack_ls2)
print(unpack_ls3)

print(id(unpack_ls1))
print(id(unpack_ls2))
print(id(unpack_ls3))

print(*["a", "b"])  # behind the scene will be print("a", "b")
