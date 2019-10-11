#code to demonstrate the use of a simple for loop

print("What level of brightness is required?")

#store the brightness
brightness_level = int(input())

print("Adjusting brightness...")

sum_brightness = "** "


for count in range(0, brightness_level, 2):

    print("Beep's brightness level: " + sum_brightness)

    sum_brightness = sum_brightness + sum_brightness
