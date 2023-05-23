''' In Python, hybrid inheritance can be implemented by creating a class hierarchy, in which a base class is inherited by multiple derived classes, and one of the derived classes is further inherited by a sub-derived class. Syntax:

class BaseClass1:
      # attributes and methods

class BaseClass2:
  # attributes and methods

class DerivedClass(BaseClass1, BaseClass2):
  # attributes and methods

'''


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Person(Human):
    def __init__(self, name, age, address):
        Human.__init__(self, name, age)
        self.address = address

    def show_details(self):
        Human.show_details(self)
        print("Address:", self.address)


class Program:
    def __init__(self, program_name, duration):
        self.program_name = program_name
        self.duration = duration

    def show_details(self):
        print("Program Name:", self.program_name)
        print("Duration:", self.duration)


class Student(Person):
    def __init__(self, name, age, address, program):
        Person.__init__(self, name, age, address)
        self.program = program

    def show_details(self):
        Person.show_details(self)
        self.program.show_details()


program = Program("Computer Science", 4)
student = Student("John Doe", 25, "123 Main St.", program)
student.show_details()


# Overall, these classes represent a basic object-oriented structure for modeling humans, persons, programs, and students. The `show_details` methods are used to display the attributes of each object in a formatted manner.