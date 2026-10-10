# Part 1 - Basic Functions

# # 1. Create a function greet() that prints:
# # Hello, welcome to Python!
# def greet():
#     print("Hello, Welcone to Python!")
# greet()

# # 2. Create a function display_name() that accepts a name and prints:
# # Hello Rahul
# def display_name(name):
#     print(f"Hello {name}")
# display_name("Amar")

# # 3. Create a function add_numbers() that accepts two numbers and prints their sum.
# def add_numbers(a, b):
#     print(a+b)
# add_numbers(4, 6)

# # 4. Create a function calculate_area() that accepts length and width and prints the area of a rectangle.
# def calculate_area(len, wid):
#     print("Area of Rectangle:", len*wid)
# calculate_area(2, 4)

# # 5. Create a function is_even() that accepts a number and prints whether it is even or odd.
# def is_even(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# is_even(956)

# # 6. Create a function find_largest() that accepts three numbers and prints the largest number.
# def find_largest(a, b, c):
#     if a > b and a > c:
#         print(f"{a} is greater")
#     elif b > a and b > c:
#         print(f"{b} is greater")
#     else:
#         print(f"{c} is greater")
# find_largest(5,85,54)

# # 7. Create a function calculate_percentage() that accepts marks in three subjects and prints the percentage.
# def calculate_percentage(mat, sci, eng):
#     return (mat + sci + eng) / 3
# print(calculate_percentage(85, 95, 75))

# # 8. Create a function convert_temperature() that accepts Celsius and prints Fahrenheit.
# def convert_temperature(Cel):
#     return (Cel * (9/5)) + 32
# print(int(convert_temperature(24)))

# # 9. Create a function check_voting_eligibility() that accepts age and prints whether the person is eligible to vote.
# def checking_voting_eligibility(age):
#     if age < 18:
#         print("Not Eligible")
#     else:
#         print("Eligible")
# checking_voting_eligibility(15)

# # 10. Create a function print_table() that accepts a number and prints its multiplication table from 1 to 10.
# def print_table(num):
#     for i in range(1, 11):
#         print(f"{num} x {i} = {num*i}")
# print_table(7)


# # Part 2 — Parameters, Arguments and Return
# # 11. Create a function add(a, b) that returns the sum instead of printing it.
# # Then:
# # result = add(10, 20)
# # print(result)
# def add(a, b):
#     return a+b
# result = add(10, 20)
# print(result)

# # 12. Create functions for:
# # addition
# # subtraction
# # multiplication
# # division
# # Each function should return the result.
# def addition (a, b):
#     return a+b
# def subtraction (a, b):
#     return a-b
# def multiplication (a, b):
#     return a*b
# def division(a, b):
#     return a/b
# print(addition(45, 67))
# print(subtraction(108, 85))
# print(multiplication(15, 14))
# print(division(145, 67))

# # 13. Create a function calculate_total(price, quantity) that returns the total bill.
# def calculate_total(price, quantity):
#     return price * quantity
# total = calculate_total(54, 5)
# print(total)

# # 14. Create a function calculate_discount(amount, discount_percent) that returns the discount amount.
# def calculate_discount(amount):
#     if amount > 10000:
#         return amount * 0.2
#     elif amount > 5000:
#         return amount * 0.1
#     elif amount > 2000:
#         return amount * 0.05
#     else:
#         return amount
# discount_amount = calculate_discount(5687)
# print(discount_amount)

# # 15. Create a function final_price(amount, discount) that returns the final price.
# def final_amt(amount):
#     if amount > 10000:
#         return (amount - amount * 0.2)
#     elif amount > 5000:
#         return (amount - amount * 0.1)
#     elif amount > 2000:
#         return (amount - amount * 0.05)
#     else:
#         return amount
# final_amount = final_amt(5687)
# print(final_amount)

# # 16. Create a function is_prime(number) that returns:
# # True
# # or:
# # False
# def is_prime(num):
#     if num == 1:
#         return 1
#     elif num == 2:
#         return "Prime"
#     elif num > 2:
#         for i in range(2, num):
#             if num % 2 == 0:
#                 return "Not prime"
#                 break
#         else:
#             return "Prime"
# num = int(input())
# print(is_prime(num))

# # 17. Create a function factorial(n) that returns the factorial of n.
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(6))

# # 18. Create a function reverse_string(text) that returns the reversed string.
# def reversed_string(str):
#     rev = ""
#     for i in str:
#         rev = i + rev
#     return rev
# print(reversed_string("Amar"))

# # 19. Create a function count_vowels(text) that returns the number of vowels.
# def count_vowels(text):
#     count = 0
#     for i in text:
#         if i in "AEIOUaeiou":
#             count += 1
#     return count
# print(count_vowels("Amruth"))

