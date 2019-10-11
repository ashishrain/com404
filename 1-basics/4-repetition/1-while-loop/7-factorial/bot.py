#code to demonstrate the use of a while loop in calculating the factorial of a number

#ask user to enter the number
print("Please enter a number:")
entered_number = int(input())

#control variable
control_number = 1

#variable to store the sum of all the multiplication
sum_of_mul = 1

#control variable in while loop
while(control_number <= entered_number):

    sum_of_mul = sum_of_mul * control_number 

    control_number += 1

#display the final result
print("The factorial is " + str(sum_of_mul))