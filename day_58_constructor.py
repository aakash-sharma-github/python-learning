# Day 58
# constructor in python.
# Two types of constructor.
# paramerized constructor and default constructor.

class employee:
    name = ""
    occ = ""
    empid = 12

# constructor will automatically called every time when a object is created.
# syntax for the constructor
# self keyword automatically takes emp object 'in my case' as a argument.
# This is parameterized constructor which takes parameter along with self.
    def __init__(self, a, b):
        print("This is a parameterized constructor")
        self.name = a
        self.occ = b

    def info(self):
        print(f"{emp.name} is a {emp.occ}.")

emp = employee("Aakash", "Developer")
emp.info()

# default constructor don't take any arguments from object it only take self as a reference of a object.
class laptop():
    name = ""
    model = ""
    amount = 100000

# This is a default constructor which doesn't take any arguments.
    def __init__(self):
        print("This is a default constructor")
        

    def info(self):
        print(f"{self.model} is a model {self.name}.")

l = laptop()
l.name = "Asus"
l.model = "Tuf"

l.info()