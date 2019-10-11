#code to demonstrate how to reverse a string using a for loop

print("What phrase do you see?")

phrase = input()

print("Reversing...")

#putting an empty string which will later add all the letters from phrase
sum_of_all = ""

#control varible in for loop
for letter in phrase:

    #adding current sum_of_all with position of phrase
    sum_of_all = letter + sum_of_all

print("The phrase is: " + str(sum_of_all))