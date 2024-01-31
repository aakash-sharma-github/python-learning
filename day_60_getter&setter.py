# Day 60
# Getter and setter in python.
class myClass:
    # constructor that is taking a value.
    # constructor is compulsory to write getter and setter.

    def __init__(self, value): # in value variable value comes from setter.
        self._value = value

    # this function is printing the value.
    def show_value(self):
        print(f"value is: {self._value}") # There the value from setter is printed.

    # this is getter.
    @property
    def multiple(self):
        return 5 * self._value # There the value from setter is calculated.
    
    # this is setter.
    @multiple.setter
    def multiple(self, newvalue):
        self._value = newvalue + 10

cls = myClass(5)  # this value get ignored but it is compulsory because constructor is taking a argument.
cls.multiple = 12 # this value set in setter and added .
print(cls.multiple) # printing getter.
cls.show_value() # calling the function that is printing the setter value.
