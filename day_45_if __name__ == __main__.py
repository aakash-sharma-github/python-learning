# Day 45
# if __name__ == "__main__":
# it is used for a function that you are importing.
# only importing can also run any module in your system.
# To avoide that and making program execute only that we want to be executed we use ' if __name__ == "__main__": '.

# example

from day_45a import notUsing

notUsing() # this will print the statement multiple times because in day_45a file function is printing.

from day_45a import using

using() # this will not print the statement multiple times because in day_45a file i have used ' if __name__ == "__main__": '