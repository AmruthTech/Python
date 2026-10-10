# Part 7 — Modules

# 49. Create your own module called:
# student_utils.py
# Put functions such as:
# calculate_total()
# calculate_average()
# calculate_grade()
# calculate_status()
# inside it.
# Then create:
# main.py
# and import your module.
# Your main.py should use those functions to calculate a student's result.
def total(marks):
    return sum(marks)

def average(marks):
    return sum(marks) / len(marks) if marks else 0

def grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "D"

def status(grade):
    return "Passed" if grade != "D" else "Failed"   

# 50. Create a small utility module called:
# analytics_utils.py
# with functions for:
# find_max()
# find_min()
# calculate_average()
# count_passed()
# count_failed()
def find_max(marks):
    return max(marks) if marks else None

def find_min(marks):
    return min(marks) if marks else None

def calculate_average(marks):
    return sum(marks) / len(marks) if marks else 0

def count_passed(grades):
    return grades.count("A") + grades.count("B") + grades.count("C")

def count_failed(grades):
    return grades.count("D")

# Then import the module into another Python file and use the functions with your Student Performance Analyzer data.