"""
Signature Validation
Given a message string, a secret key string, and a signature number, determine if the signature is valid using this encoding method:

Letters in the message and secret key have these values:
a to z have values 1 to 26 respectively.
A to Z have values 27 to 52 respectively.
All other characters have no value.
Compute the signature by taking the sum of the message plus the sum of the secret key.
For example, given the message "foo" and the secret key "bar", the signature would be 57:

f (6) + o (15) + o (15) = 36
b (2) + a (1) + r (18) = 21
36 + 21 = 57
Check if the computed signature matches the provided signature.

1. verify("foo", "bar", 57) should return True.
2. verify("foo", "bar", 54) should return False.
3. verify("freeCodeCamp", "Rocks", 238) should return True.
4. verify("Is this valid?", "No", 210) should return False.
"""

import string


def verify(message, key, signature):
    values = {}
    for index, letter in enumerate(string.ascii_lowercase):
        values[letter] = index + 1
        index2 = index + 1
    for index, letter in enumerate(string.ascii_uppercase):
        values[letter] = index2 + 1
        index2 += 1
    total = 0
    for character in message:
        if character in values:
            total += values[character]
    for character in key:
        if character in values:
            total += values[character]
    return total == signature


print(verify("Is this valid?", "No", 210))
