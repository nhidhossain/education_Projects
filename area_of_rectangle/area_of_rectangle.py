# formula area of rect is A=wl
# here, w = width and l = length 
#       or we can use A = bh
#       here, b = base and h = height
# the superscript of 2 is "\U+00B2"

w = float(input("Enter the width of the Rectangle: "))
l = float(input("Enter the length of the Rectangle: "))

area = w * l 

print("The area of your rectangle is: {} m\u00b2".format(area))
