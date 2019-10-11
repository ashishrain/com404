#code to demonstrate the use of a while loop with len function

print("Please enter a phrase:")

#store the response to phrase variable
phrase = input()

phrase_length = len(phrase)

#control variable
control_var_phrase = 0

#use of control variable in while loop
while(control_var_phrase < phrase_length):

    print("Bop ")

    #update the control_var_phrase
    control_var_phrase += 1

