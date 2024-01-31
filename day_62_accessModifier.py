# Day 62
# Access modifier in python.
# In Python there is no access modifier concept.
# It is used for limiting the access of class variables and methods from a class and outside of a class.

# public access modifier is by default in python and can be accessed directly from anywhere.
# This is public can be accessed directly.
class employee:
    def __init__(self):
        self.name = "Aakash"

emp = employee()
print(emp.name)

# protected access modifier is can only be accessed from within the class.
# '__' is name mangling it cannot be directly accessible. It is treated as protected & private.
# '_' is convencional it can be accessed directly.

# private access modifier can be accessed from within the class and its subclasses / child classes.
# This is private can be accessed indirectly
class employee1:
    def __init__(self):
        self.__name = "Sudi"

emp1 = employee1()
# print(emp1.__name) # this will throw an error because '__' is an indication of private access modifier.
print(emp1._employee1__name) # you can access using '_classname__variablename'.
# This is called name mangling. it is a technique so that the variable name have '__' in it can be accessed.
