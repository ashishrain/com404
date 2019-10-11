#code to demonstrate the use of a while loop in performing calculations with user input

print("How many numbers should I sum up?")

#store the numbers
no_of_sum = int(input())

#counter variable
counter_of_sum = 0

#a variable to store sum of all the entered numbers
sum_of_entered = 0

#store the number in a number variable
while(counter_of_sum < no_of_sum):

    #ask user to enter the number
    print("Please the number 1 of " + str(no_of_sum))

    #store the entered number in entered_no variable
    entered_no = int(input())

    #add the entered number to sum_of_entered
    sum_of_entered = sum_of_entered + entered_no

    #update the iteration
    counter_of_sum += 1

#display the final value
print("The answer is " + str(sum_of_entered))

