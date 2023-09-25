#! python3
#
# Find the radius of a sphere if you are given the volume.
# Think about how you would need to solve this equation if you were doing it on paper
#
# Inputs:
# Volume (float)
#
# Outputs:
# radius (float)
#
# Test output Volume of 20.22 should give radius of:1.69002229118
# Note: You will need to do some strange things with your cube root.
# Remember that a cube root is the same as an exponent of 1/3, but
# here you will need to do a power of 1.0/3 or something strange happens.

import math

def calculate_surface_area(volume):
    radius = ((3 * volume) / (4 * math.pi))**(1/3)
    surface_area = 4 * math.pi * radius**2
    return surface_area

volume = float(input("Enter the volume of the sphere: "))
surface_area = calculate_surface_area(volume)
print("The surface area of the sphere is:", surface_area)
