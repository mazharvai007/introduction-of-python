import asyncio
from datetime import datetime
from asyncio import sleep


# Defining and calling async function
# async def task1():
#     print("Task 1 started")
#     await sleep(2)
#     print("Task 1 completed")


# async def task2():
#     print("Task 2 started")
#     await sleep(3)
#     print("Task 2 completed")


# async def task3():
#     print("Task 3 started")
#     print("Task 3 completed")


# async def call_my_function():
#     print(datetime.now())
#     await task1()
#     await task2()
#     await task3()
#     print(datetime.now())


# print("Hiiiiiiiiiiiiiiiiiiiiiiiiiiii")
# asyncio.run(call_my_function())
# print("Byeeeeeeeeeeeeeeeeeeeeeeeeee")


async def task1():
    print("Task 1 started")
    await sleep(2)
    print("Task 1 completed")

    return 1


async def task2():
    print("Task 2 started")
    await sleep(3)
    print("Task 2 completed")

    return 2


async def task3():
    print("Task 3 started")
    print("Task 3 completed")

    return None


async def call_my_function():
    print(datetime.now())
    # await task1()
    # await task2()
    # await task3()

    # Solution 1
    # await asyncio.gather(task1(), task2(), task3())

    # Solution 2
    tasks = [task1(), task2(), task3()]
    res = await asyncio.gather(*tasks)
    print(res)

    print(datetime.now())


print("Hiiiiiiiiiiiiiiiiiiiiiiiiiiii")
asyncio.run(call_my_function())
print("Byeeeeeeeeeeeeeeeeeeeeeeeeee")
