''' Access Specifiers/Modifiers: Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.
Types of access specifiers: 
    1. Public access modifier
    2. Private access modifier
    3. Protected access modifier  '''


''' Public Access Specifier in Python: All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed. '''
class Employee:
    def __init__(self):
        self.name = "Harry"

a = Employee()
print(a.name)


''' Private Access Modifier: By definition, Private members of a class (variables or methods) are those members which are only accessible inside the class. We cannot use private members outside of class. 
In Python, there is no strict concept of "private" access modifiers like in some other programming languages. However, a convention has been established to indicate that a variable or method should be considered private by prefixing its name with a double underscore (__). This is known as a "weak internal use indicator" and it is a convention only, not a strict rule. Code outside the class can still access these "private" variables and methods, but it is generally understood that they should not be accessed or modified.
Name mangling: Name mangling in Python is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses. Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively.  '''
class Employees:
    def __init__(self):
        self.__name = "Harry2"

a = Employees()
# print(a.__name) # can't be accessed directly
print(a._Employees__name)   # can be accessed indirectly
print(a.__dir__())


''' Protected Access Modifier: In object-oriented programming (OOP), the term "protected" is used to describe a member (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses. 
In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_). For example, if a class has a method called _my_method, it is indicating that the method should only be accessed by the class itself and its subclasses.    '''
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())