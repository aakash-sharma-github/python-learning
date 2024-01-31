# Day 53
# map, filter and reduce.
# takes a sequence of input and gives calculated sequence of output.
# This all is a higher order function means a function that takes a function as an argument. ex 'nl = list(map(add, l1, l2))'
# map takes a function and a iterable object.
def add(a, b):
    return a + b


l1 = [5, 7, 9, 4, 9]
l2 = [7, 5, 9, 2, 4]

nl = []
# for i in l1:
#     for j in l2:
#         nl.append(add(i, j))

# mapp will iterate every element and pass through add function.
nl = list(map(add, l1, l2))
print("Map element: ",nl)

# filter is a function that filter any value as per given expression.


def greater(a):
    return a > 10


nl1 = [5, 8, 10, 13, 14, 15]
ng = list(filter(greater, nl1))
print("Filter element: ",ng)

# Reduce is a function that takes a iterable object and takes first and second value of that object as an arguments.
# and perform given expression on the taken values.
# ex [4, 5, 7, 9, 23, 45] this is a iterable object, reduce will first take 4, 5 as an argument and pass through a function then the output and next element will be taken as an argument and so on.
# you also have to import reduce.
from functools import reduce
def ad(a, b):
    return a + b

a = [9, 15, 23, 25, 30, 35]

red = reduce(ad, a)
print("Reduce element: ",red)

# map using lambda function.
a = [5, 8, 10, 13, 14, 15]
b = [9, 15, 23, 25, 30, 35]

ab = list(map(lambda x, y: x + y, a, b))
print("Map using lambda: ",ab)

# filter using lambda function.
c = [5, 2, 3, 4]
fil = list(filter(lambda x: x > 2, c))
print("Filter using lambda: ",fil)

# reduce using lambda function.
num = [5, 2, 4, 5, 6, 7]
reud = reduce(lambda x, y: x * y, num)
print("Reduce using lambda: ",reud)