#code to demonstrate the use of a user-defined function with a loop

def cross_bridge(distance):
    for count in range(0, distance, 1):
        print("crossed step")

    if distance < 5:
        print("we must keep going!")
    else:
        print("The bridge is collapsing!")


#calling the cross_bridge function with different values one being lesser than 5 and other being higher than 5
cross_bridge(3)
cross_bridge(6)