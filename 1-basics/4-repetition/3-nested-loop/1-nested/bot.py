#code to demonstrate the use of one loop nested is another

print("How many rows should I have?")

rows = int(input())

print("How many columns should I have?")

columns = int(input())

for count in range(0, rows, 1):
    for number in range(0, columns, 1):
        print(":)", end="")
    print()