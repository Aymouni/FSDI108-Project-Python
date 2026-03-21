# Sets are used to store multple items in a single variable
# Sets are UNORDERED, UNINDEXED, and NO DUPLICATED

# SETS are written with curly brackets {}
fruits = {"apple", "banana", "checrry"}
print(fruits)

# NO DUPLICATES ALLOWED
fruits = {"apple", "banana", "apple"}
print(fruits)   # Ignores duplicates

# Check if item exists
print("banana" in fruits)

# Adding items
fruits.add("orange")
print(fruits)

# Adding multiple items
fruits.update(["kiwi", "mango"])
print(fruits)

# Removing items
fruits.remove("banana")
print(fruits)

# If you arent sure the item exists use discard()
fruits.discard("kiwi")
print(fruits)

# Set operations (like in math)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2)) # Combining both (no duplicates)
print(set1.intersection(set2))

"""
MINI Challenge
"""

# 1. Create two sets
invited_friends = {"Alex", "Sam", "Leo", "Nina"}
rsvped = {"Nina", "Sam", "Jordan"}

# Print everyone who was invited (union of both sets)
print("Everyone invited:", invited_friends.union(rsvped))

# Print everyone who confirmed (rsvped)
print("Confirmed guests:", rsvped)

# Print who hasn't replied yet (difference)
print("Hasn't replied yet:", invited_friends - rsvped)

# Add new names to invited_friends
invited_friends.add("Maria")
invited_friends.add("Chris")
print("Updated invite list:", invited_friends)

# One person cancelled — remove from rsvped
rsvped.remove("Jordan")
print("After cancellation:", rsvped)

# Print how many total confirmed guests
print("Total confirmed guests:", len(rsvped))

# Check if Leo is still coming
if "Leo" in rsvped:
    print("Leo is coming!")
else:
    print("Leo has not confirmed yet.")