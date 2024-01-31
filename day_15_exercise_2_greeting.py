# Day 15
# Exercise 2: Greeting according to time.
import time
tm = time.strftime('%H:%M:%S')
hours = int(time.strftime('%H'))
print(hours)

tm = int(time.strftime('%H'))
if(tm >= 00 and tm <= 11):
    print("Good morning.")

elif(tm >= 12 and tm <= 15):
    print("Good Afternoon.")

elif(tm >= 16 and tm <= 19):
    print("Good Evening.")

else:
    print("Good Night.")
