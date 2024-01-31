# Day 71
# super keyword
# super is used to call patent class's methods.
class emp:
    def __init__(self, name,  id):
        self.name = name
        self.id = id

class pro(emp):
    def __init__(self, name, id, lang):
        # Getting name and id from emp class which is parent class using super keyword.
        super().__init__(name, id)
        self.lang = lang

a = emp("Aakash", 21)
print(a.name, a.id)

b = pro("Sudi", 22, "python")
print(b.name, b.id, b.lang)