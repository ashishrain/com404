#code to demonstrate the use of a user-defined function with multiple parameters

def climb_ladder(steps_left, steps_crossed):
    if(steps_left > steps_crossed):
        print("Still some way to go!")
    else:
        print("We are almost there!")

#calling the climb_ladder function and passing arguments
climb_ladder(5, 2)
climb_ladder(2, 5)