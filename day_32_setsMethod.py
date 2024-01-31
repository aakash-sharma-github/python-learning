# Day 32
# methods of sets

# Union merging of two sets
s = {2, 3, 4, 5, 6}
s1 = {1, 2, 3, 4, 5}
# print(s.union(s1))

# update() update the missing value of first set
# s.update(s1)
# print(s)

# Intersection() print the value which is available in both sets
# s2 = s.intersection(s1)
# print(s2)

# Intersecrion_update() print the first element with the value which is available in both sets
# s.intersection_update(s1)
# print(s)

# symmetric_difference() will ignore the common value
# s3 = s.symmetric_difference(s1)
# print(s3)

# difference will print the value which is not present in first set
# in my case it will print the value which is not present in s1
# s4 = s.difference(s1)
# print(s4)

# isdisjoint() will check if any of the value are common if found common false value will be returned
# print(s.isdisjoint(s1))

# issuperset() will check that the value of second set is present or not if not present return false
# print(s.issuperset(s1))

# issubset() will check that the value of first set is present or not if not present return false
# print(s.issubset(s1))

# add() will add a new value to the set
# s.add(9)
# print(s)

# update() will update the value in set of other set.
# s.update(s1)
# print(s)

# remove() and discard() is used for removing a value from the set.
# discard will not raise error if given value is not present it will print the whole set but remove will raise error.
# s.remove(2)
# s.discard(10)
# print(s)

# pop() will remove a random value from the set because sets are unordered
# s6 = s.pop()
# print(s)
# print(s6)

# del is keyword not a method in python and it will delete an entire set.
# del s
# print(s) # this will throw an error because s has already been deleted.

# clear() will remove all values from the set.
# s.clear()
# print(s)

# check if given value exists in the set
# if 10 in s:
#     print("yes")
# else:
#     print("no")
