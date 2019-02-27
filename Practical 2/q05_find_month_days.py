

# Finding values
year = int(input('Enter the year here '))
month = str(input('Enter the month here '))
month = month.lower()

# Dictionary
day_month = {
    'january': 31,
    'february': 28,
    'march': 31,
    'april': 30,
    'may': 31,
    'june': 30,
    'july': 31,
    'august': 31,
    'september': 30,
    'october': 31,
    'november': 30,
    'december': 31,
}
# if leap year is february
february = {
    'february': 29,
}


def february_leap(month, year):
    if month == 'february' and year % 4 == 0 and year % 100 != 0:
        for key, value in february.items():
            print(value, 'days in', key, year)
    elif month == 'february' and year % 400 == 0:
        for key, value in february.items():
            print(value, 'days in', key, year)
    else:
        print(day_month[month], 'days in', month, year)


february_leap(month, year)
