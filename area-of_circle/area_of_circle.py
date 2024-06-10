# formula area of rect is A=pi*r**2
# here, pi = 3.1416 and r = radius 
# the superscript of 2 is "cm\U+00B2"

import math

r = float(input("Enter the Radius of the Circle: "))

area = math.pi*(r**2)

print("The area of your rectangle is: {} cm\u00b2".format(area))