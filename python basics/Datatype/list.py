# An empty list
empty_list = []

# A list of integers
int_list = [1, 2, 3, 4, 5]

# A list of strings
str_list = ["apple", "banana", "cherry"]

# # # A list with mixed data types
mixed_list = [1, "apple", 3.14, True]

# #You can access individual elements of a list using indexing (starting from 0 for the first element):
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[2])  # Output: cherry

#Lists are mutable, so you can change their contents:
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)  # Output: ["apple", "blueberry", "cherry"]

#You can add elements to a list using methods like append() and extend():
# Append a single element
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # Output: ["apple", "banana", "cherry"]

# Extend the list with multiple elements
fruits.extend(["date", "elderberry"])
print(fruits)  # Output: ["apple", "banana", "cherry", "date", "elderberry"]

#You can remove elements using methods like remove(), pop(), and del:
# Remove an element by value
fruits = ["apple", "banana", "cherry"]
fruits.remove("apple")
print(fruits)  # Output: ["apple", "cherry"]

#to remove an element that occurs multiple times in a list
fruits = ["apple", "banana", "cherry", "apple"]
# Using a list comprehension to remove all occurrences of "apple"
fruits = [x for x in fruits if x != "apple"]
print(fruits)  # Output: ["banana", "cherry"]

#using  for loop
frts=[]
for x in fruits:
    if x !="apple":
        frts.append(x)
print(frts)   #output: ["banana", "cherry"]


# Remove an element by index
fruits = ["apple", "banana", "cherry", "apple"]
removed_fruit = fruits.pop(1)
print(fruits)  # Output: ["apple", "cherry"]
print(removed_fruit)  # Output: banana

# Remove an element using 'del'
fruits = ["apple", "banana", "cherry"]
del fruits[0]
print(fruits)  # Output: ["banana", "cherry"]

#You can extract a portion of a list using slicing:
numbers = [11,0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sliced_numbers = numbers[2:6]
print(sliced_numbers)  # Output: [2, 3, 4, 5]

#List comprehensions offer a concise way to create lists:
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

