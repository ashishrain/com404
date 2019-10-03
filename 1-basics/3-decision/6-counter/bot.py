#code to demonstrate how a variable can be used as a counter

#asks users to enter a whole number
print("Please enter the first whole number.")
first_number = int(input())

print("Please enter the second whole number.")
second_number = int(input())

print("Please enter the third whole number.")
third_number = int(input())

#created counters for both even and odd which is set to 0 as there is no odd numbers right now
even_counter = 0
odd_counter = 0

#checks if it is even or odd and adds 1 to relevant counters/variable
if (first_number % 2 != 0):
    odd_counter += 1
else:
    even_counter += 1

if (second_number % 2 != 0):
    odd_counter += 1
else:
    even_counter += 1

if (third_number % 2 != 0):
    odd_counter = odd_counter + 1
else:
    even_counter += 1

print("There were " + str(even_counter) + " even and " + str(odd_counter) + " odd numbers.")