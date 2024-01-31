# Day 70
#  class methods as alternative constructor.
class employee:
    def __init__(self, name, salary,dep):
        self.name = name
        self.salary = salary
        self.dep = dep

    @classmethod
    def fromData(cls, data):
        return cls(string.split(",")[0], int(string.split(",")[1]), string.split(",")[2]) # This is alternative constructor use method.

emp = employee("Aakash", 10000, "HM")
print(emp.name, emp.salary, emp.dep)

# Suppose that you have data in below format.
string = "Aakash, 15000, cse"
emp1 = employee.fromData(string)
print(emp1.name, emp1.salary, emp1.dep)
