# Day 46
# OS modules

import os

# if( not os.path.exists("test")): # this will check if the folder exists if not then will execute the below command.
#     os.mkdir("test") # this will make a folder with given name.

# for i in range(0, 5):
#     os.mkdir(f"test/test{i+1}") # this will make 5 new folder inside the test folder.

# for i in range(0, 5):
#     os.rename(f"/test/test{i+1}", f"/data/day_{i+1}") # this will rename test folder to day all at once.

files = os.listdir("test") # this will list all files inside the test folder.

# print(os.getcwd()) # this will print the the current working directory.
# print(os.chdir("test")) # this will change the working directory to test folder.

for f in files:
    print(os.listdir(f"test/{files}"))
