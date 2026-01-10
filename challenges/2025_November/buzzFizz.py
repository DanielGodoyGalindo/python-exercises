"""
BuzzFizz
Given an array, determine if it is a correct FizzBuzz sequence from 1 to the last item in the array. A sequence is correct if:

Numbers that are multiples of 3 are replaced with "Fizz"
Numbers that are multiples of 5 are replaced with "Buzz"
Numbers that are multiples of both 3 and 5 are replaced with "FizzBuzz"
All other numbers remain as integers in ascending order, starting from 1.
The array must start at 1 and have no missing or extra elements.

1. is_fizz_buzz([1, 2, "Fizz", 4]) should return True.
2. is_fizz_buzz([1, 2, 3, 4]) should return False.
3. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", 7]) should return False.
"""


def is_fizz_buzz(sequence):
    count = 0
    for element in reversed(sequence):
        if element != "Fizz" and element != "Buzz" and element != "FizzBuzz":
            number = element
            break
        else:
            count += 1
    if count > 0:
        number += count
    output = fizz_buzz(number)
    return output == sequence


def fizz_buzz(n):
    numbers = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            numbers.append("FizzBuzz")
        elif i % 3 == 0:
            numbers.append("Fizz")
        elif i % 5 == 0:
            numbers.append("Buzz")
        else:
            numbers.append(i)
    return numbers


"""
Pythonic:
def is_fizz_buzz(sequence):
    for i, element in enumerate(sequence, start=1):
        if i % 3 == 0 and i % 5 == 0:
            expected = "FizzBuzz"
        elif i % 3 == 0:
            expected = "Fizz"
        elif i % 5 == 0:
            expected = "Buzz"
        else:
            expected = i

        if element != expected:
            return False

    return True
"""

print(
    is_fizz_buzz(
        [
            1,
            2,
            "Fizz",
            4,
            "Buzz",
            "Fizz",
            7,
            8,
            "Fizz",
            "Buzz",
            11,
            "Fizz",
            13,
            "FizzBuzz",
        ]
    )
)
