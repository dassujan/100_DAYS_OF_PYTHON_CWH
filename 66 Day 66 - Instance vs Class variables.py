# Class Variables: Class variables are defined at the class level and are shared among all instances of the class. They are defined outside of any method and are usually used to store information that is common to all instances of the class. 
# Instance Variables: Instance variables are defined at the instance level and are unique to each instance of the class. They are defined inside the init method and are usually used to store information that is specific to each instance of the class. 


class Employee:
    companyName = "Apple"
    noOfEmployees = 0

    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmployees += 1

    def showDetails(self):
        print(
            f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

# Employee.showDetails(emp1)
emp1 = Employee("Harry")
emp1.raise_amount = 0.3
emp1.companyName = "Apple India"
emp1.showDetails()
Employee.companyName = "Google"
print(Employee.companyName)

emp2 = Employee("Rohan")
emp2.companyName = "Nestle"
emp2.showDetails()