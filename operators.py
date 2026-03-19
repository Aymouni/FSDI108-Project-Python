# 1. Arithemtic Operators

x = 1
y = 2
res = 0

res = x + y
print(res)

res = x - y
print(res)

res = x * y
print(res)

res = x / y
print(res)

# 2. Assignment Operators - used to assign values to variables
# = meaning to put a value inside the variable

x = 5
x += 5
x -= 5
x *= 5
x /= 5
print(x)

# 3. Comparison Operator
# - Used to comapre two values
# Same as if - else

# == (equal t), !=(not equal to) <= >= (less,greaterthan)

# 4. Logical Operator - used to combine conditional statements
# Used with boolean True/False

x = 3
y = 10
z = 3
print(x == y and y == z) # False, because both conditions must be true
print(x == y or y == z)  # or -> at least one must be true
print(not x == y)        # not -> flips true to false (vice versa)

# 5. Identity Operators - used to compare the objects, not if they are equal
# But if the are actually the same 

x = 3
y = 4
print(x is y)
print(x is not y)

# 6. Memebership Operator - used to test if a sequence is presented in an object
# in -> checks if something exits in a sequesnce (list)
# no in -> checks is something does NOT exists inside

x = [1, 2, 3, 4, 5] # This is a list

print(4 in x)
print(9 not in x)
