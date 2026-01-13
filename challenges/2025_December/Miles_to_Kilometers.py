"""
Miles to Kilometers
Given a distance in miles as a number, return the equivalent distance in kilometers.

The input will always be a non-negative number.
1 mile equals 1.60934 kilometers.
Round the result to two decimal places.
Remove unnecessary trailing zeros from the rounded result.

1. convert_to_km(1) should return 1.61
2. convert_to_km(21) should return 33.8
3. convert_to_km(3.5) should return 5.63.
"""


def convert_to_km(miles):
    mile_to_kms = 1.60934
    return round(miles * mile_to_kms, 2)


print(convert_to_km(1))
