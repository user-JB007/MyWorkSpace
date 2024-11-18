# #1
# # Floating-point division
a = 10
b = 3
result_float = a / b
print(f"The result of {a} / {b} (floating-point) is: {result_float}")

# Integer division
result_int = a // b
print(f"The result of {a} // {b} (integer) is: {result_int}")
#
# #2
# # Modulo operation
# result_mod = a % b
# print(f"The result of {a} % {b} (remainder) is: {result_mod}")
#
# #3
# # Division in a List
# numbers = [10, 20, 30, 40, 50]
# divisor = 5
#
# # Divide each element by the divisor
# result_list = [num / divisor for num in numbers]
# print(f"The result of dividing each element by {divisor} is: {result_list}")
#
# #4 Using NumPy for Element-wise Division
# import numpy as np
#
# # Define arrays
# array1 = np.array([10, 20, 30, 40, 50])
# array2 = np.array([2, 4, 6, 8, 10])
#
# # Perform element-wise division
# result_array = np.divide(array1, array2)
# print("The result of element-wise division is:")
# print(result_array)

a=11
b=3

d=a/b
e=a//b
f=a%b

print(d,e,f)
