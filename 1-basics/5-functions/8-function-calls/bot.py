#code to demonstrate the use of multiple function calls

print("Please enter a word?")
#creating a variable to store the word the user typed in
word = input()

print("Please choose what you want to do (in numbers)?")
print("1) display in a Box")
print("2) display lowercase")
print("3) display uppercase")
print("4) display mirrored")
print("5) Repeat")

#creating a variable to store the option chosen by the user
answer = input()

#a function to display in a box
def display_box():
     print("*" * (len(word) + 4))
     print("* " + word + " *")
     print("*" * (len(word) + 4))

#a function to display lowercase
def lower_case():
    #return the lowercase values of the argument
    return word.lower()

#a function to display uppercase
def upper_case():
    #return the uppercase values of the argument
    return word.upper()

#a function to display mirrored
def mirrored():
    sum = ""
    for position in range(len(word), 0, -1):
        sum = sum + word[position -1]
    return sum

#a function to display repeat
def repeat(repeat_no):
    repeat_lower = lower_case()
    repeat_upper = upper_case()
    for count in range(0, repeat_no, 1):
        if (count % 2 != 0):
            print(repeat_lower)
        else:
            print(repeat_upper)



#a function to run
def run():
    if (answer == "1"):
        display_box()
    
    elif (answer == "2"):
        print(lower_case())
    
    elif (answer == "3"):
        print(upper_case())
    
    elif (answer == "4"):
        print(mirrored())
    
    elif (answer == "5"):
        print("How many times do you want it to repeat?")
        repeat_no = int(input())
        repeat(repeat_no)

run()