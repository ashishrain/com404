#code to demonstrate the use of function

def spideySense(enemy, direction):

    #using if statement
    if (enemy == "Green Goblin"):
        print("Goblin bombs incoming from " + direction)
    elif (enemy == "Venom"):
        print("Venomous webbing incoming from " + direction)
    elif (enemy == "Electro"):
        print("Electro striking from " + direction)
    else:
        print("New enemy attacking from " + direction)

#testing
spideySense("Green Goblin", "front")
spideySense ("Venom", "behind")
spideySense ("Electro", "left side")
spideySense ("Unknown", "right side")