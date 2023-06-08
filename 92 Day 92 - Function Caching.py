'''In Python, function caching can be achieved using the functools.lru_cache decorator. The functools.lru_cache decorator is used to cache the results of a function so that you can reuse the results instead of recomputing them every time the function is called. The cache is stored in a regular Python dictionary, so it has a limited size. When the cache is full, the entries are deleted in the least recently used order.'''

import functools
import time

@functools.lru_cache(maxsize=None)
def fxn(n):
    time.sleep(5)
    return n*5

print(fxn(28))
print("done for 20")
print(fxn(2))
print("done for 2")
print(fxn(6))
print("done for 6")

print(fxn(28))
print("done for 20")
print(fxn(2))
print("done for 2")
print(fxn(6))
print("done for 6")
print(fxn(61))
print("done for 61")