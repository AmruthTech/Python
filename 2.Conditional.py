# # Level 2 — Operators and Conditional Statements

# # 11. Take a number as input and determine whether it is positive, negative, or zero.
# num = int(input())
# if num > 0:
#     print("Positive Number")
# elif num < 0:
#     print("Negative Number")
# else:
#     print("Zero")

# # 12. Take an integer and determine whether it is even or odd.
# num  = int(input())
# if num % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")

# # 13. Take two numbers and print which number is greater. If they are equal, print "Both are equal".
# num1 = int(input())
# num2 = int(input())
# if num1 == num2:
#     print("Both are equal")
# elif num1 > num2:
#     print(f"{num1} is Greater")
# else:
#     print(f"{num2} is Greater")

# # 14. Take three numbers and find the largest number using conditional statements.
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# if num1 > num2:
#     if num1 > num3:
#         print(f"{num1} is Largest")
#     else:
#         print(f"{num3} is Largest")
# elif num2 > num3:
#     if num2 > num1:
#         print(f"{num2} is Largest")
#     else:
#         print(f"{num1} is Largest")
# else:
#     print(f"{num3} is Largest")


# # 15. Take a student's marks and assign grades using the following rules:
# # 90–100 → A
# # 80–89 → B
# # 70–79 → C
# # 60–69 → D
# # Below 60 → F
# marks = int(input())
# if marks >= 90 and marks <= 100:
#     print("Grade A")
# elif marks >= 80 and marks < 90:
#     print("Grade B")
# elif marks >= 70 and marks < 80:
#     print("Grade C")
# elif marks >= 60 and marks < 70:
#     print("Grade D")
# elif marks >=0 and marks < 60:
#     print("Grade F")
# else:
#     print("Invalid Marks")

# # 16. Take a person's age and determine whether they are eligible to vote. Assume the minimum age is 18.
# age = int(input())
# if age >= 18 and age <110:
#     print("Eligible to vote")
# elif age >= 0 and age < 18:
#     print("Not Eligible to vote")
# else:
#     print("Please enter valid age between 0 and 110")

# # 17. Take a number and determine whether it is divisible by both 3 and 5.
# num = int(input())
# if num % 3 == 0 and num % 5 == 0:
#     print(f"{num} is divisible by both 3 and 5")
# elif num % 3 == 0:
#     print(f"{num} is only divisible by 3")
# elif num % 5 == 0:
#     print(f"{num} is only divisible by 5")
# else:
#     print(f"{num} is not divible by 3 and 5")

# # 18. Take a year as input and determine whether it is a leap year.
# year = int(input())
# if year > 0:
#     if year % 4 == 0 and year % 100 != 0:
#         print(f"{year} is a Leap year")
#     elif year % 400 == 0:
#         print(f"{year} is a Leap year")
#     else:
#         print(f"{year} is a non-leap year")
# else:
#     print("Invalid year")

# # 19. Take three sides of a triangle and determine whether they can form a valid triangle.
# a = int(input("Enter side of a Triangle: "))
# b = int(input("Enter side of a Triangle: "))
# c = int(input("Enter side of a Triangle: "))
# if a > 0 and b > 0 and c > 0:
#     if (a+b >= c) and (b+c >= a) and (c+a >= b):
#         print(f"{a}, {b}, {c} sides forms a Triange")
#     else:
#         print(f"{a}, {b}, {c} sides doesn't form a Triange")
# else:
#     print("Enter valid sides")

# # 20. Take a student's marks in Mathematics, Science, and English.
# # Calculate the average and determine whether the student has passed.
# # A student must score at least 40 in every subject and have an average of at least 50.
# maths = int(input())
# sci = int(input())
# english = int(input())
# average = (maths + sci + english) / 3
# print(average)
# if maths >= 40 and sci >= 40 and english >= 40 and average >= 50:
#     print("Student has passed")
# else:
#     print("Student has not passed")

# # 21. Create a simple calculator. Take two numbers and an operator (+, -, *, /) as input and perform the corresponding calculation.
# num1 = int(input())
# num2 = int(input())
# opt = input("Enter +, -, *, / for calculation: ")
# if opt == '+':
#     print(num1 + num2)
# elif opt == '-':
#     print(num1 - num2)
# elif opt == '*':
#     print(num1 * num2)
# elif opt == '/':
#     print(num1 / num2)
# else:
#     print("Enter valid inputs")

# # 22. Take a person's salary and calculate tax:
# # Salary ≤ ₹2,50,000 → No tax
# # ₹2,50,001–₹5,00,000 → 5%
# # ₹5,00,001–₹10,00,000 → 20%
# # Above ₹10,00,000 → 30%
# salary = int(input())
# if salary > 0 and salary <= 250000:
#     print("No tax")
# elif salary > 250000 and salary <= 500000:
#     print(f"{salary * 0.05 :.2f} tax")
# elif salary > 500000 and salary <= 1000000:
#     print(f"{salary * 0.2 :.2f} tax")
# elif salary > 1000000:
#     print(f"{salary * 0.3 :.2f} tax")
# else:
#     print("Invalid salary")

# # 23. Take a number and determine whether it is a two-digit number, three-digit number, or neither.
# num = int(input())
# if len(str(abs(num))) == 2:
#     print(f"{num} is a 2-digit number")
# elif len(str(abs(num))) == 3:
#     print(f"{num} is a 3-digit number")
# else:
#     print(f"{num} is neither")

# # 24. Take a character as input and determine whether it is a vowel or consonant.
# n = input()
# if n in 'AEIOUaeiou':
#     print(f"{n} is vowel")
# else:
#     print(f"{n} is consonant")

# # 25. Take the purchase amount from a customer and calculate the discount:
# # Below ₹1,000 → No discount
# # ₹1,000–₹4,999 → 10%
# # ₹5,000–₹9,999 → 20%
# # ₹10,000 or more → 30%
# # Print the original amount, discount, and final amount.
# amt = int(input())
# dis = 0
# if amt >= 10000:
#     dis = amt * 0.3
#     print(f"Original: {amt}, Discount: {dis}, Total Bill: {amt-dis}")
# elif amt < 10000 and amt >= 5000:
#     dis = amt * 0.2
#     print(f"Original: {amt}, Discount: {dis}, Total Bill: {amt-dis}")
# elif amt < 5000 and amt >= 1000:
#     dis = amt * 0.1
#     print(f"Original: {amt}, Discount: {dis}, Total Bill: {amt-dis}")
# else:
#     print(f"Original: {amt}, Discount: {dis}, Total Bill: {amt-dis}")