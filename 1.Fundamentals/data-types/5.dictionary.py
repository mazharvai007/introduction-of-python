man1 = {"name": "Mazhar", "age": 30, "email": "mazhar@gmail.com"}

man2 = {"name": "Abdullah", "age": 5, "email": "abdullah@gmail.com"}

print(man1["name"])
print(man2["age"])

print("-----------------")

"""
persons = [
    ["Rahim", "Karim", "Rahman"],
    [25, 30, 35],
    ["rahim@gmail.com", "karim@gmail.com", "rahman@gmail.com"],
    [10000, 20000, 30000]
]
"""

person1 = {"name": "Rahim", "age": 25, "email": "rahim@gmail.com", "salary": 10000}

person2 = {"name": "Karim", "age": 30, "email": "karim@gmail.com", "salary": 20000}

person3 = {"name": "Rahman", "age": 35, "email": "rahman@gmail.com", "salary": 30000}

print(
    f"My name is {person1["name"]}, I am {person1["age"]} years old. I get {person1["salary"]} tk per month. My email address is {person1["email"]} "
)
print(
    f"My name is {person2["name"]}, I am {person2["age"]} years old. I get {person2["salary"]} tk per month. My email address is {person2["email"]} "
)
print(
    f"My name is {person3["name"]}, I am {person3["age"]} years old. I get {person3["salary"]} tk per month. My email address is {person3["email"]} "
)

print("-----------------")

"""
Student:
1. Name
2. roll
3. class
4. school
"""

student1 = {"name": "Hasib", "roll": "01", "class": "10", "school": "ABC High School"}

student2 = {"name": "Jasim", "roll": "02", "class": "10", "school": "ABC High School"}

student3 = {"name": "John", "roll": "03", "class": "10", "school": "ABC High School"}

"""
Value Access
Syntax
"""

# Approach 1: dictionary_name["key_name"]
print(student1["name"])
print(student1["roll"])
print(student1["class"])
print(student1["school"])

print("-----------------")

# Approach 2: dictionary_name.get("key_name")
print(student2.get("name"))
print(student2.get("roll"))
print(student2.get("class"))
print(student2.get("school"))

# What is the difference between both approach
# print(student3.get("father_name")) # None
# print(student3["father_name"]) # Throwing KeyError and the key does not get in the dictionary

print("-----------------")

# List of Dictionary
persons = [
    {"name": "Karim", "age": 30, "email": "karim@gmail.com", "salary": 20000},
    {"name": "Karim", "age": 30, "email": "karim@gmail.com", "salary": 20000},
    {"name": "Rahman", "age": 35, "email": "rahman@gmail.com", "salary": 30000},
]

# Access key with values based on the index number
print(persons)
print(persons[0])
print(persons[0]["name"])
print(persons[0].get("name"))

print("-----------------")

# Dictionary with List
author = {
    "author": "Maurice Sendak",
    "born": "Maurice Bernard Sendak, June 10, 1928, Brooklyn, New York, U.S.",
    "died": "May 8, 2012 (aged 83), Danbury, Connecticut, U.S.",
    "occupation": ["Artist", "Illustrator", "Writer"],
    "genre": ["Children's literature", "picture", "books"],
    "books": [
        "Where the Wild Things Are",
        "Chicken Soup with Rice: A Book of Months",
        "In the Night Kitchen",
        "Pierre: A Cautionary Tale in Five Chapters and a Prologue",
        "Outside Over There",
        "Nutshell Library: Alligators all around / Chicken Soup With Rice / One was Johnny / Pierre",
        "Alligators All Around",
        "Higglety Pigglety Pop! or There Must Be More to Life",
        "One Was Johnny: A Counting Book",
        "My Brother's Book",
    ],
    "children": [
        {"name": "Maurice 1", "age": 15},
        {"name": "Maurice 2", "age": 20},
        {"name": "Maurice 3", "age": 25},
    ],
}
author_name = author.get("author")
author_born = author["born"]
author_died = author["died"]

author_occupation = author["occupation"]
author_occupation1 = author["occupation"][0]
author_occupation2 = author["occupation"][1]
author_occupation3 = author["occupation"][2]

author_genre = author.get("genre")
author_genre1 = author.get("genre")[0]
author_genre2 = author.get("genre")[1]
author_genre3 = author.get("genre")[2]

author_books = author.get("books")

author_children = author.get("children")

author_children1 = author.get("children")[0]
author_children1_name = author.get("children")[0]["name"]
author_children1_age = author.get("children")[0].get("age")

author_children2 = author.get("children")[1]
author_children2_name = author.get("children")[1].get("name")
author_children2_age = author.get("children")[1].get("age")

author_children3 = author.get("children")[2]
author_children3_name = author.get("children")[2]["name"]
author_children3_age = author.get("children")[2].get("age")

print("Name:", author_name)
print("Born:", author_born)
print("Died:", author_died)

print("Occupation:", author_occupation)
print("Occupation 1:", author_occupation1)
print("Occupation 2:", author_occupation2)
print("Occupation 3:", author_occupation3)

print("Genre:", author_genre)
print("Genre 1:", author_genre1)
print("Genre 2:", author_genre2)
print("Genre 3:", author_genre3)

print("Books:", author_books)

print("Children's:", author_children)

print("Children 1:", author_children1)  # type: ignore
print("Children 1 Name:", author_children1_name)
print("Children 1 Age:", author_children1_age)

print("Children 2:", author_children2)
print("Children 2 Name:", author_children2_name)
print("Children 2 Age:", author_children2_age)

print("Children 3:", author_children3)
print("Children 3 Name:", author_children3_name)
print("Children 3 Age:", author_children3_age)

print("-----------------")

company = {
    "mobile_operator": {
        "grameen_phone": {"services": ["2G", "3G", "4G"]},
        "teletalk": {"services": ["2G", "3g"]},
    }
}

companies = company.get("mobile_operator")
print(companies)

grameen_phone = company.get("mobile_operator").get("grameen_phone")
print(grameen_phone)

grameen_phone = company.get("mobile_operator").get("grameen_phone").get("services")
print(grameen_phone)

tele_talk = company.get("mobile_operator").get("teletalk")
print(tele_talk)

tele_talk = company.get("mobile_operator").get("teletalk").get("services")
print(tele_talk)
