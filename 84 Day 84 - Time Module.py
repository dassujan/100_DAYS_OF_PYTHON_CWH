import time     # Imports the `time` module, which provides various functions related to time measurement and manipulation.

# Defines a function named `usingWhile()`, which uses a `while` loop to iterate from 1 to 500 and prints each value of `i`.
def usingWhile():
    i = 0
    while i < 500:
        i = i + 1
        print(i) 

# Defines a function named `usingFor()`, which uses a `for` loop and the `range()` function to iterate from 0 to 499 and prints each value of `i`.
def usingFor():
    for i in range(500):
        print(i)

# Measure the execution time of `usingFor()`
init = time.time()
usingFor()
t1 = time.time() - init

# Measure the execution time of `usingWhile()`
init = time.time()
usingWhile()
t2 = time.time() - init

print("Execution time of usingFor():", t1)
print("Execution time of usingWhile():", t2)

print(4)

# Pause the program for 3 seconds
time.sleep(3)

print("This is printed after 3 seconds")

# Get the current time and format it as a string
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print("Current time:", formatted_time)