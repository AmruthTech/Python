# # Part 1 — Strings
# # 1. Take a string from the user and print its length without using len().
# n = input()
# count = 0
# for i in n:
#     count += 1
# print(count)

# # 2. Take a person's full name and print:
# # First character
# # Last character
# # First 3 characters
# # Last 3 characters
# name = input()
# print(name[0])
# print(name[-1])
# print(name[:3])
# print(name[-3:])

# # 3. Take a string and count the number of vowels in it.
# n = input()
# vowel = 0
# for i in n:
#     if i in "aeiouAEIOU":
#         vowel += 1
# print(vowel)

# # 4. Take a string and count separately:
# # Uppercase letters
# # Lowercase letters
# # Digits
# # Spaces
# n = input()
# low = 0
# up = 0
# digit = 0
# space = 0
# for i in n:
#     if i.islower():
#         low += 1
#     elif i.isupper():
#         up += 1
#     elif i.isdigit():
#         digit += 1
#     elif i == " ":
#         space += 1
# print(f"upper: {up} \nlower: {low} \ndigit: {digit} \nspace: {space}")

# # 5. Take a sentence and count how many words it contains.
# sentence = input()
# words = sentence.split(" ")
# count = 0
# for i in words:
#     if i.isalpha():
#         count += 1
# print(count)

# # 6. Take a string and reverse it using slicing.
# # Example:
# # Input: Python
# # Output: nohtyP
# n = input()
# print(n[::-1])

# # 7. Check whether a string is a palindrome using string slicing.
# # Input: madam
# # Output: Palindrome
# n = input()
# if n == n[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# # 8. Take a sentence and replace every space with _.
# # Input: Python is awesome
# # Output: Python_is_awesome
# n = input()
# n = n.replace(" ", "_")
# print(n)

# # 9. Take a sentence and print each word on a separate line.
# n = input()
# n = n.split(" ")
# for i in n :
#     print(i)

# # 10. Take a string and find the frequency of a particular character entered by the user.
# # Example:
# # Input: programming
# # Character: g
# # Output: 2
# n = input()
# char = input()
# print(n.count(char))

# # Part 2 — String Functions and Comprehension
# # 11. Take a string containing unnecessary spaces and clean it using appropriate string methods.
# # Example:
# # Input: "   Python Programming   "
# # Output: "Python Programming"
# n = input()
# print(n.strip())

# # 12. Take an email address and determine whether it looks valid using basic string operations.
# # At minimum, check that it contains:
# # @
# # .
# # text before @
# mail = input()
# for i in mail:
#     if "@" in mail and "." in mail:
#         print("valid")
#         break
#     else:
#         print("Invalid")
#         break

# # 13. Take a sentence and convert it into:
# # lowercase
# # uppercase
# # title case
# n = input()
# print(n.lower())
# print(n.upper())
# print(n.title())

# # 14. Take a sentence and count the frequency of every word.
# # Example:
# # Input: python is easy and python is powerful
# # python → 2
# # is → 2
# # easy → 1
# # and → 1
# # powerful → 1
# n = input()

# # 15. Use list comprehension to create a list containing the lengths of every word in a sentence.
# # Input: Python is very powerful
# # Output: [6, 2, 4, 8]
# n = input()
# n = n.split(" ")
# [print(len(i), end = ", ") for i in n]

# # 16. Use list comprehension to extract all vowels from a string.
# n = input()
# [print(i) for i in n if i in "AEIOUaeiou" ]

# # 17. Use list comprehension to create a list containing only the digits from a mixed string.
# # Input: "a1b2c3d4"
# # Output: ['1', '2', '3', '4']
# n = input()
# [print(str(i), end = ", ") for i in n if i.isdigit()]

# # 18. Take a sentence and create a list containing only words whose length is greater than 4.
# sen = input()
# li = []
# for i in sen.split(" "):
#     if len(i) > 4:
#         li.append(i)
# print(li)

# # 19. Take a string and create a new string where every vowel is replaced with *.
# n = input()
# for i in n:
#     if i in "AEIOUaeiou":
#         n = n.replace(i, "*")
# print(n)

# # 20. Take a sentence and find the longest word without using max().
# n = input()
# high = ""
# for curr in n.split(" "):
#     if len(curr) > len(high):
#         high = curr
# print(high)

12, 14, 15, 17 problems