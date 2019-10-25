#code to perform decision making

#ask user where is Forky
print("Where is Forky?")
forky_location = input()

#using if statement to decide
if (forky_location == "With Bonnie"):
    print("Phew! Bonnie will be happy.")
elif (forky_location == "Running away"):
    print("Oh no! Bonnie will be upset!")
else:
    print("Ah! I better look for him.")