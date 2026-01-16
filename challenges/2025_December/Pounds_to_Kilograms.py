"""
Pounds to Kilograms
Given a weight in pounds as a number, return the string "(lbs) pounds equals (kgs) kilograms.".

Replace "(lbs)" with the input number.
Replace "(kgs)" with the input converted to kilograms, rounded to two decimals and always include two decimal places in the value.
1 pound equals 0.453592 kilograms.
If the input is 1, use "pound" instead of "pounds".
If the converted value is 1, use "kilogram" instead of "kilograms".

1. convert_to_kgs(1) should return "1 pound equals 0.45 kilograms.".
2. convert_to_kgs(0) should return "0 pounds equals 0.00 kilograms.".
3. convert_to_kgs(100) should return "100 pounds equals 45.36 kilograms.".
4. convert_to_kgs(2.5) should return "2.5 pounds equals 1.13 kilograms.".
5. convert_to_kgs(2.20462) should return "2.20462 pounds equals 1.00 kilogram.".
"""


def convert_to_kgs(lbs):
    POUND = 0.453592
    kilograms = round(lbs * POUND, 2)
    return f"{lbs} pound{'' if lbs == 1 else 's'} equals {'%.2f' % kilograms} kilogram{'' if kilograms == 1 else 's'}."


print(convert_to_kgs(2.5))