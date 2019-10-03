#code to demonstrate the use of a logical or operator

#ask what type of adventure user want
print("What type of adventure should I have?")
ad_type = input()

#decide the adventure
#if user decides "scary" or "short"
if ((ad_type == "scary") or (ad_type == "short")):
    print("Entering the dark forest!")

#if user decides "safe" or "long"
elif ((ad_type == "safe") or (ad_type == "long")):
    print("Taking the safe route!")

#if user decides something else
else:
    print("Not sure which route to take.")