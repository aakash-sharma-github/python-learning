# Day 18
# while loop in python

a = 0
while(a < 5):
    print(a)
    a = a + 1
    
# with else
else:
    print("This is else.")

# do-while loop emulation in python

while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break