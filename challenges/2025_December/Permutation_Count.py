"""
Permutation Count
Given a string, return the number of distinct permutations that can be formed from its characters.

A permutation is any reordering of the characters in the string.
Do not count duplicate permutations.
If the string contains repeated characters, repeated arrangements should only be counted once.
The string will contain only letters (A-Z, a-z).
For example, given "abb", return 3 because there's three unique ways to arrange the letters: "abb", "bab", and "bba".

1. count_permutations("abb") should return 3.
2. count_permutations("abc") should return 6.
"""

from math import factorial
from collections import Counter

def count_permutations(s):
    counts = Counter(s)
    n = len(s)

    result = factorial(n)
    for c in counts.values():
        result //= factorial(c)

    return result


print(count_permutations("freecodecamp"))
