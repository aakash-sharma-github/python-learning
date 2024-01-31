# Day 51
# Methods of file handling

# seek() allows you to read the contents of desired point.
# examples
# o = open('text1.txt', 'r')
# o.seek(5) # this will move to 5th character.
# rd = o.read(4) # this will print 4 characters after 5th character.

# # tell() tells you that in what position you are in after seek.
# print(o.tell()) # 9 is the current position after reading 4 character and seeking 5 character.

# print(rd)
# o.close() 

o = open('text1.txt', 'w')
o.write("Hello, world")
# truncated() allows you to write the desired character to the file.
o.truncate(5) # this will only write first 5 characters to the file.
