"""
What's My Age Again?
Given the date of someone's birthday in the format YYYY-MM-DD, return the person's age as of November 27th, 2025.

Assume all birthdays are valid dates before November 27th, 2025.
Return the age as an integer.
Be sure to account for whether the person has already had their birthday in 2025.

1. calculate_age("2000-11-20") should return 25.
2. calculate_age("2000-12-01") should return 24.
3. calculate_age("2014-10-25") should return 11.
4. calculate_age("1994-01-06") should return 31.
"""


def calculate_age(birthday):
    ref_year = 2025
    ref_month = 11
    ref_date = 27
    dates = birthday.split("-")
    if int(dates[1]) <= ref_month and int(dates[2]) <= ref_date:
        return ref_year - int(dates[0])
    else:
        return ref_year - int(dates[0]) - 1


print(calculate_age("1994-12-14"))
