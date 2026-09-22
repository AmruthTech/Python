# # Part 5 — Tuples
# # 41. Create a tuple containing information about a student:
# # name
# # age
# # city
# # course
# # Access each value individually.
# tup = ("Amar", 22, "Karimnagar", "DS")
# for i in range(len(tup)):
#     print(tup[i])

# # 42. Given:
# # numbers = (10, 20, 30, 40, 50, 60)
# # print:
# # First 3 elements
# # Last 3 elements
# # Reversed tuple
# # Every second element
# numbers = (10, 20, 30, 40, 50, 60)
# print(numbers[:3])
# print(numbers[-3:])
# print(numbers[::-1])
# print(numbers[1::2])


# # 43. Take 5 numbers from the user, store them in a tuple, and calculate their:
# # Sum
# # Average
# # Maximum
# # Minimum
# tup = tuple(map(int, input().split()))
# add = sum(tup)
# avg = add / len(tup)
# high = max(tup)
# low = min(tup)
# print(add, avg, high, low)

# # 44. Given a tuple:
# # numbers = (10, 20, 10, 30, 20, 10, 40)
# # find the frequency of 10 without using .count().
# numbers = (10, 20, 10, 30, 20, 10, 40)
# count = 0
# for i in numbers:
#     if i == 10:
#         count += 1
# print(count)


# # 45. Given a tuple of student records:
# # student = (
# #     ("Rahul", 85),
# #     ("Priya", 92),
# #     ("Amit", 76)
# # )
# # iterate through the tuple and print each student's name and marks.
# student = (
#     ("Rahul", 85),
#     ("Priya", 92),
#     ("Amit", 76)
# )
# for i in student:
#     print(f"{i[0]} scored {i[1]}")


# Part 6 — Dictionaries

# a = {}
# for i in range(1, 16):
#     a[i] = i**2
# print(a)
# a = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
# for i in a:
#     print(a[i])


# # 46. Create a dictionary representing a student:
# # name
# # age
# # course
# # city
# # marks
# # Perform the following:
# # Access values
# # Add a new key
# # Modify an existing value
# # Delete a key
# # Check whether a key exists
# a = {"name": "Amar", "age": 22, "course": "data science", "city": "Hyderabad", "marks": 81.5}
# print(a.values())
# a["grade"] = "A"
# a["city"] = "Karimnagar"
# a.pop("course")
# for i in a.keys():
#     if i == "age":
#         print(a[i])
# print(a)


# # 47. Given:
# # marks = {
# #     "Rahul": 85,
# #     "Priya": 92,
# #     "Amit": 76,
# #     "Sneha": 89
# # }
# # Find:
# # Highest marks
# # Lowest marks
# # Average marks
# # Student with highest marks
# marks = {
#     "Rahul": 85,
#     "Priya": 92,
#     "Amit": 76,
#     "Sneha": 89
# }
# high = 0
# for i in marks.values():
#     if i > high:
#         high = i
# print(high)
# low = high
# for i in marks.values():
#     if i < low:
#         low = i
# print(low)
# sum = 0
# for i in marks.values():
#     sum += i
# avg = sum/len(marks)
# print(avg)
# high = 0
# for i in marks.keys():
#     if marks[i] > high:
#         high = marks[i]
#         name = i
# print(name, high)


# 48. Count word frequency using a dictionary.
# Input:
# "python is easy python is powerful"
# Output:
# {
#     "python": 2,
#     "is": 2,
#     "easy": 1,
#     "powerful": 1
# }
a = "python is easy python is powerful"



# # 49. Create a nested dictionary representing multiple student:
# student = {
#     "S001": {
#         "name": "Rahul",
#         "math": 85,
#         "science": 78,
#         "english": 91
#     },
#     "S002": {
#         "name": "Priya",
#         "math": 92,
#         "science": 88,
#         "english": 95
#     }
# }
# # Write code to:
# # Print all student
# # Print Rahul's Math marks
# # Calculate each student's average
# # Find the highest-performing student
# # print(student)
# # print(student["S001"]["math"])
# sum = 0
# for i in student.keys():
#     print(i)
#     for j in i.keys():
#         print(j)
#         if i[j].isdigit():
#             sum += i[j]
#     avg = sum/3
#     print(avg)



# # 50. Create a set from a list containing duplicate values. Then perform operations to find:
# # Unique values
# # Union of two sets
# # Intersection
# # Difference
# # Symmetric difference
# # Example:
# a = {10, 20, 30, 40}
# b = {30, 40, 50, 60}
# # Determine the result of each set operation.
# a = a.union(b)
# b.intersection_update(a)
# c = a.difference(b)
# c1 = b.difference(a)
# d = b.symmetric_difference(a)
# print(a, b, c, c1, d)
