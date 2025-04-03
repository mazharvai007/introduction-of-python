days_of_weeks = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}

number = int(input("Enter a number between (1-7): "))

if number >= 1 and number <= 7:
    print(days_of_weeks[number])
else:
    print("Invalid Input")
