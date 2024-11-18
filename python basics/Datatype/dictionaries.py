# An empty dictionary
empty_dict = {}

# A dictionary with string keys and integer values
fruit_prices = {"apple": 1, "banana": 2, "cherry": 3}

# A dictionary with mixed data types
student_info = {"name": "Alice", "age": 20, "is_enrolled": True}

#You can access the value associated with a specific key using square brackets:
fruit_prices = {"apple": 1, "banana": 2, "cherry": 3}
print(fruit_prices["apple"])  # Output: 1


#Dictionaries are mutable, so you can change the values associated with existing keys or add new key-value pairs:
fruit_prices = {"apple": 1, "banana": 2, "cherry": 3}
fruit_prices["banana"] = 5  # Modify the value associated with "banana"
fruit_prices["date"] = 4    # Add a new key-value pair
print(fruit_prices)  # Output: {"apple": 1, "banana": 5, "cherry": 3, "date": 4}


#You can remove key-value pairs using the del keyword or the pop() method:
fruit_prices = {"apple": 1, "banana": 2, "cherry": 3}

# Remove a key-value pair using del
del fruit_prices["apple"]
print(fruit_prices)  # Output: {"banana": 2, "cherry": 3}

# Remove a key-value pair using pop
price_of_banana = fruit_prices.pop("banana")
print(fruit_prices)  # Output: {"cherry": 3}
print(price_of_banana)  # Output: 2


#You can iterate over the keys, values, or key-value pairs in a dictionary:
fruit_prices = {"apple": 1, "banana": 2, "cherry": 3}

# Iterate over keys
for key in fruit_prices:
    print(key)
# Output:
# apple
# banana
# cherry

# Iterate over values
for value in fruit_prices.values():
    print(value)
# Output:
# 1
# 2
# 3

# Iterate over key-value pairs
for key, value in fruit_prices.items():
    print(key, value)
# Output:
# apple 1
# banana 2
# cherry 3


#You can check if a key exists in a dictionary using the in keyword:
fruit_prices = {"apple": 1, "banana": 2, "cherry": 3}
print("apple" in fruit_prices)  # Output: True
print("date" in fruit_prices)   # Output: False
