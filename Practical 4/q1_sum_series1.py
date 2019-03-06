n = int(input('Enter the amount of terms in the series '))
print('%-12s%-12s' % ('i', 'm(i)'))
s1 = 0
for i in range(1, n + 1):
    s1 = s1 + (1 / i)
    print('%-12s%-12s' % (i, round(s1, 2)))
