''' Self parameter: The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
It must be provided as the extra parameter inside the method definition. '''
''' Let us Creating a Class & using Self parameter '''
class Person:
    name = "Harry"
    occupation = "Software Developer"
    networth = 10

    def info(self):
        print(f"{self.name} is a {self.occupation}")


''' Creating an Object: Object is the instance of the class used to access the properties of the class Now lets create an object of the class. '''
a = Person()
b = Person()
c = Person()

a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "HR"

print(a.name, a.occupation)
a.info()
b.info()
c.info()