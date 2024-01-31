# Day 38
# Raising customErrorMessage in python

a = int(input("Enter a number 50 and 55:"))

if a < 50 or a > 55:
    raise ValueError("Please enter valid a number")

print("End of program.")

# Quick Quiz
qz = input("Enter a number between 5 ans 10 enter quit:")
if qz != 'quit':
    raise ValueError("invalid input")
else:
    qz = int(qz)
    if qz < 5 or qz > 10:
        raise ValueError("Please enter a number between 5 and 10")

print("End of program.")