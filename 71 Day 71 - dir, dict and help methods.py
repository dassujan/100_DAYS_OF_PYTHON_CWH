''' dir(): The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what you can do with an object. 
__dict__: The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection. 
help(): The help() function is used to get help documentation for an object, including a description of its attributes and methods. '''


x = [1, 2, 3]
print(dir(x))
print(x.__add__)

print("----------------------------------------------------------------------")

x = (1, 2, 3)
print(dir(x))

print("----------------------------------------------------------------------")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1

p = Person("John", 30)
print(p.__dict__)

print(help(Person))
print(help(str))