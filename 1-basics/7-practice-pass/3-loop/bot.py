#code to use loop

#ask user how many miles
print("How many miles must I travel before I reach the secret base?")
miles_to_travel = int(input())

print("I will count the miles...\n")

#using for loop to count the miles
for count in range(miles_to_travel, 0, -1):
    print("I have " + str(count) + " miles to go before I reach the base.")

#displaying the final message
print("\nI have arrived at the secret headquarters of the MIB!")
print("It is time to sneak in.")