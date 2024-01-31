# Day 24
# Tuple datatype
# Tuple is immutable object means it cannot be modified or changed.
# It can store different datatypes

# tup = (20) #this is not tuple.
# tup = (20,) #this is tuple u have to give comma to tell python that this is tuple.
# Indexing is also same as list.
# The only difference between list and tuple is that list can change and tuple cannot change thats it.
t = (4, 5, 6, 7, 9, 10)
# slicing
print(t[1:4])

# checking given element is in the list or not
if 6 in t:
    print("yes")
else:
    print("no")