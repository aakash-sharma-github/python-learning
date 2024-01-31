# Day 54
# is and == in python.
# both are comparison operators.
# is check exact location of object in memory.
# == check if the value is equal or not.

# if a constant value is given to compair by is then the value will be true.
# because python will not take any extra memory for the exact same constant value. It will just levrage the location of a.
# this is not applicable to those objects which are mutable eg: list.
# is will only return true if the value is same and immutable.
# ex
a = 8
b = 8

c = "Aakash"
d = "Aakash"

e = (1, 2, 3) # tuple are immutable.
f = (1, 2, 3)

g = {3, 4, 5} # list is mutable.
h = {3, 4, 5}

print("constant: ",a is b)
print("string: ",c is d)
print("Tuple:",e is f)
print("list:",g is h)

# == operator works just exactly like the same
print(a == b)