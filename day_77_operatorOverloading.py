# Day 77
# Operators overloading in python.

# using function of that operator insted of using the operator.

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

def __str__(self):
    return (f"{self.i}i + {self.j}j + {self.k}k")

def __add__(self, x): # Adding vector using add function instead of + operator.
    return Vector(self.i + x.i, self.j + x.j, self.k + x.k)

v1 = Vector(3, 5, 7)
print(v1)

v2 = Vector(5, 8, 9)
print(v2)

print(v1 + v2)