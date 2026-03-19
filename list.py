# Lists are used to store MULTIPLE items in a single variable.
# Think of a container that can hold many items
# Lists are written with square brackets []

my_list = [10, 20, 30, 40, 50]
print(my_list)

# List can contain different data types

mixed_list = [1, "apple", 3.5, True]
print(mixed_list)

# You can access list items by their INDEX number
# (Indexing starts at 0)

fruits = ["apple", "banana", "cherry"]
print(fruits[0]) # First item (apple)
print(fruits[2])

# You can also use a NEGATIVE indexes to count from the end
print(fruits[-2])

# Modifying List Items

fruits[1] = "mango" # Change banana for mango
print(fruits)

# Adding items
fruits.append("orange") # Adds orange to the END
print(fruits)

fruits.insert(1, "kiwi") # Adds items 
print(fruits)

# Removing the item
fruits.remove("apple")
print(fruits)

# Looing through a list
for fruit in fruits:
    print(fruit)

# Check if item exists
if "mango" in fruits:
    print("Yes, mango is in the list")

# List Length
print(len(fruits)) # Number of items list




# ==============================
# Assignment Two
# ==============================

# The list
cars = ["Toyota", "Honda", "Ford", "BMW", "Tesla"]
print("Created list:", cars)

# Accessing by index
print("First car:", cars[0])
print("Last car:", cars[-1])

# Replacing values
cars[2] = "Chevrolet"
print("After replacing Ford with Chevrolet:", cars)

# Removing values
cars.remove("Honda")
print("After removing Honda:", cars)

# Removing by index
cars.pop(1)
print("After removing item at index 1:", cars)

# Printing the list and its length
print("Final list:", cars)
print("Length:", len(cars))