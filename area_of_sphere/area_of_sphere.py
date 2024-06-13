import math

radius = float(input("Enter the Radius of the Sphere: "))

Area = 4 * math.pi * radius**2 

print(f"The Surface Area of the Sphere is: {Area:.2f}", "square units.")

# -------

import math

def surface_area_of_sphere(radius):
    
    surface_area = 4 * math.pi * radius ** 2
    return surface_area

radius = float(input("Enter the radius of the sphere: "))

area = surface_area_of_sphere(radius)

print(f"The surface area of the sphere with radius {radius} is {area:.2f} square units.")
