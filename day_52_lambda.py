# Day 52
# lambda function
# Syntax
# variableName = lambda 'argument': expression
# lambda is a used when a function is required for short expression.
# You don't need to write a function for a short expression just use lambda function.
def value(fx, val):
    return fx(val) * 2 # fx(val) will take the value which is came from below and * 2.

add = lambda a: a + 5
avg = lambda a,b,c: (a + b + c)/3

print(add(2))
print(avg(5, 2, 8))

# you can also do this
print(value(add,5))
print(value(lambda x: x + 5, 7)) # 7 will be the value of lambda x and this value will go in value function above.