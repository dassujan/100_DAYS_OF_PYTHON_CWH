''' "is" keyword compares exact location of object in memory! '''
''' "==" operator compares the values! '''


a = [1, 2, 3]
b = [1, 2, 3]
print("a == b for list : ", a == b)  # True
print("a is b for list : ", a is b)  # False


a = "hello"
b = "hello"
print("a == b for string : ", a == b)  # True
print("a is b for string : ", a is b)  # True


a = 5
b = 5
print("a == b for int : ", a == b)  # True
print("a is b for int : ", a is b)  # True


a = (1, 2)
b = (1, 2)
print("a == b for tuple : ", a == b)  # True
print("a is b for tuple : ", a is b)  # True


a = None
b = None
print("a is b : ", a is b)  # exact location of object in memory
print("a is None : ", a is None)  # exact location of object in memory
print("a == b : ", a == b)  # value