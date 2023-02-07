''' Getters in Python are methods that are used to access the values of an object's properties. They are used to return the value of a specific property, and are typically defined using the @property decorator.
It is important to note that the getters do not take any parameters and we cannot set the value through getter method.For that we need setter method which can be added by decorating method with @property_name.setter    '''

class MyClass:
    def __init__(self, value):
        self._value = value      # the MyClass class has a single property, _value, which is initialized in the init method. 

    def show(self):
        print(f"Value is {self._value}")   # writing show method 

    @property
    def value(self):
        return self._value     # The value method is defined as a getter using the @property decorator, and is used to return the value of the _value property.

    @property
    def ten_value(self):
        return 10 * self._value     # creating new method which is 10 times of value as a getter using the @property decorator

    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10     # we just want setting new value as a setter using the @property_name.setter

# To use the getter, we can create an instance of the MyClass class, and then access the value property
obj = MyClass(10)
print(obj._value)
obj.show()
# setter method like this
obj.ten_value = 67
print(obj.ten_value)
obj.show()

''' In conclusion, getters are a convenient way to access the values of an object's properties, while keeping the internal representation of the property hidden. This can be useful for encapsulation and data validation. '''