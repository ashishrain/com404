#code to demonstrate the use of return values

#function to calculate the sum of weight
def sum_weights(weight_bop, weight_beep):
    #calculate the total weight
    total_weight = (weight_bop + weight_beep)
    #return the value total_weight
    return total_weight

#function to calculate the average weight
def calc_avg_weight(weight_bop, weight_beep):
    #create a variable to store the returned value from sum_weights()
    total = sum_weights(weight_bop, weight_beep)
    #calculate the average value
    avg_weight = (total / 2)
    #return the value of avg_weight
    return avg_weight

#function to run and ask for user input
def run():
    print("What is the weight of Bop?")
    weight_bop = int(input())

    print("What is the weight of Beep?")
    weight_beep = int(input())

    print("What would you like to calculate (sum or average)?")
    answer = input()

    if answer == "sum":
        print(sum_weights(weight_bop, weight_beep))
    elif answer == "average":
        print(calc_avg_weight(weight_bop, weight_beep))
    else:
        print("I don't understand that.")


run()