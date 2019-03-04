

def nearest_cube(num):
    return round(num ** (1 / 3))


n = nearest_cube(12000)
print(n)
print(n ** 3)
while n ** 3 > 12000:
    n = n - 1
    break
print('The smallest integer is ', n)
