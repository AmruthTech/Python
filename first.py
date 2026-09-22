# marks = 80
#
# print("Grade O") if marks >= 90 else print("Grade A")
# num = int(input("Enter a number: "))
# if num > 0:
#     print("Positive number")
# elif num < 0:
#     print("Negative number")
# else:
#     print("Zero")

# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(num, "is even")
# else:
#     print(num, "is odd")


# print("1 to Square \n2 to Rectangle \n3 to Circle \n4 to Triangle")
# area_choice = int(input("Enter the area choice: "))
#
# if area_choice == 1:
#     side = float(input("Enter the side choice: "))
#     print((side)**2)
# elif area_choice == 2:
#     length = float(input("Enter the length: "))
#     breadth = float(input("Enter the breadth: "))
#     print(length*breadth)
# elif area_choice == 3:
#     radius = float(input("Enter the radius: "))
#     print(2*3.14*radius**2)
# elif area_choice == 4:
#     base = float(input("Enter the base: "))
#     height = float(input("Enter the height: "))
#     print(0.5*base*height)
# else:
#     print("Invalid choice, Please select between 1 and 4")

# letter = input()
# if letter in 'AEIOUaeiou':
#     print("Vowel")
# else:
#     print("Not a Vowel")

n = int(input())
n = str(n)
if len(n)==1:
    print("single digit number")
elif len(n)==2:
    print("two digit number")
elif len(n)==3:
    print("three digit number")
elif len(n)==4:
    print("four digit number")
elif len(n)==5:
    print("five digit number")
else:
    print("Greater than 5-digit number")