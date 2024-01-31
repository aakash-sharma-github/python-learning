# Day 79
# Multiple inheritance.
# It have multiple parents usually it have two parents.

class employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Employee name: {self.name}")

class occupation:
    def __init__(self, occupation):
        self.occupation = occupation

    def show(self):
        print(f"work as a: {self.occupation}")

# class worker(employee, occupation): # this is inheriting class and here employee class is written first so employee class will execute first.
class worker(occupation, employee): # in this case occupation class will execute first.
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

work = worker("Aakash", "Student")
# print(work.show()) # it will only execute that class which is written first in inheriting class.
# you can check it by using mro method that which class is executed first.
print(worker.mro())
print(work.name)
print(work.occupation)
work.show()
