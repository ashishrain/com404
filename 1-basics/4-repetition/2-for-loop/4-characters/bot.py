#code to demonstrate the use of for loops in string indexing

print("What strange markings do you see?")

markings = input()

print("Identifying...")

print()

for position in range(0, len(markings), 1):

    print("index " + str(position) + ": " + markings[position])

print("Done!")