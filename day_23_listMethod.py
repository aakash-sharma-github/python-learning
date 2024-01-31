# Day 23
# Methods of list
# list is mutable means list can be modified or change.

list = [3, 4, 5, 6, 1, 2, 10, 8, 9, 7, 11]
print(list)

# # Methods
list.append(12) # this will add 12 in the list.
list.sort() # this will sort the list.
list.reverse() # this will reverse the list.
print(list.index(5)) # this will print elements of the list using index.
print(list.count(5)) # this will count and print elements of the list.

# copy method
# l = list
# l[1] = 2 # this will change the value of index 1.
# l = list.copy() # this will make a copy of list and will not effect original list.

# list.insert(2, 20) # this will insert 20 at index 2.
# extend method
l = [30, 40, 50, 60]
list.extend(l) # this will extend and add given values to list.

print(list)