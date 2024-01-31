# Day 10
# User input in python.

a = input("Enter a number: ")
print(type(a))
print(a)
# Python takes input as string.
b = input("Enter first number: ")
c = input("Enter second number: ")
d = b + c
print(type(d))
print(d)

# We have to typeCast variables for desired output.
# We can convert whatever type we like. I am converting str into int.
e = int(input("Enter a number: "))
f = int(input("Enter a number: "))
g = e + f
print(type(g))
print(g)