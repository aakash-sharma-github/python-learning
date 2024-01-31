# Day 34
# Methods in dictionary

dict = {
    "name": "Aakash",
    "age": "21",
    "address": "nepal",
}
dict1 = {
    "current": "india",
    "college": "Parul"
}

# update() will update the second dictionary's keys and value in first dictionary.
dict.update(dict1)
print(dict)

# clear() used to clear the dictionary.
# dict.clear()
# print(dict)

# pop() will remove the given key value pair.
dict.pop("age")
print(dict)

# popitem() will remove the last key value pair from the dictionary.
dict.popitem()
print(dict)

# del keyword will delete the whole dictionary
del dict
print(dict)

del dict1["college"] # this will delete selected key value pairs.
print(dict1)

