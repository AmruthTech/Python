# # 41. Use a while loop to print numbers from 1 to 20.
# n = 1
# while n <= 20:
#     print(n, end=" ")
#     n += 1

# # 42. Use a while loop to repeatedly ask the user for a number. Stop when the user enters 0. At the end, print the sum of all previously entered numbers.
# arr = []
# while True:
#     num = int(input())
#     if num == 0:
#         break
#     arr.append(num)
# sum = 0
# for i in arr:
#     sum += i
# print(sum)

# # 43. Create a password program. Keep asking the user for a password until they enter the correct password. Once correct, print "Access Granted".
# password = "12345"
# while True:
#     enter = input()
#     if password == enter:
#         print("Access Granted")
#         break

# # 44. Create a number guessing program. Store a secret number, repeatedly ask the user to guess it, and print:
# # "Too high"
# # "Too low"
# # "Correct"
# # Stop when the user guesses correctly.
# sec = "12345"
# while True:
#     guess = input()
#     if len(sec) == len(guess):
#         print("Too High")
#         if sec == guess:
#             print("Correct")
#             break
#     else:
#         print("Too low")

# # 45. Print the following pattern using nested loops:
# # *
# # **
# # ***
# # ****
# # *****
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print("*", end = " ")
#     print()

# # 46. Print this pattern:
# # 1
# # 12
# # 123
# # 1234
# # 12345
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end = " ")
#     print()

# # 47. Print a multiplication table from 1 to 10 using nested loops.
# # Example:
# # 1 2 3 4 ... 10
# # 2 4 6 8 ... 20
# # ...
# # 10 20 30 ... 100
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end=",")
#     print()

# # 48. Print numbers from 1 to 100, but:
# # Skip numbers divisible by 3 using continue
# # Stop completely when the number reaches 80 using break
# while True:
#     for i in range(1,101):
#         if i % 3 == 0:
#             continue
#         print(i)
#         if i == 80:
#             break

# # 49. Take 10 numbers from the user. If the user enters a negative number, stop taking inputs immediately using break. Otherwise, calculate the sum of the entered numbers.
# arr = []
# while True:
#     num = int(input())
#     if num < 0:
#         break
#     arr.append(num)
# # print(arr)
# print(sum(arr))

# # 50. Create a program that keeps accepting numbers until the user enters -1. At the end, display:
# # Total numbers entered
# # Sum
# # Average
# # Largest number
# # Smallest number
# # Number of even values
# # Number of odd values
# arr = []
# while True:
#     num = int(input())
#     if num == -1:
#         break
#     arr.append(num)
# print("Answers:")
# print(arr)
# print(sum(arr))
# count = 0
# for i in arr:
#     count += 1
# print(sum(arr)/count)
# print(max(arr))
# print(min(arr))
# even = 0
# odd = 0
# for i in arr:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(even)
# print(odd)