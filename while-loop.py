"""
A while loop repeats a block of code as long as a condition is TRUE
Be careful - if the condition never becomes FALSE, you will get an INFINTE loop

while condition:
    # Code blok runs as long as condition is True
"""

count = 1

while count <= 5:
    print("Count is:", count)
    count += 1  # Assignment operator which adds 1 and loop stops at =5

# Using BREAK to stop a loop

number = 0

while True: 
    print(number)
    number += 1
    if number == 3:
        break   # Stops the loop when it reaches 3

# Using CONTINUE to SKIP an iteration

count = 0

while count < 5:
    count += 1
    if count == 3:
        continue    # SKIP
    print(count)

print("_______________________")
# Else with WHILE loop
# This ELSE block runs when the loop condition becomes FALSE (not by break)

count = 1

while count < 3:
    print(count)
    count += 1
else:
    print("Loop is finished!")

"""
MINI Challenge: Password checker
"""

password = ""       # Empty string
while password != "secret123":      # Keeps looing while the password is wrong
    password = input("Enter password: ")
    if password != "secret123":        # If wrong
        print("Wrong! try again.")

# Once the password is correct, while condition becomes false and loop stops
print("Access granted!")

