# # Level 3 — For Loops

# # 26. Print the numbers from 1 to 100 using a for loop.
# for i in range(1, 101):
#     print(i)

# # 27. Print all even numbers between 1 and 50.
# for i in range(0,51,2):
#     print(i)

# # 28. Print all odd numbers between 1 and 100.
# for i in range(1,100, 2):
#     print(i)

# # 29. Take a number n from the user and calculate the sum of all numbers from 1 to n.
# n = int(input())
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print(sum)

# # 30. Take a number from the user and print its multiplication table from 1 to 10.
# n = int(input())
# for i in range(1,11):
#     print(f"{n}x{i}={n*i}")

# # 31. Take a number n and calculate its factorial using a for loop.
# n = int(input())
# fact = 1
# for i in range(n):
#     fact = fact * (i+1)
# print(fact)

# # 32. Count how many numbers between 1 and 100 are divisible by 7.
# count = 0
# for i in range(1, 101):
#     if i % 7 == 0:
#         count += 1
# print(count)

# # 33. Take 10 numbers from the user and calculate their sum and average.
# num = list(map(int, input().split()))
# sum = 0
# count = 0
# for i in num:
#     sum += i
#     # if i.isdigit():
#     #     count += 1
# avg = sum / 10
# print(sum, avg)

# # 34. Take 10 numbers from the user and count how many are positive, negative, and zero.
# num = list(map(int, input().split()))
# positive = 0
# negative = 0
# zero = 0
# for i in num:
#     if i > 0:
#         positive += 1
#     elif i < 0:
#         negative += 1
#     else:
#         zero += 1
# print(f"Positive: {positive}, Negative: {negative}, Zero: {zero}")

# # 35. Take a number from the user and print all its factors.
# num = int(input())
# for i in range(1, num+1):
#     if num % i == 0:
#         print(i, end = " ")

# # 36. Take a number and determine whether it is prime.
# num = int(input())
# count = 0
# for i in range(1, num+1):
#     if num % i == 0:
#         count += 1
# if count > 2:
#     print(f"{num} is not a prime")
# else:
#     print(f"{num} is a prime")

# # 37. Print all prime numbers between 1 and 100.
# for n in range(1, 101):
#     count = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             count += 1
#     if count == 2:
#         print(n, end=" ")


# # 38. Take a number n and calculate the sum of all even numbers and the sum of all odd numbers from 1 to n.
# num = int(input())
# even = 0
# odd = 0
# for i in range(1, num+1):
#     if i % 2 == 0:
#         even += i
#     else:
#         odd += i
# print(even, odd)

# # 39. Take a number from the user and reverse its digits using a loop.
# num = int(input())
# num = str(num)
# rev = ""
# for i in num:
#     rev = i+rev
# print(rev)

# # 40. Take a number from the user and determine whether it is a palindrome.
# num = int(input())
# num = str(num)
# rev = ""
# for i in num:
#     rev = i+rev
# print(rev)
# if num == rev:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")