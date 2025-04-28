from datetime import datetime
from time import sleep


def task1():
    print("Task 1 started")
    sleep(2)
    print("Task 1 completed")


def task2():
    print("Task 2 started")
    sleep(3)
    print("Task 2 completed")


def task3():
    print("Task 3 started")
    print("Task 3 completed")


print(datetime.now())
task1()
task2()
task3()
print(datetime.now())
