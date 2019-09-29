#reads the numbers of lives and stores into variable lives
print("Please enter the number of lives.")
lives = int(input())

#reads the number of energy level and stores into variable energy
print("Please enter the energy level.")
energy = int(input())

#reads the number of shield level and stores into variable shield
print("Please enter the shield level.")
shield = int(input())

print("Health has been set.")

#displays lives, energy level and shield
print("Lives: " + ("♥" * lives) )
print("Energy: " + ("●" * energy) )
print("Shield: " + ("♦" * shield) )