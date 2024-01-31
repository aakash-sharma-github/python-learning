# Day 37
# finally clause exception handling.
# finally keyword will always execute no matter code will generate error or not.

def multi():
    a = input("Enter a number: ")

    try:
        for i in range(1, 11):
            print(f"{int(a)} X {i} = {int(a)*i}")
            
    except Exception as e:
        print(e)
        # print("Invalid input")
        return 0

    finally:
        print("End of program") # this will always execute no matter function return value or not.
    print("I am print function.") # this will not execute if function returns some value.

multi()