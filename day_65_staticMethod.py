# Day 65
# static method
# You cannot use any function inside class without using self keyword.
# But using staticmethod decorator you can use.

class math:
    # this is a addition function inside class.
    def __init__(self, num): # constructor of setter.
        self.num = num

    def addToNum(self, num1):
        self.num = self.num + num1
    
    # this is a addition function inside class without using self keyword.
    @staticmethod
    def add(a, b):
        return a + b

a = math(2) # set in setter.
a.addToNum(4) 
print(a.num)

print(math.add(5,6)) # accessing function inside class without using self keyword.
# classname.functionname(values).
