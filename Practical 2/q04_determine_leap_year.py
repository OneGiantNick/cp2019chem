def is_leap_year(x):
    if x % 4 == 0 and x % 100 != 0:
            print(x, 'is a leap year')
    elif x % 400 == 0:
        print(x, 'is a leap year')
    else:
        print(x, 'is not a leap year')


print(is_leap_year(int(input('Enter a year here '))))
