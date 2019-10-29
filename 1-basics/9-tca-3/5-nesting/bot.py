#code to demonstrte the use of nesting

#displaying the welcome message
print("Welcome to the Planet of the Apes...")

#control variable for the humans
humans_encountered = 0

#control varaiable for the apes
apes_encountered = 0

#using for loop
for count in range(0, 7, 1):

    #asking user if they are ape or human
    print("... be ye human or be ye ape?")
    encountered = input()

    #using if statement
    if (encountered == "Human"):
        #add 1 to humans_encountered
        humans_encountered = humans_encountered + 1
        print("I did not start this war. But I will finish it.\n")
    elif (encountered == "Ape"):
        apes_encountered = apes_encountered + 1
        print("Apes together strong!\n")
    else:
        print("This is not your fight.\n")

#displaying the total number of Apes and Humans
print("Total humans encountered: " + str(humans_encountered))
print("Total apes encountered: " + str(apes_encountered))