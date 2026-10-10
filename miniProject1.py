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
    key = input("enter Student ID: ").title().strip()
    val_len = int(input("Enter how many values: "))
    if val_len > 0:
        Students[key] = {}
        for _ in range(val_len):
            key1 = input("enter key: ").title().strip()
            val = int(input("Enter how many values: "))
            if val > 0:
                if val == 1 and (key1 == "Course" or key1 == "course"):
                    Students[key][key1] = list(map(str, input("Courses: ").title().split(",")))
                elif val == 1:
                    Students[key][key1] = input(f"enter {key1} value: ").title().strip()
                else:
                    Students[key][key1] = {}
                    for _ in range(val):
                        key2 = input("Enter key: ").title().strip()
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

cities = set()
for id in Students:
#     for city in Students[id]["City"]:
    if Students[id]["City"] not in cities:
        cities.add(Students[id]["City"])
print("Cities: ", cities)


courses = set()
for id in Students:
    for cour in Students[id]["Course"]:
        if cour not in courses:
            courses.add(cour)
print("Courses: ", courses)

subjects = []
for id in Students:
    for marks in Students[id]:
        for subs in Students[id]["Marks"]:
            subjects.append(subs)
        break
    break
subjects = tuple(list(subjects))
print("Subjects: ", subjects)

grade = []
for id in Students:
    if Students[id]["Grades"] in "ABCDF":
        grade.append(Students[id]["Grades"])
grades = tuple(grade)
print("Grades: ", grades)

while True:
    choice = input("Enter Operation to execute(Display/ Search/ Update/ Add/ Delete: ").title().strip()
    if choice == "Display":
        print("================================")
        print("STUDENT DETAILS")
        print("================================")
        for i in Students:
            print(f"ID: {i}")
            for j in Students[i]:
                if isinstance(Students[i][j], (str, int, float)):
                    print(f"{j}: {Students[i][j]}")
                elif isinstance(Students[i][j], list):
                    print("")
                    print(f"{j}:")
                    for k in Students[i][j]:
                        print(f"-{k}")
                    print("")
                else:
                    print(f"{j}:")
                    for k in Students[i][j]:
                        print(f"{k}: {Students[i][j][k]}")
                    print("")
            print("---------------------------")
        # break
    elif choice == "Search":
        search = input("Enter Student (ID/Name) to search: ").title().strip()
        if search in Students:
            for j in Students[search]:
                if isinstance(Students[search][j], (str, int, float)):
                    print(f"{j}: {Students[search][j]}")
                elif isinstance(Students[search][j], list):
                    print("")
                    print(f"{j}:")
                    for k in Students[search][j]:
                        print(f"-{k}")
                    print("")
                else:
                    print(f"{j}:")
                    for k in Students[search][j]:
                        print(f"{k}: {Students[search][j][k]}")
                    print("")
            # break
        else:
            for id, name in Students.items():
                if name["Name"] == search:
                    print(f"found!! {id} -> {name}")
            # break
    elif choice == "Update":
        update = input("Enter Student ID: ").title().strip()

        if update in Students.keys():
            enter_update = input(f"Enter what to update in {update}: ").strip().title()
            if enter_update in Students[update]:
                Students[update][enter_update] = input("Updated value: ").title().strip()
                print("Updated Successfully!!!")
                print(Students[update])
            elif enter_update in Students[id]["Marks"]:
                Students[update]["Marks"][enter_update] = int(input("Updated marks: "))
                print(Students[update])
            else:
                print(f"Invalid {enter_update}")
        else:
            print(f"Invalid ID {update}")
    elif choice == "Add":
        n = int(input("How many student: "))
        for _ in range(n):
            key = input("enter Student ID: ").title().strip()
            val_len = int(input("Enter how many values: "))
            if val_len > 0:
                Students[key] = {}
                for _ in range(val_len):
                    key1 = input("enter key: ").title().strip()
                    val = int(input("Enter how many values: "))
                    if val > 0:
                        if val == 1 and (key1 == "Course" or key1 == "course"):
                            Students[key][key1] = list(map(str, input("Courses: ").title().split()))
                        elif val == 1:
                            Students[key][key1] = input(f"enter {key1} value: ").title().strip()
                        else:
                            Students[key][key1] = {}
                            for _ in range(val):
                                key2 = input("Enter key: ").title().strip()
                                Students[key][key1][key2] = int(input(f"Enter {key2} value: "))
    elif choice == "Delete":
        delete_id = input("Enter ID to delete: ").title().strip()
        # for id in Students:
        if delete_id in Students.keys():
            Students.pop(delete_id)
            print("Deleted Successfully!!")
            print(Students)
        else:
            print(f"Invalid ID {delete_id}")
    else:
        print("Exit")
        break

# print(Students)
print("How many students are taking Python?")
python = 0
for i in Students:
    # print(Students[i]["Course"])
    if "Python" in Students[i]["Course"]:
        python += 1
print("Python: ", python)

print("How many students are taking SQL?")
py_sql = 0
for i in Students:
    if "Python" in Students[i]["Course"] and " Sql" in Students[i]["Course"]:
        py_sql += 1
print("Python and SQL: ", py_sql)

