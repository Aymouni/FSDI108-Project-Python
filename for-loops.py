"""
A for loop in python is a control structure that lets you repeat a bloxk of code for each
item in a sequesnce (such as list, string, tuple, range of numbers, etc..)

for variable in sequence:
    # Code block runs for each item in the sequence
"""

# Basic example
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

for letter in "Aymen":
    print(letter)

print("__________________________________________")

# Range() generates a sequence of numbers
for x in range(5):  # Runs through the range until stops
    print(x)

print("__________________________________________")
# Start and end range
for x in range(2, 6):
    print(x)

print("__________________________________________")
# Step
for x in range(0, 10, 2):
    print(x)

print("__________________________________________")


"""
MINI Challenge
"""

# Ask the user to enter a number
num = int(input("Enter a number: "))

# Loop from 1 to 10 and multiply
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")