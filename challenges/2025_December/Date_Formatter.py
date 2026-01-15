"""
Date Formatter
Given a date in the format "Month day, year", return the date in the format "YYYY-MM-DD".

The given month will be the full English month name. For example: "January", "February", etc.
In the return value, pad the month and day with leading zeros if necessary to ensure two digits.
For example, given "December 6, 2025", return "2025-12-06".

1. format_date("December 6, 2025") should return "2025-12-06".
2. format_date("January 1, 2000") should return "2000-01-01".
3. format_date("November 11, 1111") should return "1111-11-11".
4. format_date("September 7, 512") should return "512-09-07".
5. format_date("May 4, 1950") should return "1950-05-04".
6. format_date("February 29, 1992") should return "1992-02-29".
"""


def format_date(date_string: str):
    
    # Get date parts
    parts = date_string.split()
    month, day, year = parts[0], parts[1][:-1], parts[2]

    month_names = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12",
    }

    return f"{year}-{month_names[month]}-{day.zfill(2)}"


print(format_date("January 1, 2000"))
