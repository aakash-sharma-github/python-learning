# Day 9
# TypeCasting in python.

# Explicit typecasting 
# Developer converts variable type one from another is Explicit typecasting.
a = "1"
b = "2"
# gives integer output.
print(int(a)+int(b))

# Implicit typecasting
# python itself converts its type.
#  Python converts lower datatype to higher datatype to prevent data loss.
c = 14.8 
print(type(c))
d = 4
print(type(d))
# Gives float output.
e = c+d
print(type(e))
