''' Multiple inheritance is a powerful feature in object-oriented programming that allows a class to inherit attributes and methods from multiple parent classes. This can be useful in situations where a class needs to inherit functionality from multiple sources. '''

class Employee:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"Her name is {self.name} & dance is {self.dance}")

class DancerEmployee(Dancer, Employee):
  def __init__(self, dance, name):
    self.dance = dance
    self.name = name

o  = DancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
o.show() 
print(DancerEmployee.mro())

''' DocX Link: https://docs.python.org/3/reference/datamodel.html 
Python follows a method resolution order (MRO) to resolve conflicts between methods or attributes from different parent classes. The MRO determines the order in which parent classes are searched for attributes and methods.'''


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")
        
class Mammal:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color
        
class Dog(Animal, Mammal):
    def __init__(self, name, breed, fur_color):
        Animal.__init__(self, name, species="Dog")
        Mammal.__init__(self, name, fur_color)
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")

# In this example, the Dog class inherits from both the Animal and Mammal classes, so it can use attributes and methods from both parent classes.