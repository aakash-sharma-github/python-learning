# Day 44
# How imports works in python.
# import is used for importing any module to your program so that you can easily perform any perticular tasks.
# example
from math import sqrt # this will import sqrt functions from math module. note: in this import you can only use sqrt functions.
print(sqrt(25))

# importing every fumction from any module using * keyword.
from math import * # this will import every functions from math. note: in this import you can use any function of math module.
print(sqrt(25)) # this will print the value of sqrt(25)

# Using imported functions as a different name using as keyword.
from math import sqrt as s # now i can use sqrt functions by s as a short name.
print(s(25))

# dir keyword used for listing any module so that you can check functions and methods present in the module.
import math
print(dir(math)) # this will print all the functions and methods present in math module.
print(type(sin)) # you can also check type of that function.

# You can also create your own module.
# create a .py file write your function or any program then you can import it anywhere by your function name.
# in day 30 i have created a function which calculate factorial and now i am going to import that function in this file.
# you can import your function as " from 'filename' import 'function_name' "
from day_30 import factorial
print(factorial(10))