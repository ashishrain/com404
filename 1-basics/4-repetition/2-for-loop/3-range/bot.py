#code to demonstrate the use of a simple for loop

print("What level of brightness is required?")

#store the brightness
required_brightness_level = int(input())

print("Adjusting brightness...")

for brightness in range(2, required_brightness_level + 1, 2):
    print("Beep's brightness level: " + (brightness * "** "))
