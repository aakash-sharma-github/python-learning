# Day 25
# Operations in tuple.
# We can use every methods of list in tuple after converting tuple to list.

tuple = (1, 2, 3, 4, 5, 2, 7, 2, 9, 3, 4, 5)

print(tuple.count(3)) # this will count and print the occurrences of given items.
print(tuple.index(2)) # this will show the element is at what index of.
print(tuple.index(2, 2, 8)) # first this will make a copy and slice tuple from index 2 to 8 and then locate position of 2 from original tuple.
print(len(tuple)) # this will print length of tuple.

# Converting tuple to list.
tup = ("mango","red", 6, True)
temp = list(tup) # Convert to tuple to list.
# Now we can perform any tasks of list in it because it has converted to list.
# Then after you have to convert the list to tuple.
temp[3] = "yellow"
tup = tuple(temp) # Converted list to tuple.
print(tup)

# concatenate tuple
name1 = ("Aakash", "sudi", "Sukesh")
name2 = ("Shah", "Sharma")
tu = name1 + name2
print(tu)