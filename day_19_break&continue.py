# Day 19
# Break and continue statement in python.

# break

for i in range(1,11):
    if(i == 5):
        break   # Break will stop loop after given condition is true. Means loop ko chhor k nikal jao.
    print("5 X",i,"=",i*5)

# continue

for b in range(10):
    if(b == 8):
        continue # Continue will skip the given condition. means given condition ko skip kardo.
    print(b)
    
# Emulating do while.. using infinite do while loop can emulate in python
a = 0
while True:
    print(a)
    a = a + 1
    if(a == 5):
        break

