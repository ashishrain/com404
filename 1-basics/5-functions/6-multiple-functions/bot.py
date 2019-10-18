#code to demonstrate the implementation of multiple user defined functions

#function to print the characters with the steps
def display_ladder(steps):

    for count in range(0, steps, 1):
        print("| |")
        print("***")

    print("| |")

#function to ask for user input and call display_ladder function
def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    display_ladder(steps)


create_ladder()