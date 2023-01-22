x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")
        # Empty case with if-condition
    case _ if x != 90:
        print(x, "is not 90")
    case _ if x != 80:
        print(x, "is not 80")
        # default case(will only be matched if the above cases were not matched)
        # so it is basically just an else:
    case _:
        print(x)