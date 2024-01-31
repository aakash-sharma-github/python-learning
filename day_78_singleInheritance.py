# Day 78
# single inheritance
# single inheritance is that which is only child of the parent class.
# Quick quiz: create a cat ckass by using animal class. Add some methods specific to cat.
class animal:
    def __init__(self, name,owner):
        self.name = name
        self.owner = owner

    def sound(self):
        print(f"{self.name} Bark!!!")

class cat(animal):
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} Meuw Meuw!!!!")

c = cat("cat")
c.sound()

a = animal("dog", "Sudi")
a.sound()
