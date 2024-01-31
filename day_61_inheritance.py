# Day 61
# Inheritance in python.
# Inheritance is a oops concept that is used to inherit property from it's parent class.
# no needs to write extra code for same task as existing class just inherit from parent class.
class employees:
    # constructor is setting values in the variables below.
    def __init__(self, name, dprt, id):
        self.name = name
        self.dprt = dprt
        self.id = id
    
    # printing the details.
    def details(self):
        print(f"id: {self.id} is {self.name} from {self.dprt}")

# let suppose i want to create a new class called student and i want to add some more details of student and all the details that have in employee class but i dont want to add students details in employee class.
# i will just inherit employee class this will allow me to use employee class properties and additional student class.
class student(employees):

    def showdetails(self):
        print(f"id: {self.id} is {self.name} from {self.dprt}")
        print("This is inherited block.")

emp = employees("Aakash", "CSE", 56)
emp.details()
std = student("Sudi","BHMCT",22)
std.showdetails()