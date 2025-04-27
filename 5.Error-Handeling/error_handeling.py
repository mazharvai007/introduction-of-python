from typing import Dict


def process_entity(person: Dict):
    cal = person["salary"] / person["tax"]
    return cal


p = {"salary": 10000, "tax": 10}
print("Before")

try:
    # print(process_entity(person=p))

    val = process_entity(person=p)
    print(val)
except ZeroDivisionError as error:
    print(error)
except KeyError as error:
    print(KeyError)
except ValueError as error:
    print(error)
except Exception as error:
    print(error)
print("After")
