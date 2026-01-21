"""
Speed Check
Given the speed you are traveling in miles per hour (MPH), and a speed limit in kilometers per hour (KPH), determine whether you are speeding and if you will get a warning or a ticket.

1 mile equals 1.60934 kilometers.
If you are traveling less than or equal to the speed limit, return "Not Speeding".
If you are traveling 5 KPH or less over the speed limit, return "Warning".
If you are traveling more than 5 KPH over the speed limit, return "Ticket".

1. speed_check(30, 70) should return "Not Speeding".
2. speed_check(40, 60) should return "Warning".
3. speed_check(40, 65) should return "Not Speeding".
4. speed_check(60, 90) should return "Ticket".
"""


def speed_check(speed_mph, speed_limit_kph):
    
    MPH_TO_KMH = 1.60934
    calculated_speed = speed_mph * MPH_TO_KMH
    difference = calculated_speed - speed_limit_kph

    if difference <= 0:
        return "Not Speeding"
    elif difference <= 5:
        return "Warning"
    else:
        return "Ticket"


print(speed_check(60, 90))
