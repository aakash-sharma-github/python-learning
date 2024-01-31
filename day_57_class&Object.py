# Day 57
# classes and objects.

# class is a template.
class employee:
    name = "Sukesh"
    idNo = 69
    occupation = "Chef"

# self is a keyword that is used to call an object.
    def example(self):
        print(f"{self.name} is a {self.occupation}.")

# object is raw information that to be filled in class as a template.
s = employee()
s.name = "Aakash"
s.occupation = "Assistant Chef"

# print(s.name)
# example(s) # this will work if your function is not inside the class.
s.example() # this will work normally.