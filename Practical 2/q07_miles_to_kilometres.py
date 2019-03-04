def print_table(x, y):
    print('Kilometres and Miles conversion table')
    print("---------------------------------------------------------------")
    print("Miles\t\t\tKilometres\t\t\tKilometres\t\t\tMiles")
    for i in range(x, y + 1):
        print("%s\t\t\t\t%s\t\t\t\t\t%s\t\t\t\t\t%s" %
              ('{:.1f}'.format(i), '{:.1f}'.format(i * 1.609), '{:.1f}'.format(i), '{:.1f}'.format(i / 1.609)))
        i + 1
    print("---------------------------------------------------------------")


x = int(input('First integer in table '))
y = int(input('Last integer in table '))
print_table(x, y)
