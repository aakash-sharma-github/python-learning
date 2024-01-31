# day 14
# if - else condition.

age = int(input("Enter your age:"))
# if
if(age < 18):
    print("You cannot drive.")
# if else
else:
    print("You can drive.")
# if elif else
num = int(input("Enter your number: "))

if(num < 0):
    print("Your number is negative.")

elif(num == 0):
    print("Your number is zero.")

else:
    print("Your number is positive.")

# nested if
num1 = int(input("Enter num1: "))
if(num1 < 0):
    print("Negative")

elif(num1 > 0):
    if(num1 < 10):
        print("Between 1-10")
    elif(num1 > 20 and num1 < 30):
        print("Between 20-30.")

elif(num1 == 0):
    print("Zero")

else:
    print("Positive.")