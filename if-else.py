# if -> checks a condition
#elif -> (else if) checks another condition if the first one is False
#else -> runs if all other conditions are False

x = 10

if x > 0:
    print("X is positive")
elif x == 0:
    print("X is zero")
else:
    print("X is negative")

# Short Hand IF Statements

if x > 5: print("X is greater than 5")

# Short Hand if..else

print("Even") if x % 2 == 0 else print("Odd")

# Nested If Statements

if x > 0:
    if x < 20:
        print("X is a positive number less than 20")

# Combining Condition

age = 18

if age >= 18 and age <=21:
    print("You are between 18 and 21 years old!")

"""
MINI Chanllenge

"""

temperature = int(input("Enter today's temperature in Fahrenheit: "))


if temperature >= 86:
    print("It's hot outside!")
elif temperature >= 68 and temperature < 86:
    print("The weather is nice.")
elif temperature >= 50 and temperature < 68:
    print("It's a bit chilly.")
else:
    print("It's cold.")

jacket = True if temperature < 59 else False

if jacket:
    print("Better wear a jacket!")
else:
    print("No jacket needed.")