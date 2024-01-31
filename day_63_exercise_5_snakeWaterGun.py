# Day 63
# Snake water and gun game in python.

import random

def check(com, user):
    if com == user:
        return 0

    if com == 0 and user == 1:
        return -1

    if com == 1 and user == 2:
        return -1

    if com == 2 and user == 0:
        return -1

    return 1

com = random.randint(0,2)
user = int(input("0 for snake, 1 for water, 2 for gun:\n"))

score = check(com, user)
print(f"You choosed: {user}")
print(f"Computer choosed: {com}")

if(score == 0 ):
    print("Game draw")

elif(score == 1):
    print("You won")

elif(score == -1):
    print("You loose")

else:
    print("Invalid input")

