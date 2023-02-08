''' Python Inheritance Syntax:
        class BaseClass:
            Body of base class
        class DerivedClass(BaseClass):
            Body of derived class
Derived class inherits features from the base class where new features can be added to it. This results in re-usability of code.    '''

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("The default langauge is Python")

e1 = Employee("Rohan Das", 400)
e1.showDetails()
e2 = Programmer("Harry", 4100)
e2.showDetails()
e2.showLanguage()
