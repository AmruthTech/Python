# Mini Project — Student Marks & Performance Analyzer

# Build a console-based Student Performance Analyzer using only the concepts you've learned so far.

# Do not use functions, dictionaries, classes, NumPy, Pandas, or other libraries yet. The point of this project is to force you to use the fundamentals properly.

# Requirements

# The program should first ask:

# Enter number of student:
n = int(input("How many student: "))

# For each student, collect:

# Student name:
# Math marks:
# Science marks:
# English marks:
# Store the information using lists.
Students = {}
for _ in range(n):
    key = input("enter Student ID: ")
    val_len = int(input("Enter how many values: "))
    if val_len > 0:
        Students[key] = {}
        for _ in range(val_len):
            key1 = input("enter key: ").title()
            val = int(input("Enter how many values: "))
            if val > 0:
                if val == 1 and (key1 == "Course" or key1 == "course"):
                    Students[key][key1] = list(map(str, input("Courses: ").title().split()))
                elif val == 1:
                    Students[key][key1] = input(f"enter {key1} value: ").title()
                else:
                    Students[key][key1] = {}
                    for _ in range(val):
                        key2 = input("Enter key: ")
                        Students[key][key1][key2] = int(input(f"Enter {key2} value: "))

# Students["Totals"] = 100
for i in Students.keys():
    sum = 0
    for j in Students[i]["Marks"]:
        sum += Students[i]["Marks"][j]
        # print(Students[i]["Marks"][j])
    Students[i]["Total"] = sum
    Students[i]["Average"] = sum/len(Students[i]["Marks"])

    avg = Students[i]["Average"]
    if avg >= 90:
        Students[i]["Grades"] = "A"
    elif avg >= 80 and avg < 90:
        Students[i]["Grades"] = "B"
    elif avg >= 70 and avg < 80:
        Students[i]["Grades"] = "C"
    elif avg >= 60 and avg < 70:
        Students[i]["Grades"] = "D"
    elif avg < 60:
        Students[i]["Grades"] = "F"

    if Students[i]["Marks"]["Maths"] < 40 or Students[i]["Marks"]["Science"] < 40 or Students[i]["Marks"]["English"] < 40:
        Students[i]["Status"] = "FAIL"
    else:
        Students[i]["Status"] = "PASS"

for i in Students:
    print(i)
    for j in Students[i].items():
        print(j)
        # print("")
        for k in Students[i][j].items():
            print(k)
        # print("")
    print("")

# hl = {"S001": {"marks": {"math": 12, "sci": 21}}}
# print(hl["S001"]["marks"].values())

# # For every student, calculate:
# totals = []
# averages = []
# grades = []
# status = []
# # Total marks
# # Average marks


# for i in range(n):
#     total = mathsMarks[i] + scienceMarks[i] + englishMarks[i]
#     totals.append(total)
#     average = totals[i]/3
#     averages.append(average)

# # Pass/Fail status
# # A student is considered Fail if they score below 40 in any individual subject, regardless of their average.
#     if mathsMarks[i] < 40 or scienceMarks[i] < 40 or englishMarks[i] < 40:
#         status.append("FAIL")
#     else:
#         status.append("PASS")

# # Grade
# # Use these grading rules:

# # Average >= 90  → A
# # Average >= 80  → B
# # Average >= 70  → C
# # Average >= 60  → D
# # Average < 60   → F

#     if averages[i] >= 90:
#         grades.append("A")
#     elif averages[i] >= 80 and averages[i] < 90:
#         grades.append("B")
#     elif averages[i] >= 70 and averages[i] < 80:
#         grades.append("C")
#     elif averages[i] >= 60 and averages[i] < 70:
#         grades.append("D")
#     elif averages[i] < 60:
#         grades.append("F")





# # Then calculate class-level statistics:

# # Total student
# Total_student = n


# # Additional requirements
# Pass = 0
# Fail = 0
# A, B, C, D, F = 0, 0, 0, 0, 0

