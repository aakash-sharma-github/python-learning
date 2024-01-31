# Day 91
# Generators in python
# yield keyword is used for generator
# It is used to generate or iterate values on the go.
# It doesn't store all the values in the memory. It only stores the values that user are asking for.
# To generate values you can use next() or for loop. by using the next() function you can generate next value to be printed.
# use for loops for iterate it all at once.

def generate():
    for i in range(50):
        yield i

gen = generate()
# only generate next values.
# it is kind of lazy.
# it only generates next values when you ask for by using the next() function.
# print(next(gen))
# print(next(gen))
# print(next(gen))

# iterating upto given values.
for j in gen:
    print(j)