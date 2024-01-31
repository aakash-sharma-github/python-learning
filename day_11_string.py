# day 11
# strings in python.

name = "Aakash"
print(name)

# string using escape sequence for using ('),("") in your strings.
str = "Today\'s news."
print(str)

# Multiline strings.
# We can use triple double quote " or triple single quote ' to write multiline strings in python.
mul = """ Hello friends,
            Today is day 11 of 100 day of codding challenge. """

print(mul)

# Indexing always starts with 0 in python.
# Aakash is of 6 letters but our index starts from 0 so it will ends in 5.
print(name[0]) # print A.
print(name[1]) # print a.
print(name[2]) # print k.
print(name[3]) # print a.
print(name[4]) # print s.
print(name[5]) # print h.
print("\n Using for loop. \n") # This escape sequence create next line.

# We can also use for loops in strings to print index wise.
for chr in name:
    print(chr)
