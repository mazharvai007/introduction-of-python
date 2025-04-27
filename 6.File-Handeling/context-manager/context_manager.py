# Context Manager


# State 1 - Know about Context manager
class MyContext:
    def __init__(self) -> None:
        print("Constructor")

    def __enter__(self):
        print("Enter")

    def __exit__(self, a, b, c):
        print("Exit")


with MyContext() as ctx:
    print(f"Here {ctx}")


# Stage 2 - Real time implementation
class MyFileContext:
    def __init__(self, filename, mode) -> None:
        print("Constructor")
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("Context Generate")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Context tear done")
        self.file.close()


with MyFileContext(filename="demo.txt", mode="r") as file:
    # Operational part
    content = file.read()
    print(content)


# Implementation of Python
with open("demo.txt", "r") as file:
    print(file.read())
