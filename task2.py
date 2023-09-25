#! python3
# Find the volume of a sphere.
# You will ask the user to enter the radius of the sphere.
# Calculate the Volume and then display the result to the user.
# You will need to import the math module in order to use math.pi

# Inputs:
# radius
#
# Outputs
# volume
#
# test output radius of 3 should give volume of 113.09733552923254

import math

def calculate_volume(radius):
    volume = (4/3) * math.pi * radius ** 3
    return volume

radius = float(input("Enter the value of the radius: "))
volume = calculate_volume(radius)
print("The volume of the sphere is:", volume)

