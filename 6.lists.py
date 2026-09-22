# # Part 3 — Lists

# # 21. Create a list of 10 numbers and print:
# # Length
# # First element
# # Last element
# # Maximum
# # Minimum
# # Sum
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(len(li))
# print(li[0])
# print(li[-1])
# high = 0
# for i in li:
#     if i > high:
#         high = i
# print(high)
# low = high
# for i in li:
#     if i < low:
#         low = i
# print(low)
# sum = 0
# for i in li:
#     sum += i
# print(sum)

# # 22. Take 10 numbers from the user and store them in a list. Print only the even numbers.
# li = list(map(int, input().split(" ")))
# for i in li:
#     if i % 2 == 0:
#         print(i, end=" ")

# # 23. Take a list of numbers and create another list containing their squares.
# li = list(map(int, input().split(" ")))
# l1 = []
# for i in li:
#     i = i**2
#     l1.append(i)
# print(l1)


# # 24. Take a list and reverse it using slicing.
# li = list(map(int, input().split(" ")))
# print(li[::-1])

# # 25. Given:
# #   numbers = [10, 20, 30, 40, 50, 60, 70]
# #   Print:
# #   First 3 elements
# #   Last 3 elements
# #   Elements from index 2 to 5
# #   Every second element
# #   Reversed list
# numbers = [10, 20, 30, 40, 50, 60, 70]
# print(numbers[:3])
# print(numbers[-3:])
# print(numbers[2:6])
# print(numbers[1::2])
# print(numbers[::-1])

# 26. Given a list of numbers, count how many times a particular number occurs without using .count().
# li = list(map(int, input().split(" ")))


# # 27. Find the largest number in a list without using max().
# li = list(map(int, input().split(" ")))
# high = 0
# for i in li:
#     if i > high:
#         high = i
# print(high)

# # 28. Find the second-largest number in a list.
# li = list(map(int, input().split(" ")))
# li.sort()
# print(li[-2])


# # 29. Remove duplicate values from a list while preserving the original order.
# # Example:
# # Input: [10, 20, 10, 30, 20, 40]
# # Output: [10, 20, 30, 40]
# Input = [10, 20, 10, 30, 20, 40]
# ori = []
# for i in Input:
#     if i not in ori:
#         ori.append(i)
# print(ori)



# # 30.Take a list of numbers and create three separate lists:
# # positive numbers
# # negative numbers
# # zeroes
# l1 = list(map(int, input().split(" ")))
# positive = []
# negative = []
# zeros = []
# for i in l1:
#     if i > 0:
#         positive.append(i)
#     elif i < 0:
#         negative.append(i)
#     elif i == 0:
#         zeros.append(i)
#     else:
#         print("invalid")
# print(positive)
# print(negative)
# print(zeros)





# # Part 4 — List Comprehension + Problem Solving
# # 31. Using list comprehension, create a list of squares of numbers from 1 to 20.
# n = [i**2 for i in range(1, 21)]
# print(n)

# # 32. Using list comprehension, create a list of all numbers between 1 and 100 that are divisible by both 3 and 5.
# n = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
# print(n)

# # 33. Given:
# # names = ["Rahul", "Priya", "Amit", "Sneha", "John"]
# # Create a new list containing names whose length is greater than 4.
# names = ["Rahul", "Priya", "Amit", "Sneha", "John"]
# new = [i for i in names if len(i) > 4]
# print(new)


# # 34. Given:
# # marks = [45, 78, 91, 32, 67, 88, 29]
# # Create a list containing "PASS" or "FAIL" for each mark.
# marks = [45, 78, 91, 32, 67, 88, 29]
# status = ["PASS" if i > 35 else "FAIL" for i in marks]
# print(status)


# # 35. Given a list of numbers, create a new list where:
# # Even numbers become their squares.
# # Odd numbers remain unchanged.
# num = list(map(int, input().split()))
# even_sq = [i**2 if i % 2 == 0 else i for i in num]
# print(even_sq)

# # 36. Take a sentence, split it into words, and create a list containing the first character of every word.
# # Input: "Python Data Analytics"
# # Output: ['P', 'D', 'A']
# sen = input()
# words = sen.split()
# for i in words:
#     for j in i:
#         print(i[0], end = ",")
#         break

# # 37. Given two lists:
# # names = ["Rahul", "Priya", "Amit"]
# # marks = [85, 92, 76]
# # create a list of strings:
# # Rahul scored 85
# # Priya scored 92
# # Amit scored 76
# names = ["Rahul", "Priya", "Amit"]
# marks = [85, 92, 76]
# for i in range(len(names)):
#     print(f"{names[i]} scored {marks[i]}")


# # 38. Given a list of numbers, create a new list containing only numbers that are greater than the average of the list.
# l1 = list(map(int, input().split()))
# sum1 = 0
# for i in l1:
#     sum1 += i
# avg = sum1 / len(l1)
# l2 = [i for i in l1 if i > avg]
# print(l2)

# # 39. Take a list of strings and create a list containing the strings that are palindromes.
# l1 = list(map(str, input().split()))
# l2 = [i for i in l1 if i == i[::-1]]
# print(l2)


# # 40. Given a list of student marks, create a list of grades using list comprehension.
# # Rules:
# # >= 90 → A
# # >= 80 → B
# # >= 70 → C
# # >= 60 → D
# # < 60  → F
# marks = list(map(int, input().split()))
# grades = ["A" if i >= 90 else
#         "B" if i >= 80 and i < 90 else
#         "C" if i >= 70 and i < 80 else
#         "D" if i >= 60 and i < 70 else
#         "F" if i < 60 else
#         "Invalid"
#         for i in marks]
# print(grades)

26 problem