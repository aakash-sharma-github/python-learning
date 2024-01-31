# Day 30
# Recursion in python
# function calling itself.
def factorial(n):
    if n==0 or n==1: 
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# Quick quiz
# print fibonacci series
def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num-1) + fib(num-2)

print(fib(2))