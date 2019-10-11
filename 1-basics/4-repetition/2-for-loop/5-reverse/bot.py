#code to demonstrate how to reverse a string using a for loop

print("What phrase do you see?")

phrase = input()

print("Reversing...")

sum_of_all = ""

#control varible in for loop
for position in range(len(phrase), 0, -1):

    sum_of_all = sum_of_all + phrase[position - 1]

print("The phrase is: " + str(sum_of_all))