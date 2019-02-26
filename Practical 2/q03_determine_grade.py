
def grade_boundaries(x):
    if 70 <= x <= 100:
        print('A')
    elif 60 <= x <= 69:
        print('B')
    elif 55 <= x <= 59:
        print('C')
    elif 50 <= x <= 54:
        print('D')
    elif 45 <= x <= 49:
        print('E')
    elif 35 <= x <= 44:
        print('S')
    elif 0 <= x <= 34:
        print('U')
    else:
        print('Invalid! Score must be within 0 - 100')


grade_boundaries(float(input('Enter a score here ')))
