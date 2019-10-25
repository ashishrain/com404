#code to demonstrate the use of nesting

#creating a varaible health which has value of 100
health = 100

#display the health to the user
print("Your health is 100%. Escape is in progress...\n")

#using for loop
for count in range(0, 5, 1):

    #ask what the user sees
    print("...Oh dear, who is that?")
    seen_object = input()

    #using if statement to find the object
    if (seen_object == "Smiler's Bot"):
        #subtracts 20 from health
        health = health - 20
        print("Time to jam out of here!\n")
    elif(seen_object == "Hacker"):
        #adds 20 to health
        health = health + 20
        print("Yay! Better follow this one!\n")
    else:
        print("Phew, just another emoji!")

#display the final health left
print("Escaped! Health is " + str(health) + "%")
