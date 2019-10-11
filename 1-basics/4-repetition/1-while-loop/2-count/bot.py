#code to demonstrate the use of a while loop with a counter

print("How many live cables must I avoid?")

#ask user for number of live cables
live_cables = int(input())

#control variable
no_of_live_cables = 0

#use of control variable in loop condition
while (no_of_live_cables < live_cables):

    print("Avoiding...")

    #update current iteration
    no_of_live_cables += 1

    #display the message with the updated iteration
    print("...Done! " + str(no_of_live_cables) + " live cable avoided!")

#display blank space
print()

#display the last message
print("All live cables have been avoided." )
