'''Hierarchical Inheritance is a type of inheritance in Object-Oriented Programming where multiple subclasses inherit from a single base class. In other words, a single base class acts as a parent class for multiple subclasses. This is a way of establishing relationships between classes in a hierarchical manner. Syntax:

class BaseClass:
    pass
class D1(BaseClass):
    pass
class D2(BaseClass):
   pass
class D3(D1):
   pass
   
'''


class Animal:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print("Name:", self.name)


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print("Species: Dog")
        print("Breed:", self.breed)


class Cat(Animal):
    def __init__(self, name, color):
        Animal.__init__(self, name)
        self.color = color

    def show_details(self):
        Animal.show_details(self)
        print("Species: Cat")
        print("Color:", self.color)


dog = Dog("Max", "Golden Retriever")
dog.show_details()
cat = Cat("Luna", "Black")
cat.show_details()


# Overall, these classes represent a basic object-oriented structure for modeling animals, specifically dogs and cats. The `show_details` methods are used to display the attributes of each animal in a formatted manner. By using inheritance, the `Dog` and `Cat` classes inherit the attributes and methods of the `Animal` class, allowing for code reuse and specialization of behavior.
