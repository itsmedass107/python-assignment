def analyze_result(name, roll_no, marks):

    total = sum(marks)
    avg = total / 5

    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    elif avg >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print("Student:", name, "(Roll no:", roll_no, ")")
    print("Total:", total,"," "(Average:", avg, ")")
    print("Grade:", grade)

    print("Subjects below 40:")

    for i in range(5):
        if marks[i] < 40:
            print("Subject", i + 1)


name = "Nikhil Dass"
roll_no = 107
marks = [88, 35, 76, 92, 48]

analyze_result(name, roll_no, marks)
