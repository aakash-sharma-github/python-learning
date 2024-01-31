# Day 71
# dir, __dict__, help method.
# dir is used for checking what methods are available in any datatype or functions as documentation
a = (1,"aakash",None)
# this will show you what methods can be applied to that datatype or functions.
print(dir(a))

# __dict__ is used to store any values in dictionary datatype.
class emp():
    def __init__(self, name, age, address,salary):
        self.name = name
        self.age = age
        self.address = address
        self.salary = salary

e = emp("Aakash", 20, "Nepal", 10000)
# this will give you all values in dictionary datatype.
print(e.__dict__)

# help will show the entire information about the given datatype, functions or methods as documentation.
# this will give me every information about tuple.
print(help(tuple))