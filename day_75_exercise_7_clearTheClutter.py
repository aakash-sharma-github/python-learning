# Day 75
# Exercise 7: clear the clutter.

import os

# os.rename("cluttered/sdfd.txt", "cluttered/test.txt") # rename file
i = 1
file = os.listdir("cluttered")
for png in file:
    if png.endswith(".png"):
        print(png)
        os.rename(f"cluttered/{png}",f"cluttered/{i}.png" )
        i = i + 1