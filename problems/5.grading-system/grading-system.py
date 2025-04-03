# Get marks from users
bangla = int(input("Enter Bangla Marks: "))
english = int(input("Enter English Marks: "))
math = int(input("Enter Math Marks: "))
science = int(input("Enter Science Marks: "))
religious = int(input("Enter Religious Marks: "))
social = int(input("Enter social Marks: "))

# Addition all marks
total_marks = bangla + english + math + science + religious + social

# Total subjects
total_subject = 6

# get average marks from the totals marks divided by the total subject
grand_total = int(total_marks / total_subject)

# Get Student Grade
if (
    (bangla >= 0 and bangla <= 100)
    and (english >= 0 and english <= 100)
    and (math >= 0 and math <= 100)
    and (science >= 0 and science <= 100)
    and (religious >= 0 and religious <= 100)
    and (social >= 0 and social <= 100)
):
    if grand_total >= 81 and grand_total <= 100:
        print("You got: A+")
    elif grand_total >= 61 and grand_total <= 80:
        print("You got: A")
    elif grand_total >= 51 and grand_total <= 60:
        print("You got: B")
    elif grand_total >= 41 and grand_total <= 50:
        print("You got: C")
    elif grand_total >= 33 and grand_total <= 40:
        print("You got: D")
    else:
        print("You are: Failed")
else:
    print("Invlid Marks")
