"""
Weekday Finder
Given a string date in the format YYYY-MM-DD, return the day of the week.

Valid return days are:

"Sunday"
"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
Be sure to ignore time zones.

1. get_weekday("2025-11-06") should return Thursday.
2. get_weekday("1999-12-31") should return Friday.
"""

from datetime import datetime


def get_weekday(date_string):
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    return days[datetime.strptime(date_string, "%Y-%m-%d").date().weekday()]


print(get_weekday("1999-12-31"))
