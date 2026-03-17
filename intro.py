print("Hello World from Python!") # No semicolons needed
print(2)
print(5 + 3)
print(True)

# Comments
"""
This is a comment

"""

# Variables and Concatenations
name  = "Aymen"
age = 35
print(name,age) # Print the variable value

# Concatentaions (Joining strings with +)
# Concatenations cannot combine strings and integer
# To Fix it - cast age to string using str()
print("May name is " + name + ", and I am " + str(age) + " years old.")

name  = "Mike"
age = 30
middle_name = "Smith"
last_name = "Saad"
found = False # Boolean variable

print(name)
print("May name is " + name + ", and I am " + str(age) + " years old.")
print("Did he show up to class? " + str(found))

# MINI Challenge

pet_name = "Luna"
pet_age = 3
breed = "Golden Retriever"
tricks = 5

print("My dog " + pet_name + " is " + str(pet_age) + " years old. She is a " + breed + " and knows " + str(tricks) + " tricks!")

# F-String
# Start with f"", variable in {} # Cleaner way
work = "SDGKU"
job = "Prof"
print(f"I work at {work} my job is {job}!")

# Multi-line f-string
print(f"""
my name is {name} {middle_name} {last_name}
I like Python!
    Type indentations
""")

# Type function
print(type(name))   #<class 'str'>
print(type(age))    #<class 'int'>
print(type(found))   #<class 'bool'>

# Casting (changing data types)
print(20 + int("20"))
print(20 + age)
print(20 + 2.98)


# User input
# Input() lets the user type values into the terminal
user_name = input("Input your name: ")
print(f"Hello, {user_name}")

print(input("Enter your age: "))

# Example: converting input to INT
new_age = int(input("Enter your age: "))
print(age + new_age)


# MINI Challenge
pizza_slices = int(input("How many slices of pizza do you have? "))
people = int(input("How many people are eating? "))

slices_per_person = pizza_slices // people

print(f"Each person gets {slices_per_person} slices.")