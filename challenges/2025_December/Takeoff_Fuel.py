"""
Takeoff Fuel
Given the numbers of gallons of fuel currently in your airplane, and the required number of liters of fuel to reach your destination, determine how many additional gallons of fuel you should add.

1 gallon equals 3.78541 liters.
If the airplane already has enough fuel, return 0.
You can only add whole gallons.
Do not include decimals in the return number.

1. fuel_to_add(0, 1) should return 1.
2. fuel_to_add(5, 40) should return 6.
3. fuel_to_add(10, 30) should return 0.
4. fuel_to_add(896, 20500) should return 4520.
5. fuel_to_add(1000, 50000) should return 12209.
"""


from math import ceil


def liters_to_gallons(liters):
    GALLON_TO_LITERS = 3.78541
    return ceil(liters / GALLON_TO_LITERS)


def fuel_to_add(current_gallons, required_liters):
    output = liters_to_gallons(required_liters) - current_gallons
    return output if output > 0 else 0

print(fuel_to_add(1000, 50000))