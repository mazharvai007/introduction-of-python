number_of_students = int(input("Enter Number of Students: "))
print(
    f"We will calculate the grade for {number_of_students} {"student" if number_of_students == 1 else "students"} "
)

total_subjects = 11


# Subjects for Science Group
def science_subjects() -> int:
    """
    Enter marks for All science subjects: Physics, Chemistry, Biology, and Higher Math
    """

    physics_marks = check_marks(int(input("Enter marks for Physics: ")), "Physics")
    chemistry_marks = check_marks(
        int(input("Enter marks for Chemistry: ")), "Chemistry"
    )
    biology_marks = check_marks(int(input("Enter marks for Biology:")), "Biology")
    higher_math_marks: int = check_marks(
        int(input("Enter marks for Higher Math: ")), "Higher Math"
    )

    return physics_marks + chemistry_marks + biology_marks + higher_math_marks


# Subjects for Commerce Group
def commerce_subjects() -> int:
    """
    Enter marks for all Commerce subjects: Finance, Accounting, Business studies & entity
    """

    finance_banking_marks = int(input("Enter marks for Finance & Banking: "))
    accounting_marks = int(input("Enter marks for Accounting: "))
    business_studies_entity_marks = int(
        input("Enter marks for Business Studies & Entity: ")
    )

    return finance_banking_marks + accounting_marks + business_studies_entity_marks


# Subjects for Arts Group
def arts_subjects() -> int:
    """
    Enter marks for all Arts subjects: Geography, Civic & Citizenship, and Economics
    """

    geography_marks = int(input("Enter marks for Geography: "))
    civic_citizenship_marks = int(input("Enter marks for Civic & Citizenship: "))
    economics_marks = int(input("Enter marks for Economics: "))

    return geography_marks + civic_citizenship_marks + economics_marks


# Common subjects for all students
def common_subjects() -> int:
    """
    Enter marks all common subjects: Bangla (1st, 2nd), English (1st, 2nd), Math, Religion, ICT, and General science for Commerce and Arts students
    """

    bangla_first_paper_marks = check_marks(
        int(input("Enter marks for Bangla 1st paper: ")), "Bangla 1st paper"
    )
    bangla_second_paper_marks = check_marks(
        int(input("Enter marks for Bangla 2nd paper: ")), "Bangla 2nd paper"
    )
    english_first_paper_marks = check_marks(
        int(input("Enter marks for English 1st paper: ")), "English 1st Paper"
    )
    english_second_paper_marks = check_marks(
        int(input("Enter marks for English 2nd paper: ")), "English 2nd Paper"
    )
    math_marks = check_marks(int(input("Enter marks for Math: ")), "Math")
    religion_marks = check_marks(int(input("Enter marks for Religion: ")), "Religion")
    ict_marks: int = check_marks(int(input("Enter marks for ICT: ")), "ICT")

    general_science_marks = 0
    if study_group == "Commerce" or study_group == "Arts":
        general_science_marks = check_marks(
            int(input("Enter marks for General Science: ")), "General Science"
        )

    return (
        bangla_first_paper_marks
        + bangla_second_paper_marks
        + english_first_paper_marks
        + english_second_paper_marks
        + math_marks
        + religion_marks
        + ict_marks
        + general_science_marks
    )


# Check Marks between 0 and 100
def check_marks(marks: int, subject_name: str):
    """
    We check the marks here. If users entered marks less then 0 or greater then 100 this will throw the error
    """

    if not (0 <= marks <= 100):
        print(
            f"You entered invalid marks {marks} for {subject_name}. The marks must be between 0 and 100"
        )
        return int(input(f"Enter marks for {subject_name}: "))
    return marks


# Get Final Result including average and grade
def final_result(student_name: str, study_group: str, *subjects):

    marks1 = subjects[0]
    marks2 = subjects[1]

    average_marks = (marks1 + marks2) // total_subjects
    grade = "nothing"

    if average_marks >= 81 and average_marks <= 100:
        grade = "A+"
    elif average_marks >= 61 and average_marks <= 80:
        grade = "A"
    elif average_marks >= 51 and average_marks <= 60:
        grade = "B"
    elif average_marks >= 41 and average_marks <= 50:
        grade = "C"
    elif average_marks >= 33 and average_marks <= 40:
        grade = "D"
    else:
        grade = "Failed"

    print(
        f"\nStudent Name: {student_name}\nExam: SSC\nGroup: {study_group}\nAverage Marks: {average_marks} \nGrade: {grade}\n"
    )


# The loop will work based on the students number
for value in range(1, number_of_students + 1, 1):
    student_name = input(f"Enter Student {value} Name: ")
    study_group = input("Enter your Study Group (Science/Commerce/Arts): ")

    if study_group == "Science" or study_group == "science":
        final_result(student_name, study_group, common_subjects(), science_subjects())
    elif study_group == "Commerce" or study_group == "commerce":
        final_result(student_name, study_group, common_subjects(), commerce_subjects())
    elif study_group == "Arts" or study_group == "arts":
        final_result(student_name, study_group, common_subjects(), arts_subjects())
    else:
        print("Are not you a student?")
