
sides = []

# Getting lengths of triangles
len1 = float(input('Enter side 1 of Triangle A '))
len2 = float(input('Enter side 2 of Triangle A '))
len3 = float(input('Enter side 3 of Triangle A '))

# Append to list slides
sides.append(len1)
sides.append(len2)
sides.append(len3)

# Calculate whether triangle is valid
if sides[0] + sides[1] > sides[2] and sides[1] + sides[2] > sides[0] and sides[0] + sides[2] > sides[1]:
    print('Perimeter of Triangle A is ', sides[0] + sides[1] + sides[2])
else:
    print('Invalid triangle!)
    
