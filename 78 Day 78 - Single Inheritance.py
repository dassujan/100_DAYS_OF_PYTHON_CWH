class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark!")

d = Dog("Dog", "Doggerman")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()

''' Consider a class named "Animal" that contains the attributes and behaviors that are common to all animals.
Then, The Dog class inherits all the attributes and behaviors of the Animal class, including the __init__ method and the make_sound method. Additionally, the Dog class has its own __init__ method that adds a new attribute for the breed of the dog, and it also overrides the make_sound method to specify the sound that a dog makes. '''

# Quick Quiz: Implement a Cat class by using the animal class. Add some methods specific to cat
class Cat(Animal):
    def __init__(self, name, carnivora):
        Animal.__init__(self, name, species="Cat")
        self.carnivora = carnivora
    def desc(self):
        print("Cat is an animal.")
c = Cat("Cat", "mew")
c.desc()
c.make_sound()