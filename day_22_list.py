# Day 22
# List datatypes in python.
# List can store different datatypes.
# Indexing of list is same as others and can be access using negative indexing.

colour = ["red", "green", "orange", "yellow"]
list = [3, 7, 9, 11, 24, 30, 40, 90, 34, 86]

# Accessing the list by indexing
print(colour[0])
print(colour[1])
print(colour[2])
print(colour[3])

# Negative indexing
print(colour[-2])
print(colour[len(colour)-1]) # Converting negative index to positive.

# Checking wether the colour is in the list or not.
if "green" in colour:
    print("yes")
else:
    print("no")

# slicing list
print(list[1:4]) # print from index 1 to 3.
print(list[1:8:2]) # print from index 1 to 8 and will jump and skip one value till index 8.
