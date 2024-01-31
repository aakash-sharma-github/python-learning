# Day 59
# decorator in python.
# decorator modify a function and return as a function. It takes a function as an argument.
def greet(ar):
    def greeter(*args, **kwargs): # if any argument do this.
        print("Good morning!!!")
        ar(*args, **kwargs) # this is a methods thats takes arguments. *args this takes argument as a tuple and **kwargs this takes argument as a dictionary.
        print("Thanks for using this function")
    return greeter

@greet
def name():
    print("Aakash")

@greet
def add(a, b):
    print(a + b)

name()
# greet(add)(5, 6) # do this if @greet is not defined else.
add(5, 6)

# This is a additional code.
import logging

def log_function(func):
    def decorated(*args, **kwargs):
        logging.info(f"calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function
def my_function(a, b):
    print(a + b)

my_function(5, 8)