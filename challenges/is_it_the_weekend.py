"""
Is It the Weekend?
Given a date in the format "YYYY-MM-DD", return the number of days left until the weekend.

The weekend starts on Saturday.
If the given date is Saturday or Sunday, return "It's the weekend!".
Otherwise, return "X days until the weekend.", where X is the number of days until Saturday.
If X is 1, use "day" (singular) instead of "days" (plural).
Make sure the calculation ignores your local timezone.

1. days_until_weekend("2025-11-14") should return "1 day until the weekend.".
2. days_until_weekend("2025-01-01") should return "3 days until the weekend.".
3. days_until_weekend("2025-12-06") should return "It's the weekend!".
4. days_until_weekend("2026-01-27") should return "4 days until the weekend.".
"""

from datetime import datetime


def days_until_weekend(date_string):
    # Saturday is represented by 5 (Monday = 0)
    SATURDAY = 5
    date_obj = datetime.strptime(date_string, "%Y-%m-%d")
    weekday = date_obj.weekday()
    if weekday >= SATURDAY:
        return "It's the weekend!"
    days_left = SATURDAY - weekday
    return f"{days_left} {'day' if days_left == 1 else 'days'} until the weekend."


print(days_until_weekend("2026-01-27"))
