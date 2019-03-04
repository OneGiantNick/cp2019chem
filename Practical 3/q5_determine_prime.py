

def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True


lis = []
b = 2
num = 0
while num < 1000:
    if is_prime(b):
        lis.append(b)
        num += 1
    b += 1
    if len(lis) == 10:
        for a in lis:
            print("{} ".format(a), end="")
        print("")
        lis = []
