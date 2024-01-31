# Day 33
# Dictionary in python
# dict are ordered after version 3.7.
dict = {
    "name": "Aakash",
    "age": "20",
    "college": "Parul"
}

# two ways to access the dictionary.
print(dict["age"]) # this will throw error if key is not in dictionary.
print(dict.get("college")) # this will return none if key is not found in dictionary.

# accessing keys and values in dictionary
print(dict.keys())
print(dict.values())

# accessing value using for loop
for key in dict.keys():
    print(dict[key])

# accessing items in dictionary.
print(dict.items())

# using for loop
for keys, values in dict.items():
    print(keys, values)

