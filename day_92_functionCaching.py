# Day 92
# Function Caching in python
# it store the previously computed result as cache and when the same calculation dected the cached result will be returned.
# memoization means to store computed resullt and can be retrieved witnout repeating same computation.
from functools import lru_cache
import time 

@lru_cache(maxsize = None)
def fx(n):
    time.sleep(2)
    return n * 2

# Stores it's computed resullt as cache.
print(fx(2))
print("done for 2")
print(fx(4))
print("done for 4")
print(fx(6))
print("done for 6")
# after retrieved from caching
print(fx(2))
print("done for 2")
print(fx(4))
print("done for 4")
print(fx(6))
print("done for 6")