# # 20. Create a function calculate_student_result(math, science, english) that returns:
# # total
# # average
# # grade
# # status
# # Think carefully about what form you want the returned result to take.
# def calculate_student_result(mat, sci, eng):
#     total = mat + sci + eng
#     print(total)
#     avg = total / 3
#     print(avg)
#     if avg > 90:
#         print("A")
#     elif avg > 80:
#         print("B")
#     elif avg > 70:
#         print("C")
#     else:
#         print("D")

#     if mat < 40 or sci < 40 or eng < 40:
#         print("Fail")
#     else:
#         print("Pass")
# calculate_student_result(85, 65, 49)



# # Part 3 — Functions + Lists/Dictionaries
# # 21. Write a function find_max(numbers) that returns the largest number in a list without using max().
# def find_max(numbers):
#     high = 0
#     for i in numbers:
#         if i > high:
#             high = i
#     return high
# max_val = find_max([25, 68, 34, 25, 92])
# print(max_val)

# # 22. Write a function find_min(numbers) that returns the smallest number without using min().
# def find_min(numbers):
#     low = 100
#     for i in numbers:
#         if i < low:
#             low = i
#     return low
# min_val = find_min([25, 68, 34, 25, 92])
# print(min_val)

# # 23. Write a function calculate_average(numbers) that returns the average of a list.
# def calculate_average(numbers):
#     total = 0
#     for i in numbers:
#         total += i
#     avg = total / len(numbers)
#     return avg
# average = calculate_average([25, 68, 34, 56, 92])
# print(average)

# # 24. Write a function count_even(numbers) that returns the number of even values in a list.
# def count_even(numbers):
#     even = 0
#     for i in numbers:
#         if i % 2 == 0:
#             even += 1
#     return even
# even = count_even([25, 68, 34, 56, 92, 85, 73])
# print(even)

# # 25. Write a function remove_duplicates(numbers) that returns a new list containing unique values while preserving order.
# def remove_duplicates(numbers):
#     new = []
#     for i in numbers:
#         if i not in new:
#             new.append(i)
#     return new
# new_list = remove_duplicates([2, 5, 6, 8, 2, 4, 9, 8, 4])
# print(new_list)

# # 26. Write a function get_passed_students(students).
# # Given:
# students = [
#     {"name": "Rahul", "average": 82},
#     {"name": "Priya", "average": 91},
#     {"name": "Amit", "average": 55}
# ]
# # Return only the students whose average is at least 60.
# def get_passed_students(students):
#     avg = []
#     for i in students:
#         if i["average"] >= 60:
#             avg.append(i["name"])
#     return avg
# avg_gtr = get_passed_students(students)
# print(avg_gtr)

# # 27. Write a function find_top_student(students) that returns the student with the highest average.
# students = [
#     {"name": "Rahul", "average": 82},
#     {"name": "Priya", "average": 91},
#     {"name": "Amit", "average": 55}
# ]
# def find_top_students(students):
#     high = 0
#     for i in students:
#         if i["average"] > high:
#             name = i["name"]
#             high = i["average"]
#     return name, high
# avg_gtr = find_top_students(students)
# print(avg_gtr)

# # 28. Write a function get_students_by_grade(students, grade) that returns students having the specified grade.
# students = [
#     {"name": "Rahul", "average": 82},
#     {"name": "Priya", "average": 91},
#     {"name": "Amit", "average": 55}
# ]
# def get_students_by_grade(students):
#     for i in students:
#         if i["average"] > 90:
#             i["grade"] = "A"
#         elif i["average"] > 70:
#             i["grade"] = "B"
#         else:
#             i["grade"] = "C"
#     return students
# stud = get_students_by_grade(students)
# print(stud)

# # 29. Write a function get_students_by_city(students, city) that returns students from a particular city.
# students = [
#     {"name": "Rahul", "average": 82, "city": "Karimnagar"},
#     {"name": "Priya", "average": 91, "city": "Hyderabad"},
#     {"name": "Amit", "average": 55, "city": "Suryapet"}
# ]
# def get_students_by_city(students, city):
#     for i in students:
#         if i["city"] == city:
#             return i
# print(get_students_by_city(students, "Hyderabad"))


# # 30. Write a function get_unique_courses(students) that returns the unique courses taken by all students.
# students = [
#     {"name": "Alice", "courses": ["Math", "Physics", "Chemistry"]},
#     {"name": "Bob",   "courses": ["Math", "Biology"]},
#     {"name": "Cara",  "courses": ["Physics", "English", "Biology"]},
#     {"name": "Dev",   "courses": ["Chemistry", "English", "History"]},
# ]
# def get_unique_courses(students):
#     unique = set()
#     for i in students:
#         unique.update(i["courses"])
#     return unique
# print(get_unique_courses(students))



