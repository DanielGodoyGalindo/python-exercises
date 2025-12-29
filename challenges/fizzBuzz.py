"""
FizzBuzz
Given an integer (n), return an array of integers from 1 to n (inclusive), replacing numbers that are multiple of:

3 with "Fizz".
5 with "Buzz".
3 and 5 with "FizzBuzz".

1. fizz_buzz(2) should return [1, 2].
2. fizz_buzz(4) should return [1, 2, "Fizz", 4].
3. fizz_buzz(8) should return [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8].
"""


def fizz_buzz(n):
    numbers = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            numbers.append("FizzBuzz")
        elif i % 3 == 0:
            numbers.append("Fizz")
        elif i % 5 == 0:
            numbers.append("Buzz")
        else:
            numbers.append(i)
    return numbers

print(fizz_buzz(20))