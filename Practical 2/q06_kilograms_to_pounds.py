
def print_table(x, y):
    print('K1ilogrammes to pounds conversion table')
    print("---------------------------------------------------------------")
    print("Kilogrammes\t\t\tPounds")
    for i in range(x, y + 1):
        print("%d\t\t\t\t\t%s" % (i, '{:.1f}'.format(i * 2.2)))
        i + 1
    print("---------------------------------------------------------------")


x = int(input('First integer in table '))
y = int(input('Last integer in table '))
print_table(x, y)
