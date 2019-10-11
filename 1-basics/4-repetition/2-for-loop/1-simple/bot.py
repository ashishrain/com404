#code to demonstrate the use of a simple for loop

print("How many mountains should I display?")

#store amount to no_of_display variable
no_of_display = int(input())

print("Displaying...")

for count in range(0, no_of_display, 1):

    print("""
           __
          /  \_  
         /^    \\
        /  ^    \_
      _/ ^ ^     ^\\
     /  ^     ^    \\
     """)