# for i in range(n):
# # Number of student passed
#     if status[i] == "PASS":
#         Pass += 1
# # Number of student failed
#     else:
#         Fail += 1

# # Number of A grades
# # Number of B grades
# # Number of C grades
# # Number of D grades
# # Number of F grades
#     if grades[i] == "A":
#         A += 1
#     elif grades[i] == "B":
#         B += 1
#     elif grades[i] == "C":
#         C += 1
#     elif grades[i] == "D":
#         D += 1
#     elif grades[i] == "F":
#         F += 1


# # Class average
# cls_average = 0
# for i in averages:
#     cls_average += i
# cls_average = cls_average / n

# # Highest average
# high_avg = 0
# for curr_avg in averages:
#     if curr_avg > high_avg:
#         high_avg = curr_avg

# # Lowest average
# low_avg = high_avg
# for curr_avg in averages:
#     if curr_avg < low_avg:
#         low_avg = curr_avg

# # Add a simple menu:

# # 1. Display all student
# # 2. Display class statistics
# # 3. Find highest-performing student
# # 4. Find lowest-performing student
# # 5. Search for a student
# # 6. Exit
# while True:
#     Choose_menu = int(input("""# 1. Display all student
#     # 2. Display class statistics
#     # 3. Find highest-performing student
#     # 4. Find lowest-performing student
#     # 5. Search for a student
#     # 6. Exit\n"""))
#     if Choose_menu == 1:
#         # Your program should finally display
#     # ===== STUDENT PERFORMANCE REPORT =====

#     # Name: Rahul
#     # Math: 85
#     # Science: 78
#     # English: 91
#     # Total: 254
#     # Average: 84.67
#     # Grade: B
#     # Status: PASS
#     # Repeat this for every student.
#         print("===== STUDENT PERFORMANCE REPORT =====")
#         for i in range(n):
#             print(f"Name: {student[i]} \nMaths: {mathsMarks[i]} \nScience: {scienceMarks[i]} \nEnglish: {englishMarks[i]} \nTotal: {totals[i]} \nAverage: {averages[i]:.2f} \nGrade: {grades[i]} \nStatus: {status[i]}\n")

#     elif Choose_menu == 2:
#         print("CLASS REPORT ANALYSIS")
#         print(f"Pass student: {Pass}\nFail student: {Fail} \nA Grade Count: {A} \nBGrade Count: {B} \nC Grade Count: {C} \nD Grade Count: {D} \nF Grade Count: {F}")
#         print(f"Class Average: {cls_average} \nHighest Average: {high_avg} \nLowest Average: {low_avg}")

#     elif Choose_menu == 3:
#         print(f"Highest Average: {high_avg}")
#     elif Choose_menu == 4:
#         print(f"Lowest Average: {low_avg}")
#     elif Choose_menu == 5:
#         i = int(input("Enter student number (Starts with 0): "))
#         print(f"Name: {student[i]} \nMaths: {mathsMarks[i]} \nScience: {scienceMarks[i]} \nEnglish: {englishMarks[i]} \nTotal: {totals[i]} \nAverage: {averages[i]:.2f} \nGrade: {grades[i]} \nStatus: {status[i]}\n")
#     elif Choose_menu == 6:
#         break

# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# The menu should keep running until the user chooses 6.

# Use a while loop for the menu.

# Use for loops when processing the student data.

# Use if/elif/else for grades and pass/fail decisions.

# Use break when exiting the menu.

# Use continue where it makes logical sense—for example, when searching through student and skipping student whose names don't match.

# Stretch challenges

# Once the basic project works, add these without changing the overall approach:

# Prevent marks below 0 or above 100.
# If the user enters invalid marks, ask them to enter the marks again.
# Allow the user to add more student after the initial list has been created.
# Display the top 3 student based on average.

# Display the subject-wise class average:

# Mathematics Average: 76.4
# Science Average: 72.8
# English Average: 81.2
# Find the subject in which the class performed best.
# Find the subject in which the class performed worst.
# Display a simple performance bar using *:
# Rahul  : ********
# Priya  : *********
# Amit   : ******
