# Tuples are just like lists - they can store multiple items
# BUT! they are IMMUTABLE (you can't change them after you create them)
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# Accessing items
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])

# Check if item exists
if "apple" in my_tuple:
    print("Yes, apple is in the tuple")

# Length of the tuple
print(len(my_tuple))

# Single item tuple
# You MUST add a comma at the end or python wont recognize it as a tuple
single = ("grape")
print(type(single)) # This is a string

tuple = ("water",)
print(type(tuple))  # This is a tuple

# Nested tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
combine = (tuple1, tuple2)
print(combine)

"""
MINI Challenge
"""
# 1. Create a tuple called travel_bag with 5 items
travel_bag = ("shirt", "shoes", "pants", "charger", "passport")

# 2. Print the second and fourth items
print("Second item:", travel_bag[1])
print("Fourth item:", travel_bag[3])

# 3. Check if "shoes" is in the travel bag
if "shoes" in travel_bag:
    print("You're ready to walk!")
else:
    print("You forgot your shoes!")

# 4. Create a new tuple called essentials
essentials = ("toothbrush", "wallet", "sunglasses")

# 5. Combine both tuples into final_bag
final_bag = travel_bag + essentials

# 6. Print how many total items
print("Total items:", len(final_bag))

# 7. Print the last item in final_bag
print("Last item:", final_bag[-1])