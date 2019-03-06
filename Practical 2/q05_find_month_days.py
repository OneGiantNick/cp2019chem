
# Finding values
year = int(input('Enter the year here '))
month = str(input('Enter the month here '))

# Dictionary
day_month = {
    '1': 31,
    '2': 28,
    '3': 31,
    '4': 30,
    '5': 31,
    '6': 30,
    '7': 31,
    '8': 31,
    '9': 30,
    '10': 31,
    '11': 30,
    '12': 31,
}
month_year = {
    '1': 'January',
    '2': 'February',
    '3': 'March',
    '4': 'April',
    '5': 'May',
    '6': 'June',
    '7': 'July',
    '8': 'August',
    '9': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}
# if leap year is february
february = {
    'february': 29,
}


def february_leap(month, year):
    if month == 2 and year % 4 == 0 and year % 100 != 0:
        for key, value in february.items():
            print(value, 'days in', key, year)
    elif month == 2 and year % 400 == 0:
        for key, value in february.items():
            print(value, 'days in', key, year)
    else:
        print(day_month[month], 'days in', month_year[month], year)


february_leap(month, year)
