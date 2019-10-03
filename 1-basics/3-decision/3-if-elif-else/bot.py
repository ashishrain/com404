#code to demonstrate the use of an if...elif...else statement

print("Towards which direction should I paint (up, down, left or right)?")

#stores the user input in direction variable
direction = input()

#checks if the user input is up, down, left or right
if (direction == "up"):
    print("I am painting in the upward direction!")
elif (direction == "down"):
    print("I am painting in the downward direction")
elif (direction == "left"):
    print("I am painting in the left direction")
elif (direction == "right"):
    print("I am painting in the right direction")
else:
    print("I am painting in the other direction")