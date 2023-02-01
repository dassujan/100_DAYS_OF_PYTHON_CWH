'''Lambda Function Syntax: lambda arguments: expression
Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce. '''


# def double(x):
#   return x*2

def appl(fx, value):
    return 6 + fx(value)

def double(x): return x * 2
def cube(x): return x * x * x
def avg(x, y, z): return (x + y + z) / 3

print("Double: ", double(5))
print("Cube: ", cube(5))
print("Average: ", avg(3, 5, 10))
print("Double in function: ", appl(double, 2))  # 6+double(2)=10
print("Triple in function: ", appl(lambda x: x * x * x, 2))   # 6+(2*2*2)= 14