def gcd(x, y, verbose=True):
    if y > x:
        return gcd(y, x)
    while y != 0:
        (x, y) = (y, x % y)
    if verbose:
        print('gcd is %s' % x)
        return x


gcd(24, 18)
