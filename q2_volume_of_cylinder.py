from math import pi
radius = float(input("Enter the radius of the cylinder"))
length = float(input("Enter the length of the cylinder"))
area = pi*pi*radius
vol = radius*length
print("vol of cylinder", "{:.1f}".format(vol))
