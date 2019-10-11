#Added code to demonstrate the use of a simple while loop

print("How many cables should I remove?")

#read user response
cables_to_be_removed = int(input())

#control variable
removed_cables = 0

#use control variable in loop condition
while (removed_cables < cables_to_be_removed):

    print("Removed cable")

    #update the current iteration count
    removed_cables = removed_cables + 1