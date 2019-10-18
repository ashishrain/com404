#code to demonstrate the use of a user-defined function with a parameter

def escape_by(plan):
    if(plan == "jumping over"):
        print("We cannot escape that way! The boulder is moving too fast!")
    elif(plan == "going deeper"):
        print("That might just work! Let's go deeper!")
    else:
        print("We cannot escape that way! The boulder is in the way!")

#calling the escape_by function with three different values
escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")