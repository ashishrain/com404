#code to demonstrate the use of summing with a while loop

print("Calculating the sum of the first 100 numbers...")

#control variable
counter_number = 0

sum_of_all = 0

#use of control variable in while loop
while(counter_number < 100):

    counter_number += 1
    

    #adding counter_number to sum_of_all
    sum_of_all = sum_of_all + counter_number


print("Done! The answer is " + str(sum_of_all))