# Class Methods in Python

In Python, classes are used to define objects that have certain properties and methods. A method is a function that is associated with a class, and it is used to define the behavior of the objects that are created from the class.

Here are some commonly used class methods in Python:

## __init__ method

The `__init__` method is a special method that is automatically invoked when you create a new instance of a class. This method is responsible for setting up the object’s initial state, and it is where you would typically define any instance variables that you need. This method is also called the "constructor".

## __str__ and __repr__ methods

The `__str__` and `__repr__` methods are both used to convert an object to a string representation. The `__str__` method is used when you want to print out an object, while the `__repr__` method is used when you want to get a string representation of an object that can be used to recreate the object.

## __call__ and __len__ methods

The `__call__` method is used to make an object callable, meaning that you can pass it as a parameter to a function and it will be executed when the function is called. This is an incredibly powerful tool that allows you to create objects that behave like functions.

The `__len__` method is used to get the length of an object. This is useful when you want to be able to find the size of a data structure, such as a list or dictionary.