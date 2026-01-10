"""
Fingerprint Test
Given two strings representing fingerprints, determine if they are a match using the following rules:

Each fingerprint will consist only of lowercase letters (a-z).
Two fingerprints are considered a match if:
They are the same length.
The number of differing characters does not exceed 10% of the fingerprint length.
"""


def is_match(fingerprint_a, fingerprint_b):
    diff_chars = 0
    if not fingerprint_a.islower() or not fingerprint_b.islower():
        return False
    if not len(fingerprint_a) == len(fingerprint_b):
        return False
    for index, char in enumerate(fingerprint_a):
        if char != fingerprint_b[index]:
            diff_chars += 1
    if len(fingerprint_a) * 10 / 100 < diff_chars:
        return False
    return True


print(
    is_match(
        "thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazycat"
    )
)

'''
def is_match(fingerprint_a, fingerprint_b):
    # Validations
    if not (fingerprint_a.isalpha() and fingerprint_a.islower()):
        return False
    if not (fingerprint_b.isalpha() and fingerprint_b.islower()):
        return False
    if len(fingerprint_a) != len(fingerprint_b):
        return False

    # Count differences
    diff_chars = sum(a != b for a, b in zip(fingerprint_a, fingerprint_b))

    # Max allowed: 10%
    max_diff = len(fingerprint_a) * 0.10

    return diff_chars <= max_diff
'''
