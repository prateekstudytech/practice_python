print("Mutable vs Immutable Types in Python")
# In Python, there are two main categories of data types: mutable and immutable.

# Integertypes are immutable, meaning they cannot be changed after creation.
# This means that any operation that seems to modify an integer actually creates a new integer.
num1 = 10
print(f"Value of num1: {num1}")  # Output: 10
print(f"id of num1: {id(num1)}") # Output: Memory address of the integer object

# Integers are immutable in Python, so when we perform operations on them,
# we are not modifying the original integer, but rather creating a new one.
# Attempting to change the value of 'num1' directly will not work as integers are immutable.
num1 += 5
# This creates a new integer and assigns it to 'num1', but does not modify the original integer.
print(f"Value of num1: {num1}")  # Output: 15
print(f"id of num1: {id(num1)}") # Output: Memory address of the new integer object
# The id of 'num1' has changed, indicating that a new integer object has been created.

num2 = num1
# This creates a new reference to the same integer object.
print(f"Value of num2: {num2}")  # Output: 15
print(f"id of num2: {id(num2)}") # Output: Memory address of the same integer object
# If we assign a new integer to 'num2', it will create a new integer object.
num2 = 20
# This creates a new integer object and assigns it to 'num2', changing the reference.
print(f"Value of num2: {num2}")  # Output: 20
print(f"id of num2: {id(num2)}") # Output: Memory address of the new integer object
# The id of 'num2' has changed, indicating that we have created a new integer object.
# In summary, integers are immutable in Python, and any operation that seems to modify them
# actually creates a new integer object, leaving the original unchanged.


# Lists, on the other hand, are mutable, meaning they can be changed in place.
b = [1, 2, 3]
print(f"Value of b: {b}")  # Output: [1, 2, 3]
# The id of 'b' is the memory address of the list object.
print(f"id of b: {id(b)}") # Output: Memory address of the list object

# We can modify the list in place, which will change the original list object.
b.append(4)
# This modifies the original list object, adding a new element to it.
print(f"Value of b: {b}")  # Output: [1, 2, 3, 4]
print(f"id of b: {id(b)}") # Output: Memory address of the modified list object
# The id of 'b' remains the same, indicating that we have modified the original list object.
# If we assign a new list to 'b', it will create a new list object.
b = [5, 6, 7]
# This creates a new list object and assigns it to 'b', changing the reference.
print(f"Value of b: {b}")  # Output: [5, 6, 7]
print(f"id of b: {id(b)}") # Output: Memory address of the new list object
# The id of 'b' has changed, indicating that we have created a new list object.
# In summary, integers are immutable and create new objects when modified,
# while lists are mutable and can be changed in place.


# Dictionaries are also mutable, meaning they can be changed in place.

dict1 = {'key1': 'value1', 'key2': 'value2'}
print(f"Value of dict1: {dict1}")  # Output: {'key1': 'value1', 'key2': 'value2'}
print(f"id of dict1: {id(dict1)}") # Output: Memory address of the dictionary object

# We can modify the dictionary in place, which will change the original dictionary object.
dict1['key3'] = 'value3'
# This modifies the original dictionary object, adding a new key-value pair to it.
print(f"Value of dict1: {dict1}")  # Output: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(f"id of dict1: {id(dict1)}") # Output: Memory address of the modified dictionary object

dict2 = dict1
# This creates a new reference to the same dictionary object.
print(f"Value of dict2: {dict2}")  # Output: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(f"id of dict2: {id(dict2)}") # Output: Memory address of the same dictionary object
# Modifying dict2 will also modify dict1, as they both reference the same object.
dict2['key4'] = 'value4'
# This modifies the original dictionary object, adding a new key-value pair to it.
print(f"Value of dict1: {dict1}")  # Output: {'key1': 'value1', 'key2': 'value2',
# 'key3': 'value3', 'key4': 'value4'}
print(f"Value of dict2: {dict2}")  # Output: {'key1': 'value1', 'key2': 'value2',
# 'key3': 'value3', 'key4': 'value4'}
print(f"id of dict1: {id(dict1)}") # Output: Memory address of the modified dictionary object
print(f"id of dict2: {id(dict2)}") # Output: Memory address of the modified dictionary object
# In summary, dictionaries are mutable and can be changed in place,
# and multiple references to the same dictionary object will reflect changes made to it.
