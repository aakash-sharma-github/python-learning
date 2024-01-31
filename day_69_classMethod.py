# Day 69
# class method in python.
class employee:
    company = "Apple Inc." # class variable.
    def show(self):
        print(f"Name: {self.name}, Company: {self.company}")

    @classmethod #You can change class variable's value by using @classmethod decorator
    def change(cng, newname):
        cng.company = newname

emp = employee()
emp.name = "Aakash"
emp.show()

# Changing class variable's value
emp.change("Google Inc")
print(employee.company)