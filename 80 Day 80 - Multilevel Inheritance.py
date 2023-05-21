''' Multilevel inheritance is a type of inheritance in object-oriented programming where a derived class inherits from another derived class. This type of inheritance allows you to build a hierarchy of classes where one class builds upon another, leading to a more specialized class. '''

# Here, we define a base class called `Animal`. It has an `__init__` method that initializes the `name` and `species` attributes of the object. The `show_details` method prints the name and species of the animal.
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")

# The `Dog` class is a subclass of `Animal`. It also has an `__init__` method that calls the `__init__` method of the `Animal` class to set the name and species. It sets the `breed` attribute specific to dogs. The `show_details` method is overridden to call the `show_details` method of the `Animal` class and print the breed.
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")

# The `GoldenRetriever` class is a subclass of `Dog`. It also has an `__init__` method that calls the `__init__` method of the `Dog` class to set the name and breed. It sets the `color` attribute specific to golden retrievers. The `show_details` method is overridden to call the `show_details` method of the `Dog` class and print the color.
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color

    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")


# This code creates an instance of the `Dog` class called `o` with the name "tommy" and the breed "Black". Then it calls the `show_details` method of `o`, which displays the name, species (which is set to "Dog"), and breed.
o = Dog("tommy", "Black")
o.show_details()
print(GoldenRetriever.mro())    # This line prints the Method Resolution Order (MRO) of the `GoldenRetriever` class. MRO determines the order in which methods are resolved in the inheritance hierarchy. The MRO is a linearization of the inheritance graph, and it helps in resolving method lookups in multiple inheritance scenarios.