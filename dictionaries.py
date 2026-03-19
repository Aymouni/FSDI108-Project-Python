# Dictionaries store data in KEY:VALUE pairs
# Written with curly brackets {}


student = {
    "name" : "Aymen",
    "age" : 23,
    "major" : "Computer Science"
}
print(student)

# accessing Items
print(student["name"]) # Access by key

# Changing values
student["age"] = 25
print(student)

# Removing Items
student.pop("major")
print(student)

# Check IF a key exists
if "name" in student:
    print("Key 'name' exists in the dictionary!")

# Nested Dictionary
students = {
    "student1" : {"name": "Leo", "age": 22},
    "student2" : {"name": "Aymen", "age": 21}
}
print(students["student2"]["age"]) # Access nested dict

"""
MINI Challenge
"""

report_card = {
    "name": "Aymen",
    "subject": "Math",
    "grades": (95, 95, 95)
}

print(f"Student: {report_card['name']}, Subject: {report_card['subject']}")

report_card["average"] = sum(report_card["grades"]) / len(report_card["grades"])

if report_card["average"] >= 90:
    print("EXCELLENT!")
elif report_card["average"] >= 70:
    print("Good Job")
else:
    print("Needs Improvement")

report_card.pop("subject")
print(report_card)




# ==============================
# Assignment Two
# ==============================

# Creating a dictionary
student = {
    "name": "Aymen",
    "age": 20,
    "major": "MBA",
    "gpa": 4.0
}
print("Created dictionary:", student)
print("Length:", len(student))

# Accessing values using keys
print("Name:", student["name"])
print("GPA:", student["gpa"])

# Adding a new key
student["graduation_year"] = 2027
print("After adding graduation year:", student)
print("Length:", len(student))

# Updating an existing value
student["gpa"] = 3.9
print("After updating GPA:", student)

# Removing a key
student.pop("major")
print("After removing major:", student)
print("Length:", len(student))