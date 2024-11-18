#You can create a set using curly braces {} or the set() function:
# Creating a set with curly braces
my_set = {1, 2, 3, 4, 5, 4}

# Creating an empty set (note: you must use the set() function, as {} creates an empty dictionary)
empty_set = set()

# Creating a set with the set() function
another_set = set([1, 2, 3, 4, 5])

#You can add elements to a set using the add() method:
my_set = {1, 2, 3, 5}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}


#You can remove elements from a set using the remove() or discard() method:
my_set = {1, 2, 3, 4}
my_set.remove(3)  # Removes 3 from the set
print(my_set)  # Output: {1, 2, 4}

my_set.discard(2)  # Removes 2 from the set
print(my_set)  # Output: {1, 4}


#Sets support various mathematical set operations like union, intersection, difference, and symmetric difference:
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union: elements in either set
union_set = set_a.union(set_b)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection: elements in both sets
intersection_set = set_a.intersection(set_b)
print(intersection_set)  # Output: {3}

# Difference: elements in set_a but not in set_b
difference_set = set_a.difference(set_b)
print(difference_set)  # Output: {1, 2}

# Symmetric Difference: elements in either set, but not in both
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}

#You can check if an element is a member of a set using the in keyword:
my_set = {1, 2, 3, 4}
print(2 in my_set)  # Output: True
print(5 in my_set)  # Output: False


#You can iterate over the elements of a set using a loop:
my_set = {1, 2, 3, 4}
for element in my_set:
    print(element)


