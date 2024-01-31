# Day 13
# Strings methods.

a = "Aakash"

# convert all character into uppercase.
print(a.upper())

# convert all character into lowercase.
print(a.lower())

b = " Honey bunny "

# Remove spaces from string. if string start and ends with space.
print(a.strip())

# It will split the string and return as list items. It will split at the given character in method.
print(b.split(" ")) 

c = "Hi !!!"
# remove any character which passes through this methods.
print(c.rstrip("!"))

# It will replace the string. In this case 'Hi' will replace with 'Hello'.
print(c.replace("Hi","Hello"))

d = "hello friends."

# This method will capitalize the first letter of string.
print(d.capitalize()) 

# This method will add . or character passes through this method in this string to center the string.
print(d.center(20,"."))

# This will count the given character in the string.
print(d.count("l"))

e = "100 days codding challenge !!!"

# This will check if the string is starts with the given character or not this returns boolean value.
print(e.startswith("100"))

# This will check if the string is ends with the given character or not this returns boolean value.
print(e.endswith("!!!"))

# This will find the given character in the string and return the index in which the character is present.
print(e.find("days"))

# Return the index of given character from the string.
print(e.index("100"))

# This method will swap whole string from lower into upper or upper into lower case.
print(e.swapcase())

# This will capitalizes all the first letter of words of the string.
print(e.title())



