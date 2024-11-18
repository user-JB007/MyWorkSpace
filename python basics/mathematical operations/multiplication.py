# #1 Basic
# # Multiplying two numbers
# a = 5
# b = 3
# result = a * b
# print(f"The result of {a} * {b} is: {result}")
#
#
# #2
# # multiplying elements in a list
from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Using reduce to multiply all elements
result = reduce(multiply, numbers)
print(f"The result of multiplying all elements in the list is: {result}")


# #3
# #Multiplying Each Element by a Constant
# # List of numbers
# numbers = [1, 2, 3, 4, 5]
#
# # Constant to multiply each element by
# constant = 3
#
# # Multiply each element by the constant
# result = [num * constant for num in numbers]
# print(f"The result of multiplying each element by {constant} is: {result}")
#
# #4
# #Using NumPy for Matrix Multiplication
# import numpy as np
#
# # Define matrices
# matrix1 = np.array([[1, 2], [3, 4]])
# matrix2 = np.array([[5, 6], [7, 8]])
#
# # Perform matrix multiplication
# result = np.dot(matrix1, matrix2)
# print("The result of matrix multiplication is:")
# print(result)
#
#
