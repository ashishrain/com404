#code to demonstrate the use of a simple for loop

print("What level of brightness is required?")

#ask user for required brightness and store in required_brightness variable
required_brightness = int(input())

#using print for a blank space
print()

print("Adjusting Brightness...")

#using print for a blank space
print()

#using for loop to display the brightness
for brightness in range(2, required_brightness + 1, 2):

    #printing the updated brightness_level
    print("Beep's brightness level: " + (brightness * "*"))
    print("Bop's brightness level: " + (brightness * "*"))

print("Adjustment Complete!")