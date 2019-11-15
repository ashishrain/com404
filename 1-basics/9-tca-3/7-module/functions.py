#contains the functions for the program to manipulate numbers

#ask user to enter the 5 digit numbers
print("Please enter 5 digit numbers")
entered_numbers = input()

#ask user to choose any one options
print("Please choose any one of the following functions:")
print("1) Display ASCII Triangle")
print("2) Display Left Digits Triangle")
print("3) Display Right Triangle")
chosen_option = input()

#function for displaying a ascii triangle
def option_one(nums_to_manipulate):
    print("*")
    print("**")
    print("***")
    print("****")
    print("*****")
    print("******")
    print("*******")
    print("********")
    print("* " + nums_to_manipulate + " *")
    print("**********")

#function for displaying left digits triangle
def option_two(nums_to_manipulate):    
    #using for loop to perform left digits triangle
    for count in range(0, len(nums_to_manipulate) + 1, 1):
        for count_two in range(0, count, 1):
            print(nums_to_manipulate[count_two],end="")
        print()

#function for displaying right triangle
def option_three(nums_to_manipulate):
    #print("    " + nums_to_manipulate[0])
    #print("   " + nums_to_manipulate[0] + nums_to_manipulate[1])
    #print("  " + nums_to_manipulate[0] + nums_to_manipulate[1] + nums_to_manipulate[2])
    #print(" " + nums_to_manipulate[0] + nums_to_manipulate[1] + nums_to_manipulate[2] + nums_to_manipulate[3])
    #print(nums_to_manipulate)
    for count in range(0, len(nums_to_manipulate)):
        print(" " * len(nums_to_manipulate) - 1 + nums_to_manipulate[count])


#using if statement to perform specific tasks given by users
if (chosen_option == "1"):
    option_one(entered_numbers)
elif (chosen_option == "2"):
    option_two(entered_numbers)
elif (chosen_option == "3"):
    option_three(entered_numbers)
else:
    print("The option cannot be recognized. Please try again.")