print("Which students are taking sql?")
for i in Students:
    if " Sql" in Students[i]["Course"]:
        print(i,"->", Students[i]["Name"])

print("Which students taking sql and python?")
for i in Students:
    if "Python" in Students[i]["Course"] and " Sql" in Students[i]["Course"]:
        print(i,"->", Students[i]["Name"])

print("Which students are taking three or more courses?")
for i in Students:
    if len(Students[i]["Course"]) >= 3:
        print(i,"->", Students[i]["Name"])

print("Get all Students!!")
for i in Students.items():
    print(i)

print("All Students by grade A!!")
for i in Students:
    if Students[i]["Grades"] == "A":
        print(i,"->", Students[i]["Name"])

print("All students with Average above 80!!")
for i in Students:
    if Students[i]["Average"] >= 80:
        print(i,"->", Students[i]["Name"])

print("All Students from Hyderabad")
for i in Students:
    if Students[i]["City"] == "Hyderabad":
        print(i,"->", Students[i]["Name"])


print("----------CLASS ANALYTICS -----------")
print("Total Students")
total = 0
for i in Students:
    total += 1
print(total)

print("Passed Students")
passed = 0
for i in Students:
    if Students[i]["Status"] == "PASS":
        passed += 1
print(passed)

print("Failed Students")
failed = 0
for i in Students:
    if Students[i]["Status"] == "FAIL":
        failed += 1
print(failed)

print("Class Average")
cls_avg = 0
for i in Students:
    cls_avg += Students[i]["Average"]
print(cls_avg/total)

print("Highest Average")
high_avg = 0
for i in Students:
    if Students[i]["Average"] > high_avg:
        high_avg = Students[i]["Average"]
print(high_avg)

print("Lowest Average")
low_avg = high_avg
for i in Students:
    if Students[i]["Average"] < low_avg:
        low_avg = Students[i]["Average"]
print(low_avg)

print("=================")
print("Math Average")
math_avg = 0
for i in Students:
    for mark in Students[i]["Marks"]:
        if mark == "Maths":
            math_avg += Students[i]["Marks"][mark]
print(math_avg/total)

print("Science Average")
sci_avg = 0
for i in Students:
    for mark in Students[i]["Marks"]:
        if mark == "Science":
            sci_avg += Students[i]["Marks"][mark]
print(sci_avg/total)

print("English Average")
eng_avg = 0
for i in Students:
    for mark in Students[i]["Marks"]:
        if mark == "English":
            eng_avg += Students[i]["Marks"][mark]
print(eng_avg/total)

print("====================")
print("Number of A Grade Students")
gradeA = 0
for i in Students:
    if Students[i]["Grades"] == "A":
        gradeA += 1
print(gradeA)

print("Number of B Grade Students")
gradeB = 0
for i in Students:
    if Students[i]["Grades"] == "B":
        gradeB += 1
print(gradeB)

print("Number of C Grade Students")
gradeC = 0
for i in Students:
    if Students[i]["Grades"] == "C":
        gradeC += 1
print(gradeC)

print("Number of D Grade Students")
gradeD = 0
for i in Students:
    if Students[i]["Grades"] == "D":
        gradeD += 1
print(gradeD)

print("Number of F Grade Students")
gradeF = 0
for i in Students:
    if Students[i]["Grades"] == "F":
        gradeF += 1
print(gradeF)

# -----------------------------------------------------------------------------------------------------------------------------------


# {'S001': {'Name': 'Amar', 'City': 'Karimnagar', 'Course': ['Python,', 'Sql,', 'Excel,', 'Bi,', 'Tableau'], 
#          'Marks': {'Maths': 80, 'Science': 65, 'English': 75},'Total': 220, 'Average': 73.33333333333333, 'Grades': 'C', 'Status': 'PASS'}, 
# 'S002': {'Name': 'Mahi', 'City': 'Manchiryal', 'Course': ['Python,', 'Excel,', 'Bi,', 'Tableau'], 
#          'Marks': {'Maths': 80, 'Science': 85, 'English': 90}, 'Total': 255, 'Average': 85.0, 'Grades': 'B', 'Status': 'PASS'}, 
# 'S003': {'Name': 'Anil', 'City': 'Jagityal', 'Course': ['Python,', 'Sql,', 'Bi,', 'Statistics'], 
#          'Marks': {'Maths': 70, 'Science': 65, 'English': 35}, 'Total': 170, 'Average': 56.666666666666664, 'Grades': 'F', 'Status': 'FAIL'}, 
# 'S004': {'Name': 'Raju', 'City': 'Karimnagar', 'Course': ['Python,', 'Sql,', 'Excel,', 'Tableau'], 
#          'Marks': {'Maths': 70, 'Science': 75, 'English': 58}, 'Total': 203, 'Average': 67.66666666666667, 'Grades': 'D', 'Status': 'PASS'}, 
# 'S005': {'Name': 'Nikhila', 'City': 'Hyderabad', 'Course': ['Python,', 'Sql,', 'Bi,', 'Tableau'], 
#          'Marks': {'Maths': 80, 'Science': 95, 'English': 86}, 'Total': 261, 'Average': 87.0, 'Grades': 'B', 'Status': 'PASS'}}



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
