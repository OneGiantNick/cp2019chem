
from calendar import monthrange

month = int(input("Enter month: "))
year = int(input("Enter year: "))

print(monthrange(year, month)[1])
