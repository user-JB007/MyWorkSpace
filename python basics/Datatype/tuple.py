#You can create a tuple with or without parentheses:
# Tuple with parentheses
my_tuple = (1, 2, 3)

# Tuple without parentheses
my_tuple = 1, 2, 3

# An empty tuple
empty_tuple = ()

# A tuple with a single element (note the comma)
single_element_tuple = (1,)


#You can access elements of a tuple using indexing (starting from 0 for the first element):
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[0])  # Output: apple
print(my_tuple[2])  # Output: cherry


#You can unpack the elements of a tuple into separate variables:
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3


#Tuples are immutable, which means you cannot change their contents. Attempting to do so will result in an error:
my_tuple = (1, 2, 3)
# my_tuple[1] = 4  # This will raise a TypeError


#Tuples have a few built-in methods, such as count() and index():
my_tuple = (1, 4, 5, 3, 4)
print(my_tuple.count(4))  # Output: 2 (counts the number of occurrences of 2)
print(my_tuple.index(4))  # Output: 3 (returns the index of the first occurrence of 3)

#as we have 4 two times, to find a how many indexes are there
my_tuple = (1, 4, 5, 3, 4)
indices = []

for index, value in enumerate(my_tuple):
    if value == 4:
        indices.append(index)

print(indices)  # Output: [1, 4]


#Tuples can contain other tuples (and other data types) as elements:
my_dict = {(1, 2): "a", (3, 4): "b"}
print(my_dict[(3, 4)])  # Output: a


#Because tuples are immutable, they can be used as keys in dictionaries (unlike lists):
my_dict = {(1, 2): "a", (3, 4): "b"}
print(my_dict[(1, 2)])  # Output: a