# # Part 4 — Local and Global Variables
# # 31. Create a global variable:
# tax_rate = 0.18
# # Create a function that uses it to calculate tax on a given amount.
# def calculate_tax(amount):
#     tax = amount * tax_rate
#     return tax
# tax_amt = calculate_tax(1000)
# print(tax_amt)

# # 32. Create a function where a variable is defined inside the function. Try to access it outside the function.
# # Observe what happens and explain why.
# def my_function():
#     local_var = "I am local"
#     print(local_var)
# my_function()  # This will raise a NameError because local_var is not defined outside the function.

# # 33. Create:
# count = 0
# # Then write a function that attempts to increment count.
# # Understand why the behavior is different from modifying a local variable.
# def increment_count(count):
#     for i in range(5):
#         count += 1  # This will raise an UnboundLocalError because count is being referenced before assignment.
#     return count
# print(increment_count(count))  # Uncommenting this line will raise an error.

# # 34. Create a global counter and a function that modifies it using the global keyword.
# # Use this only to understand how global state works.
# def increment_global_count():
#     global count
#     for i in range(5):
#         count += 1
#     return count
# print(increment_global_count())  # This will correctly increment the global count variable.

# # 35. Write a program demonstrating the difference between:
# # local variable
# # global variable
# # parameter
# # Your program should contain examples of all three.
# # The objective here isn't to build something useful. It's to understand scope.
# def local_variable_example():
#     local_var = "I am a local variable"
#     print(local_var)
# def global_variable_example():
#     global global_var
#     global_var = "I am a global variable"
#     print(global_var)
# def parameter_example(param):
#     print(f"I am a parameter with value: {param}")
# local_variable_example()
# global_variable_example()
# parameter_example("Hello")


# # Part 5 — Lambda Functions
# # 36. Create a lambda function that calculates the square of a number.
# sq = lambda a: a**2
# print(sq(5))

# # 37. Create a lambda function that checks whether a number is even.
# even = lambda a: a % 2 == 0
# print(even(4))

# # 38. Create a lambda function that returns the larger of two numbers.
# large = lambda a,b: a if a > b else b
# print(large(4, 7))

# # 39. Given:
# numbers = [1, 2, 3, 4, 5, 6]
# # Use filter() with a lambda to obtain only even numbers.
# even = list(filter(lambda x: x % 2 == 0, numbers))
# print(even)

# # 40. Given:
# numbers = [1, 2, 3, 4, 5]
# # Use map() with a lambda to create a list of squares.
# squares = list(map(lambda x: x**2, numbers))
# print(squares)

# # 41. Given:
# students = [
#     {"name": "Rahul", "average": 82},
#     {"name": "Priya", "average": 91},
#     {"name": "Amit", "average": 76}
# ]
# # Use sorted() with a lambda to sort students by average.
# order = sorted(students, key = lambda x: x["average"])
# print(order)
# averages = list(map(lambda x: {**x, "average": x["average"] - 100}, students))
# print(averages)

# # 42. Sort the same students by name using a lambda function.
# names = sorted(students, key = lambda x: x["name"])
# print(names)



# # Part 6 — Recursion
# # 43. Write a recursive function to calculate factorial.
# def fact(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * fact(num - 1)
# result = fact(5)
# print(result)

# # 44. Write a recursive function that calculates the sum of numbers from 1 to n.
# def sum(num):
#     if num == 0:
#         return 0
#     else:
#         return num + sum(num - 1)
# print(sum(10))

# # # 45. Write a recursive function to calculate the power:
# # # 2^5 = 32
# def power(num, pow):
#     if pow == 0:
#         return 1
#     else:
#         return num * power(num, pow - 1)
# print(power(2, 5))

# # 46. Write a recursive function to reverse a string.
# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     else:
#         return s[-1] + reverse_string(s[:-1])
# print(reverse_string("hello"))

# # 47. Write a recursive function to calculate the nth Fibonacci number.
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(10))  # Output: 55

# # 48. Write a recursive function that counts down from n to 1.
# # For example:
# # 5
# # 4
# # 3
# # 2
# # 1
# def nums(num):
#     if num == 1:
#         return 1
#     else:
#         print(num)
#         return nums(num - 1)
# print(nums(5))
# # For these problems, pay attention to two things:
# # Base case
# # Recursive case
# # If you cannot clearly identify both, you don't yet understand the recursion problem.
