# Day 84
# Time Module in pythons
# time.time() function return time in seconds
# if you want to check that how much time is taken by a function you can use time.time().
import time
# def loop():
#     for i in range(50000):
#         print(i)

# init = time.time()
# loop()
# t = time.time() - init
# print(t)

# time.sleep() function will start executing the function after given amount of time.

print("This is without sleep")
time.sleep(2)
print("This is with sleep")

# time.strftime() function will format time as per given format string.
t = time.localtime()
formatedTime = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatedTime)

