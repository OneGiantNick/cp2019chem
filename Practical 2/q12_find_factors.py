from math import sqrt


def prime_factors(n):
    while n % 2 == 0:
        print(2),
        n = n / 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            print(i),
            n = n / i
    if n > 2:
        print(n)


num = int(input('Enter a number here and find prime factors '))
prime_factors(num)
