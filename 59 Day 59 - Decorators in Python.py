''' A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function. The basic syntax for using a decorator is the following:      
    @decorator_function
    def my_function():
    pass
The @decorator_function notation is just a shorthand for the following code:
    def my_function():
        pass
    my_function = decorator_function(my_function)

Practical use case: One common use of decorators is to add logging to a function. 
For example, you could use a decorator to log the arguments and return value of a function each time it is called:    '''

import logging
def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(
            f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b

''' In this example, the log_function_call decorator takes a function as an argument and returns a new function that logs the function call before and after the original function is called.   '''


def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello world")

@greet
def add(a, b):
    print(a+b)

# greet(hello)()
hello()
# greet(add)(1, 2)
add(1, 2)