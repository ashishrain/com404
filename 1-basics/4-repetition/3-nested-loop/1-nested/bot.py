#code to demonstrate the use of one loop nested is another

#ask how many rows user would like
print("How many rows would you like?")
rows = int(input())

#using print for space
print()

#ask how many columns user would like
print("How many columns would you like?")
columns = int(input())

#using print for space
print()

print("Here I go:")

#using print for space
print()

#use of for loop to display the grid of emojis
#use of for loop to display the rows
for count in range(0, rows, 1):

    #use of another nested for loop to create columns
    for number in range(0, columns, 1):

        #using end="" to specify that an empty string ("") should be added to the end of the printed line instead of a new line (\n)
        print(":)", end="")

    #using print fucntion to make the next emojis start from the next line instead of it piling next to eachother
    print()

print("Done!")