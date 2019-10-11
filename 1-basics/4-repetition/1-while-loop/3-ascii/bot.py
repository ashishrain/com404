#Added code to demonstrate the use of a while loop with ascii art.

#ask how many bars should be charged
print("How many bars should be charged?")

#variable to store bars charged
bars_charged = int(input())

#control variable
no_of_bars_charged = 0

#use of control variable in loop
while(no_of_bars_charged < bars_charged):

    print("Charging:")

    #update the iteration
    no_of_bars_charged += 1

    #display the no of bars charged with updated iteration
    print(no_of_bars_charged * """ █ """)

#display the fully charged message
print("The battery is fully charged.")