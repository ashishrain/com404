#code to demonstrate the use of functions

#function to find whether the fusion shot has occured
def isFusionShot(slug_type_one, slug_type_two):
    #using if statement to find whether the value of slug types are same
    if (slug_type_one == slug_type_two):
        return True
    else:
        return False

#function to call the isFunctionShot and check it it matches "Infurnus" and "AquaBeek"
def isDefectiveShot(slug_type_one, slug_type_two):
    #using if statement
    if (isFusionShot(slug_type_one, slug_type_two) == False):
        #using if statement to find if matches "Infurnus" and "AquaBeek"
        if ((slug_type_one == "Infurnus" and slug_type_two == "AquaBeek") or (slug_type_one == "AquaBeek" and slug_type_two == "Infurnus")):
            return True
        else:
            return False
    else:
        return False

#function to run
def run():
    #ask user to enter the slug type
    print("Please enter the first slug type")
    slug_type_one = input()

    print("Please enter the second slug type")
    slug_type_two = input()

    #ask user to choose fusion or defective
    print("Please select fusion or defective")
    selection = input()

    #using if statement to call respective funtion
    if (selection == "fusion"):
        print(isFusionShot(slug_type_one, slug_type_two))
    elif (selection == "defective"):
        print(isDefectiveShot(slug_type_one, slug_type_two))
    else:
        print("Invalid selection. Please try again")

#run the program
run()