# Day 16
# Match case statement
# It is just like switch case like c, c++, java.
# In python's match case using break is optional.
a = int(input("Enter a number:"))

match a:
    case 0:
        print("a is zero.")

    case 2 if (a % 2 == 0) :
        print("a is even number and case is 2.")

    case 4 if(a >= 1 and a <= 10):
        print("a is between 1-10. case 4")
    case _:
        print("Invalid input.")
    