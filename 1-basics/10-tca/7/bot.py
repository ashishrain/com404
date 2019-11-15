# Add your code below for question 7.

#ask user to enter a phrase and store it to entered_phrase variable
print("Please enter any phrase")
entered_phrase = input()

#first function to perform if value of chosen_option is "1"
def option_one(entered_phrase):
    print("-" * (len(entered_phrase)+4))
    print("| " + entered_phrase + " |")
    print("-" * (len(entered_phrase)+4))

#second function to perform if value of chosen_option is "2"
def option_two(entered_phrase):
    print(" " * (len(entered_phrase) + 1) + ("-" * (len(entered_phrase)+4)) )
    print(entered_phrase + " " + (("|" + (" " * (len(entered_phrase) + 2)) + "|")))
    print(" " * (len(entered_phrase) + 1) + ("-" * (len(entered_phrase)+4)) )

#third function to perform if value of chosen_option is "3"
def option_three(entered_phrase):
    print(("-" * (len(entered_phrase)+4)) + " " * (len(entered_phrase) + 1))
    print((("|" + (" " * (len(entered_phrase) + 2)) + "|")) + " " + entered_phrase)
    print(("-" * (len(entered_phrase)+4)) + " " * (len(entered_phrase) + 1))

#fourth function to perform if value of chosen_option is "4"
def option_four(entered_phrase):
    #ask user for grid sixe and store it in entered_grid_size variable
    print("Please enter the size of the grid")
    entered_grid_size = int(input())

    #declaring a variable name lined
    line = ("-" + "-" * len(entered_phrase) + "-")  * (entered_grid_size)

    print(line)

    #using for loop for displaying the grid
    for count in range(0, entered_grid_size, 1):

        print(("| ") + ((entered_phrase + " ") * entered_grid_size))

#ask user to choose an option and store it to chosen_option variable
print("Please choose an option (1 / 2 / 3 / 4)")
chosen_option = input()

#using if statement to decide what to do
#if the value of chosen_option is "1" do:
if (chosen_option == "1"):
    option_one(entered_phrase)

#if the value of chosen_option is "2" do:
if (chosen_option == "2"):
    option_two(entered_phrase)

#if the value of chosen_option is "3" do:
if (chosen_option == "3"):
    option_three(entered_phrase)

#if the value of chosen_option is "4" do:
elif (chosen_option == "4"):
    option_four(entered_phrase)

