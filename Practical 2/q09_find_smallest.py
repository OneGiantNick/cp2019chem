from math import sqrt


def nearest_square(num):
    return round(sqrt(num)) ** 2


n = sqrt(nearest_square(12000))
while n ** 2 < 12000:
    n + 1
print('Smallest integer is ', n)
