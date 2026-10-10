# ------------------ Part 1 — NumPy Basics and Array Creation ---------------------------

# 1. Import NumPy and create a 1D array containing:
# 10, 20, 30, 40, 50
# Print the array.
import numpy as np

# arr = np.array([10, 20, 30, 40, 50])
# print(arr)

# # 2. Create a NumPy array containing the numbers from 1 to 20.
# arr = np.arange(1, 21, 2)
# print(arr)

# # 3. Create an array containing all even numbers from 2 to 20.
# arr = np.arange(2, 21, 2)
# print(arr)

# # 4. Create a NumPy array of five zeros.
# arr = np.zeros(5)
# print(arr)

# # 5. Create a NumPy array of seven ones.
# a = np.ones(7)
# print(a)

# # 6. Create an array containing the values:
# arr = np.array([5, 10, 15, 20, 25])
# # arr  = np.full(5, 5)
# print(arr)

# # shape
# # size
# # number of dimensions
# # data type
# print(arr.shape)
# print(arr.size)
# print(arr.ndim)
# print(arr.dtype)

# # 7. Create a 3 × 3 NumPy array containing numbers from 1 to 9.
# arr = np.array(range(1, 10)).reshape(3, 3)
# # mat = np.eye(3, 3, arr)
# print(arr)

# # 8. Create a 4 × 5 array containing numbers from 1 to 20.
# arr = np.array(range(1, 21)).reshape(4, 5)
# print(arr)

# # 9. Create a 3 × 4 array filled with zeros.
# arr = np.zeros(12).reshape(3, 4)
# print(arr)

# # 10. Create a 5 × 5 identity matrix using NumPy.
# mat = np.eye(5, 5)
# print(mat)



# --------------------- Part 2 — Array Indexing --------------------------

# # 11. Given:
# arr = np.array([10, 20, 30, 40, 50])
# # Print:
# # first element
# # last element
# # second element
# # second-last element
# print(arr[0])
# print(arr[-1])
# print(arr[1])
# print(arr[-2])


# # 12. Given:
# arr = np.array([5, 10, 15, 20, 25, 30])
# # Access the element 20 using its index.
# print(arr[arr==20])

# # 13. Given:
# arr = np.array([10, 20, 30, 40, 50])
# # Change:
# # 30 → 100
# arr[arr==30] = 100
# # and print the modified array.
# print(arr)

# # 14. Given:
# arr = np.array([10, 20, 30, 40, 50])
# # Change the first element to 999.
# arr[0] = 999
# print(arr)

# # 15. Given:
# arr = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])
# # Print:
# # 10
# # 50
# # 90
# # using indexing.
# print(arr[0, 0])
# print(arr[1, 1])
# print(arr[2, 2])

# # 16. Using the same 2D array, print:
# # 20
# # 40
# # 80
# print(arr[0, 1])
# print(arr[1, 0])
# print(arr[2, 1])


# # 17. Given a 4 × 4 array, access the element located at:
# # row 3
# # column 2
# arr = np.array(range(1, 17)).reshape(4, 4)
# print(arr[3, 2])

# # 18. Create a 3D NumPy array and access a specific element using three indices.
# arr = np.array(range(1, 25)).reshape(2, 3, 4)
# # The important thing here is understanding:
# # array[layer][row][column]
# print(arr[1, 1, 2])
# # rather than memorizing syntax.



# -------------------------- Part 3 — Slicing Arrays ---------------------------------

# 19. Given:
# arr = np.array([10, 20, 30, 40, 50, 60, 70])
# # Print:
# # first three elements
# print(arr[0:3])
# # last three elements
# print(arr[-3:])
# # elements from index 2 to 5
# print(arr[2:6])

# # 20. Using the same array, print every second element.
# print(arr[::2])

# # 21. Reverse the array using slicing.
# print(arr[::-1])

# # 22. Given:
# arr = np.arange(1, 21)
# # extract:
# # 1–5
# print(arr[:5])
# # 10–15
# print(arr[9:15])
# # last 5 values
# print(arr[-5:])
# # all even-indexed values
# print(arr[::2])

# # 23. Given a 4 × 4 array, extract the first two rows.
# arr = np.array(range(1, 17)).reshape(4, 4)
# print(arr[:2])

# # 24. Extract the last two rows.
# print(arr[-2:])

