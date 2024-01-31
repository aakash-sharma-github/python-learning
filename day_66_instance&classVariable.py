# Day 66
# Instance variables and class variables.
# Instance variables are those that are defined in any object.
# Class variables are those that are defined inside any class.
class Employee:
    company = "Google Inc." # class variable

    def __init__(self, name):
        self.name = name
        self.salary = 1000

    def details(self):
        print(f"I am {self.name} i work at {self.company} and i make ${self.salary}")

emp = Employee("Aakash")
emp.salary = 5000 # This is Instance variables that is defined after object is created and will not effect any other object.
emp.company = "Microsoft Corporation" 
emp.details()


# I have not defined any instance variables for salary so it is taking default value.
emp1 = Employee("sudi")
emp1.details()
