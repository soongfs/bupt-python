def is_leap_year(year: int) -> bool:
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


date = input()
year, month, day = date.split("-")
year = int(year)
month = int(month)
day = int(day)
# print(year, mon, day)
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if day != 1:
    print(year, month, day - 1, sep="-")
elif month == 1:
    print(year - 1, 12, 31, sep="-")
elif month == 3:
    if is_leap_year(year):
        print(year, 2, 29, sep="-")
    else:
        print(year, 2, 28, sep="-")
else:
    print(year, month - 1, days_in_month[month - 2], sep="-")
