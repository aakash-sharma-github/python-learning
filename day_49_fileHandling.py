# Day 49
# file handling in python

# it take two arguments filename and mode 
# r for reading, w for writing
# a for appending meaning you can add additional content to the file.
# for image, pdf, exe, or any other file mode will be 'rb' which is binary mode

# reading a file
# read mode is default if you not want to give mode to open.
o = open('requirement.txt', 'r')

text = o.read() 
print(text)
o.close() # close is important or use with statement.

# writing a file
# if you open file in write mode that do not exist then it will create a new file.
# this will erease previous content of the file.
o = open('requirement.txt', 'w')

o.write('python3 \n')
o.close()

# appending to a file
o = open('requirement.txt', 'a')

o.write('This is append mode. \n')
o.close()

# # with statement used for automatically close files.
with open('requirement.txt', 'a') as f:
    f.write('This is append mode using with statement.')