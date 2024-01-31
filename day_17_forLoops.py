# Day 17
# loops in python
name = "saurabh"
for i in name:
    print(i)

# Nested for loop
animals = ['cat','dog','cow','donkey']
for ani in animals:
    print(ani)
    for an in ani:
        print(an)

# Range() in for loop
for a in range(8):
    print(a)

for b in range(1,10): # Will print 1-9
    print(b)

# step() method of range in loops

for c in range(1,20,5): # Will skip z index value in (n-1) form.
    print(c)

# Quick Quiz 
# Print Multiple Tables using for loop
tb = int(input("Enter number:"))
for t in range(1,11):
    print(tb,"x",t,"=",(tb*t))