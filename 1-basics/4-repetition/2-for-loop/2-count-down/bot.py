#code to demonstrate counting down with a for loop

print("How far are we from the cave?")

#store the number in distance variable
distance = int(input())

#counter variable in for loop
for count in range(distance, 0, -1):
    
    #displaying distance
    print(str(count) + "steps remaining")

print("We have reached the cave!")