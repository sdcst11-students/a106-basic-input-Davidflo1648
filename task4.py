#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912

import math

def calculate_surface_area(radius, height):
    slant_height = math.sqrt(radius**2 + height**2)
    base_area = math.pi * radius**2
    lateral_area = math.pi * radius * slant_height
    surface_area = base_area + lateral_area
    return surface_area

radius = float(input("Enter the value of the radius: "))
height = float(input("Enter the value of the height: "))
surface_area = calculate_surface_area(radius, height)
print("The surface area of the cone is:", surface_area)

