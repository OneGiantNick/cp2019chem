
i = 1
print('%-12s%-12s' % ('i', 'm(i)'))
for i in range(1, 21):
    m = 0
    for n in range(1, i + 1):
        m += n / (n + 1)
    print('%-12s%-12s' % (i, m))
