# Day 48
# local and global variables
# local variables are also called block variables that can only be accessed inside a function.

# global variables are called universal variables that can accessed anywhere in program inside a function or outside.
# If a function has a variable same name as a global variable then variable inside a function will executed.
# if you want to change the value of local variables outside of a function then you have to use global keyword.

a = 10 # global variable

def fun():
    global x # this is not recommended because in longer programs this will create issues with readability and debugging.
    x = 15
    y = 16 # local variable

fun()
print(a)
print(x) # this is also local variable but with a global keyword that makes it accessible outside of function.
# print(y) # this will give an error because local variables are not accessible outside a function.