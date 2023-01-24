# def average(a, b, c=1):
#   print("The average is ", (a + b + c) / 2)


def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)
name("Amy")


def average(*numbers):
  print(type(numbers))      # argument value as tuple
  sum = 0
  for i in numbers:
    sum = sum + i
  # print("Average is: ", sum / len(numbers))
  # return 7
  return sum / len(numbers)


# average(4, 6)
# average(b=9)

# c = average(5)
c = average(5, 6, 7, 1)
print(c)


def name(**name): 
  print(type(name))     # argument value as dict
  print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname="Buchanan", lname="Barnes", fname="James")