"""
String - is the collection of characters
Each character of a string starts from 0 index

- slice()
- upper()
- lower()
- capitalize()
- strip()
- replace(old, new)
- format()
    - with placeholder
    - without placeholder
- find()
- split()
- join()
- startswith()
- endswith()
- isdigit()
- isalpha()
- isspace()
"""

# ------------------------------------
# -5 | -4 | -3 | -2 | -1     # -index
# ------------------------------------
# H  | E  | L  | L  | O     # string
# ------------------------------------
# 0  | 1  | 2  | 3  | 4     # index
# ------------------------------------

from os import name


demo = "HELLO"
print(demo[0])
print(demo[1])
print(demo[2])
print(demo[3])
print(demo[4])

print("-----------------------------")

print(demo[-1])  # O
print(demo[-2])  # L
print(demo[-3])  # L
print(demo[-4])  # E
print(demo[-5])  # H

print("-----------------------------")

print(len(demo))  # length 5

print("==============================")

# String Iteration

for character in demo:
    print(character)

print("-----------------------------")

for index in range(0, len(demo)):
    print(demo[index])

print("==============================")

# Slice
str_slice = "Funny"

start = 0
stop = 3
skip = 2

print(str_slice[start:stop])
print(str_slice[-4:-1])

another_str_slice = "I am a big fan of Python"
print(another_str_slice[2:8])
print(another_str_slice[2:15])
print(another_str_slice[2:15:1])
print(another_str_slice[start:stop:skip])

print("==============================")

# Upper
print(str_slice.upper())

print("==============================")

# Lower
print(another_str_slice.lower())

print("==============================")

# Capitalize
capital_case = "capital case"
print(capital_case.capitalize())

# Case insensitive condition checking
# email = "abc@gmail.com"
# user_input = input("Enter your email: ")

# print(email.lower() == user_input.lower())
# print(email.upper() == user_input.upper())
# print(email.capitalize() == user_input.capitalize())

# Strip
print("    Hello    ".strip())
print("    Hello    Python    ".strip())

str_strip = "------------Hello-----------"
result = str_strip.strip("-")
print(result)

# String Immutability
sentence = "English is a good language. I do not know English."
print(sentence)
result = sentence.replace("English", "Python")  # the str.replace() gives a new data
print(result)

result = str_slice[0] + "P" + str_slice[2:]
print(result)

# String Formatting
username = "Nahid"
greet = f"Hello, Welcome to {username}"
print(greet)

# format() - without placeholder
str_with_out_placeholder = "Hello {}, how are you? Your age is {}"
greet = str_with_out_placeholder.format("Nahid", 20)

print(greet)

# String formatting with placeholder
"""
Dear {name},
We are excited to invite you to the {event} on {date}.
Location: {location}
We hope to see you there!

Best Regards
The Event Team

"""


def send_email(default="en"):
    if default == "en":
        email_body = """
            Dear {name},
            We are excited to invite you to the {event} on {date}.
            Location: {location}
            We hope to see you there!

            Best Regards
            The Event Team
        """
    elif default == "bn":
        email_body = """
            প্রিয় {name},
            আমরা আপনাকে {event} এ আমন্ত্রণ জানাতে পেরে আনন্দিত যা {date} তারিখে অনুষ্ঠিত হবে।

            স্থানঃ {location}

            আমরা আশা করি আপনি সেখানে আসবেন।

            শুভেচ্ছান্তে
            ইভেন্ট টিম
        """

    return email_body.format(
        name="John Doe",
        event="Python Summit 25",
        date="15 April, 2025",
        location="Hotel Marriot",
    )


print(send_email("bn"))
