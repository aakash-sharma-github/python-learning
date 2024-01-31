# Day 80
# multilevel inheritance.
# suppose A is parent class and B is A's inherited child class and then c is created which is inheriting B class.
# It is also known as grandparent inheritance.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show(self):
        print(f"name: {self.name} species: {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species = "Dog")
        self.breed = breed

    def show(self):
        Animal.show(self)
        print(f"Breed: {self.breed}")

class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed = "Golden Retriever")
        self.color = color

    def show(self):
        Dog.show(self)
        print(f"Color: {self.color}")

gr = GoldenRetriever("tom", "white")
gr.show()