''' Here topics are :----
1. How importing in python works
2. from keyword
3. importing everything
4. The "as" keyword
5. The dir function
'''

from math import sqrt, pi
from math import pi, sqrt as s
import math as math_builtin_python

result = math_builtin_python.sqrt(9) * math_builtin_python.pi
print(result)  # Output: 9.42477796076938

# from harry import welcome, harry
from harry import *
import harry as hr
import math

print(dir(math))
print(math.nan, type(math.nan))
hr.welcome()
print(hr.harry)