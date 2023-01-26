# The shorthand syntax can be a convenient way to write simple if-else statements, especially when you want to assign a value to a variable based on a condition.
# result = value_if_true if condition else value_if_false

a = 330000
b = 3303
print("A") if a > b else print("=") if a == b else print("B")

c = 9 if a > b else 0
print(c)