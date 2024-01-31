# Day 36
# ErrorHandling in python

a = input("Enter a number: ")

try:

    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")

# we can use multiple except.
except Exception as e: # we can also use only except.
    print(e) # This will explain error.
    print("Invalid input")

print("End of program")