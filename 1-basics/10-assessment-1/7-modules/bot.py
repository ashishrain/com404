#code to demonstrate the use of modules

#ask user to enter a phrase
print("Please a phrase")
entered_phrase = input()

#ask user to choose an option
print("Please choose an option (1 / 2 / 3 / 4)")
chosen_option = input()

#function for option_four
def option_one(phrase_to_grid):
    #ask user to enter the size of the grid
    print("Please enter the size of the grid")
    entered_size = int(input())

    #variable to store the first top line
    line = ((("--") + ("-" * len(entered_phrase))) * entered_size) + "--"

    #display line at top
    print(line)

    #using for loop
    for count in range(len(entered_phrase)):
        print("| " + ((entered_phrase + "  ") * (entered_size - 1)) + entered_phrase + " |")
    
    #display line at bottom
    print(line)

#function to display right angled triangle
def option_two(entered_phrase):
    #using for loop
    for rows in range(len(entered_phrase)):
        #using nested loop for columns
        for cols in range(rows + 1):
            print(entered_phrase[cols], end="")
        print()

#function to display right sided triangle
def option_three(entered_phrase):
    #creating a variable to count the empty spaces
    empty_spaces = len(entered_phrase)

    #using for loop
    for rows in range(1, len(entered_phrase) + 1):
        #decreasing the empty_spaces by 1
        empty_spaces = empty_spaces - 1
        #printing the empty spaces
        print(" " * (empty_spaces), end="")

        #using another for loop
        for cols in range(rows, 0, -1):
            print(entered_phrase[-cols], end="")
        
        print()

#function
def option_four(entered_phrase):
    print(entered_phrase[-1])

#using if statement
if (chosen_option == "1"):
    option_one(entered_phrase)

elif (chosen_option == "2"):
    option_two(entered_phrase)

elif (chosen_option == "3"):
    option_three(entered_phrase)

elif (chosen_option == "4"):
    option_four(entered_phrase)