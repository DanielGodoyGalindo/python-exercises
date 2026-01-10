"""
Vowels and Consonants
Given a string, return an array with the number of vowels and number of consonants in the string.

Vowels consist of a, e, i, o, u in any case.
Consonants consist of all other letters in any case.
Ignore any non-letter characters.
For example, given "Hello World", return [3, 7].
"""


def count(s):
    vowels = ["a", "e", "i", "o", "u"]
    vowels_count = 0
    consonants_count = 0
    for letter in s:
        if letter in vowels:
            vowels_count += 1
        elif letter.isalpha():
            consonants_count += 1
    return [vowels_count, consonants_count]

'''
Pythonic:

def count(s):
    vowels = "aeiou"
    return [
        sum(c in vowels for c in s),
        sum(c.isalpha() and c not in vowels for c in s)
    ]
'''


print(count("Hello World"))
