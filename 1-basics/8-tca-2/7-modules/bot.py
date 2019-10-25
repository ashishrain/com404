#code to demonstrate modules

#ask user for the word
print("Please enter a word")
entered_word = input()

#function to perform if user chooses option 1
def option_one(entered_word):
    print(entered_word)
    print("*" * len(entered_word))

#function to perform if the user chooses option 2
def option_two(entered_word):
    print("*" * len(entered_word))
    print(entered_word)

#function to perform if the user chooses option 3
def option_three(entered_word):
    print("*" * len(entered_word))
    print(entered_word)
    print("*" * len(entered_word))

#function to perform if the user chooses option 4
def option_four(entered_word):
    #ask user for size of the grid
    print("Please enter what size would you like for the grid?")
    entered_size = int(input())

    #using for loop for displaying the grid

    for row in range(0, entered_size, 1):

        line = "*" * len(entered_word)

        # display top line
        print( (line + "   ") * entered_size)

        # display word

        print( ((entered_word + " | ") * (entered_size - 1)) + entered_word)

        # display bottom line
        print( (line + "   ") * entered_size)



#ask user to choose an option
print("Please choose an option (1 / 2/ 3/ 4)")
chosen_option = input()

#using if statement to decide what to do
if (chosen_option == "1"):
    option_one(entered_word)

elif (chosen_option == "2"):
    option_two(entered_word)

elif (chosen_option == "3"):
    option_three(entered_word)

elif (chosen_option == "4"):
    option_four(entered_word)