# # 25. Extract the first two columns.
# print(arr[:, :2])

# # 26. Extract the middle 2 × 2 section of a 4 × 4 array.
# print(arr[1:3, 1:3])

# # 27. Given:
# arr = np.arange(1, 26).reshape(5, 5)
# print(arr)
# # extract:
# # top-left 3 × 3 matrix
# print(arr[0:3, 0:3])
# # bottom-right 2 × 2 matrix
# print(arr[-2: , -2:])
# # first column
# print(arr[:, 0])
# # last column
# print(arr[:, -1])
# # middle row
# print(arr[2])

# # 28. Reverse the rows of a 2D array using slicing.
# print(arr[::-1])

# # 29. Reverse the columns of a 2D array using slicing.
# print(arr[:, ::-1])



# -------------------- Part 4 — Mathematical Operations ----------------------------------

# # 30.  Given:
# a = np.array([10, 20, 30, 40])
# b = np.array([1, 2, 3, 4])
# # Calculate:
# # a + b
# # a - b
# # a * b
# # a / b
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

# # 31. Multiply every element of an array by 5.
# a = np.array([10, 20, 30, 40])
# print(a * 5)

# # 32. Add 100 to every element of an array.
# print(a + 100)

# # 33. Square every element of:
# arr = np.array([1, 2, 3, 4, 5])
# print(arr ** 2)

# # 34. Calculate the square root of every element in an array.
# arr = np.array([1, 4, 9, 16, 25])
# print(arr ** (0.5))

# 35. Given two arrays of student marks:
# math = np.array([80, 75, 90, 85])
# science = np.array([70, 88, 92, 81])
# # calculate the total marks for each student.
# print(math + science)

# # 36. Given three arrays:
# math = np.array([80, 75, 90, 85])
# science = np.array([70, 88, 92, 81])
# english = np.array([65, 85, 75, 80])
# # math
# # science
# # english
# # calculate the average mark of every student.
# print((math + science + english) / 3)

# # # 37. Increase every product price in an array by 10%.
# product = np.array([80, 75, 90, 85])
# print(product * 1.1)

# # 38. Given an array of temperatures in Celsius, convert every value to Fahrenheit.
# temperature = np.array([23, 35, 28, 33, 30, 37])
# # Formula:
# # F = C × 9/5 + 32
# print(temperature * (9/5) + 32)


# # 39. Given an array of salaries, increase every salary by 15%.
# salaries = np.array([20000, 30000, 40000, 35000, 28000])
# print(salaries + (salaries * 0.15))



# -------------------- Part 5 — Combining and Splitting Arrays ------------------------

# # 40. Given:
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# # combine them into:
# # [1 2 3 4 5 6]
# # using NumPy.
# print(np.concatenate((a, b), axis = 0))

# # 41. Combine two 2D arrays vertically.
# arr1 = np.array([[1, 2, 3], [4, 5, 6]])
# arr2 = np.array([[7, 8, 9], [10, 11, 12]])
# print(arr1, arr2)
# print(np.stack((arr1, arr2)))
# print(np.vstack((arr1, arr2)))

# # 42. Combine two 2D arrays horizontally.
# print(np.hstack((arr1, arr2)))

# # 43. Given:
# arr = np.arange(1, 13)
# # split it into three equal arrays.
# print(np.split(arr, 3))

# # 44. Split a 12-element array into four equal parts.
# print(np.split(arr, 4))

# # 45. Given a 4 × 4 array, split it into two arrays based on rows.
# arr = np.array(range(1, 17)).reshape(4, 4)
# print(np.vsplit(arr, 2))

# # 46. Given a 4 × 4 array, split it into two arrays based on columns.
# print(np.hsplit(arr, 2))


# ----------------------- Part 6 — Search, Filter and Sort -------------------------------

# # 47. Given:
# arr = np.array([10, 25, 30, 45, 50, 65, 70])
# # find the positions of all values greater than 40.
# print(np.where(arr > 40))

# # 48. Given an array of student marks, filter students who scored at least 75.
# # For example:
# arr = np.array([45, 82, 67, 91, 73, 88])
# # Expected values:
# # 82 91 88
# print(*arr[arr > 80])

# # 49. Given:
# arr = np.array([50, 20, 80, 10, 90, 30])
# # sort the array:
# # ascending
# print(np.sort(arr))
# # descending
# print(np.sort(arr, descending=True))

