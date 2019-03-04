from random import randint

n = int(input('Enter amount of rows '))
randint(0, 1)
for i in range(n):
    s = str(randint(0, 1))
    for j in range(n - 1):
        s += " " + str(randint(0, 1))
    print(s)
