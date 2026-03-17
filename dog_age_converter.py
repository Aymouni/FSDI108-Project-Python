# Dog Age Converter title

print("---------- Dog Age Converter ----------\n")

# Ask the user for their dog's age and convert to integer
human_age = int(input("Enter your dog's age in human years: "))

# Multiply by 7 to convert to dog years
dog_age = human_age * 7

# Display the result using an f-string
print(f"Your dog is {dog_age} years old in dog years!")