# # 50. Given:
# marks = np.array([45, 82, 67, 91, 73, 88])
# # perform all of the following:
# # 1. Find the highest mark
# print(np.max(marks))
# # 2. Find the lowest mark
# print(np.min(marks))
# # 3. Find the average mark
# print(np.mean(marks))
# # 4. Find the median
# print(np.median(marks))
# # 5. Find the standard deviation
# print(np.std(marks))
# # 6. Find the index of the highest mark
# print(np.argmax(marks))
# # 7. Find all marks above the average
# print(marks[marks > np.mean(marks)]) 
# # 8. Sort the marks
# print(np.sort(marks))
# # 9. Count how many students scored >= 75
# print(np.size(marks[marks >= 75]))
# # 10. Count how many students failed (< 40)
# print(np.size(marks[marks < 40]))



# ---------------------  Additional Statistical Practice  ------------------------------

# # Given:
# marks = np.array([72, 85, 91, 68, 77, 88, 95, 54, 81, 73])
# # Calculate:
# print(np.mean(marks)) # Mean
# print(np.median(marks))  # Median
# print(np.min(marks))  # Minimum
# print(np.max(marks))  # Maximum
# print(np.max(marks) - np.min(marks)) # Range
# print(np.std(marks)) # Standard deviation
# print(np.var(marks)) # Variance
# print(np.percentile(marks, 25)) # 25th percentile
# print(np.percentile(marks, 50)) # 50th percentile
# print(np.percentile(marks, 75)) # 75th percentile

# # Then answer:
# # What percentage of students scored above the mean?
# print(((marks[marks > np.mean(marks)].size) / 10) * 100)


# # Mixed Problem 1 — Sales
# # You have:
# sales = np.array([
#     1200,
#     850,
#     1500,
#     2300,
#     950,
#     1800,
#     2100
# ])
# # Find:
# print(np.sum(sales)) # Total sales
# print(np.mean(sales)) # Average sales
# print(np.max(sales)) # Highest sales
# print(np.min(sales)) # Lowest sales
# print(np.where(sales > 1500)) # Days with sales > 1500
# print(np.count_nonzero(sales > 1500)) # Number of days with sales > 1500
# print(np.sort(sales)) # Sales sorted from highest to lowest

# # Mixed Problem 2 — Employee Salaries
# salaries = np.array([
#     30000,
#     45000,
#     52000,
#     38000,
#     60000,
#     75000,
#     42000
# ])
# # Calculate:
# print(np.mean(salaries)) # Average salary
# # Median salary
# # Highest salary
# # Lowest salary
# # Employees earning > 50000
# print(salaries * 1.10) # 10% salary increase for everyone

# print(np.mean(salaries * 1.10)) # Then calculate the new average salary.

# # Mixed Problem 3 — Student Performance

# # Create:
# math = np.array([78, 85, 92, 67, 55, 88, 73])
# science = np.array([82, 79, 95, 70, 61, 90, 75])
# english = np.array([75, 88, 91, 72, 64, 85, 80])
# # Calculate:
# print(math + science + english) # Total marks for each student
# avg = (math + science + english) / 3
# print(avg) # Average marks for each student
# print(np.max(avg)) # Highest average
# print(np.min(avg)) # Lowest average
# print(avg[avg >= 75]) # Students with average >= 75
# print(avg[avg > 60].size) # Number of students who passed
# print(avg[avg <= 60].size) # Number of students who failed

# # Mixed Problem 4 — Product Prices
# prices = np.array([100, 250, 75, 500, 120, 300])
# # Apply:
# print(prices * 0.1) # 10% discount
# # Then:
# print(prices - (prices * 0.1)) # Calculate discounted prices
# print(np.sum(prices)) # Calculate total original value
# print(np.sum(prices - (prices * 0.1))) # Calculate total discounted value
# print(np.sum(prices * 0.1)) # Calculate total savings

# # Mixed Problem 5 — Temperature Analysis
# temperatures = np.array([32, 35, 31, 29, 38, 40, 36, 33, 30, 41])
# # Find:
# # Average temperature
# # Maximum temperature
# # Minimum temperature
# print(np.where(temperatures > 35)) # Days above 35
# print(np.where(temperatures < 32)) # Days below 32
# # Median temperature
# # Standard deviation

# print(np.sort(temperatures)) # Then sort the temperatures.