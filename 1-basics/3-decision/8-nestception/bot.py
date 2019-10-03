#Added code to demonstrate the use of multiple nested statements

#ask user where to look
print("Where should I look? (in the bedroom/ in the bathroom/ in the lab)")
location = input()

#decide where to look
#if user decides to look in the bedroom
if (location == "in the bedroom"):

    #ask user where to look in the bedroom
    print("Where in the bedroom should I look? (under the bed/ somewhere else)")
    bedroom_location = input()

    #decide where to look in the bedroom
    if (bedroom_location == "under the bed"):
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery.")

#if user decides to look in the bathroom
elif (location == "in the bathroom"):

    #ask user where to look in the bathroom
    print("Where in the bathroom should I look? (in the bathtub/ somewhere else)")
    bathroom_location = input()

    #decide where to look in the bathroom
    if (bathroom_location == "in the bathtub"):
        print("Found a rubber duck but no battery")
    else:
        print("It is wet but I found no battery.")

#if user decides to look in the lab
elif (location == "in the lab"):

    #ask user where to look in the lab
    print("Where in the lab should I look? (on the table/ somewhere else)")
    lab_location = input()

    #decide where to look in the lab
    if (lab_location == "on the table"):
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")

#if user enters something else
else:
    print("I do not know where that is but I will keep looking.")