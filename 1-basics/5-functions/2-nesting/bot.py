#code to demonstrate the use of a user-defined function with a nested decision

def identity():
    print("What lies before you?")
    objects = input()
    if (objects == "a large boulder"):
        print("It's time to run!")
    else:
        print("we will be fine")

identity()