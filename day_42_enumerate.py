# Day 42
# Enumerate function in python
# this gives you index without writing any longer code for accessing index.
# it return tuple.

# example without Enumerate function.
fruits = ["apple", "orange", "banana", "mango", "papaya"]
index = 0

for fruit in fruits:
    print(fruit)
    if index == 2:
        print("Banana is my favorite.")
    index +=1


# example with Enumerate function

name = ["sudi", "aakash", "sukesh", "rohan", "fufu"]

for index,i in enumerate(name):
    print(i)
    if index == 1:
        print("Aakash is my name.")


# you can also start index from 1 with enumerate.
books = ["maths", "english", "physics", "chemistry", "computer", "accounting"]

for index,i in enumerate(books, start=1):
    print(f"{index}. {i}")

