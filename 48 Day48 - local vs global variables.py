'''Local & Global Variables'''
x = 4
print(x)

def hello():
    x = 5
    print(f"The local x is {x}")
    print("Hello harry")
print(f"The global x is {x}")
hello()
x = 5 
print(f"The global x is {x}")


'''The Global Keyword'''
x = 10  # global variable

def my_function():
  global x
  x = 6  # this will change the value of the global variable x
  y = 5  # local variable
  print(y)

my_function()
print(x)  # prints 6
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function