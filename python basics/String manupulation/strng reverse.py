# using slicing method

# original_string = "Hello, world!"
# reversed_string = original_string[::-1]
# print(f"The reversed string is: {reversed_string}")

#Using loop method

# b = input("enter a string: ")
# original_string = b
# reverse_string = ""
# for i in original_string:
#     reverse_string = i+reverse_string
# print (f"The reversed string is {reverse_string}")

#using join

# original_string = input("enter a string: ")
# reversed_string = ''.join(reversed(original_string))
# print(f"The reversed string is: {reversed_string}")

#using recursion
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

original_string = "Hello, world!"
reversed_string = reverse_string(original_string)
print(f"The reversed string is: {reversed_string}")

