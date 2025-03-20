number_of_rows = int(input("Enter a number: "))

if number_of_rows >= 1:
    for row_num in range(1, number_of_rows + 1, 1):
        for col_num in range(1, row_num + 1):
            if col_num % 3 == 0 and col_num % 5 == 0:
                print("FizzBuzz", end=" ")
            elif col_num % 3 == 0:
                print("Fizz", end=" ")
            elif col_num % 5 == 0:
                print("Buzz", end=" ")
            else:
                print(col_num, end=" ")
        print(end="\n")
else:
    print("You should enter a number that greater than 1")

print("-------------")

"""
Change the condition for that number divisible by 3 and 5. 3 x 5 = 15.
"""
if number_of_rows >= 1:
    for row_num in range(1, number_of_rows + 1, 1):
        for col_num in range(1, row_num + 1):
            if col_num % 15 == 0: # this condition can make the program running time complexity O(n)
                print("FizzBuzz", end=" ")
            elif col_num % 3 == 0:
                print("Fizz", end=" ")
            elif col_num % 5 == 0:
                print("Buzz", end=" ")
            else:
                print(col_num, end=" ")
        print(end="\n")
else:
    print("You should enter a number that greater than 1")
