# Day 21
# Functions arguments in python

# Default argument
def fun (a, b = 6):
    print("The sum of a and b is ", (a+b))

fun(5,b=8)


def greet(name,  grt = "Good Morning!!!"):
    print(grt, name)

greet("Aakash")

# Keyword argument
fun(b = 5, a = 9)
greet(grt = "Hello",name = "Sudi")

# Required arguments.  value must be add in function call.
def req(n, p = 8):
    print("Requirement",n*p)

req(5)

# Return statement
def add(a,b):
    print("Sum is: ")
    return a + b

add(5,5)