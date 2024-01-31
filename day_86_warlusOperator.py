# Day 86
# Warlus operator in python 
# it was first introduced in Python 3.8
# warlus operator :=
#warlus operator allows to change values of variables within any expression. 

# without using warlus operator

food = list()
while True:
    foods = input("What would you like? ")
    if foods == "bas":
        break
    food.append(foods)
print(food)

# using Warlus operator

foods = list()
while(food := input("What would you like? ")) != "bas":
    foods.append(food)
print(foods)