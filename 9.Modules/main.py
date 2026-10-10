import utils as student_utils

marks = [85, 78, 92, 67, 88]
total = student_utils.total(marks)
average = student_utils.average(marks)
grade = student_utils.grade(average)
status = student_utils.status(grade)
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
print(f"Status: {status}")

print("\n--- Analytics ---")
max_mark = student_utils.find_max(marks)
min_mark = student_utils.find_min(marks)
average_mark = student_utils.calculate_average(marks)
grades = [student_utils.grade(mark) for mark in marks]
print(f"Maximum Mark: {max_mark}")
print(f"Minimum Mark: {min_mark}")
print(f"Average Mark: {average_mark:.2f}")
print(f"Passed Students: {student_utils.count_passed(grades)}")
print(f"Failed Students: {student_utils.count_failed(grades)}")