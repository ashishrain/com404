#code to demonstrate the use of a logical and operator

#ask user what did i hear
print("What did I hear?")
hear = input()

#ask user what did i see
print("What did I see?")
see = input()

#decide what Beep should do
#if user inputs "grrr" and "two red eyes"
if ((hear == "grrr") and (see == "two red eyes")):
    print("There is a scary creature. I should get out of here!")

#if user inputs something else
else:
    print("I am a little scared but I will continue.")