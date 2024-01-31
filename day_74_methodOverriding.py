# Day 74
# Method Overriding.
class addition:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        return self.a + self.b + self.c

class average (addition):
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        super().__init__(num1, num2, num3)

    def avg(self):
        return super().add() / 3 # using add function from addition class.

ad = addition(2,5,7)
print(ad.add())

av = average(8, 5, 3)
print(av.avg())