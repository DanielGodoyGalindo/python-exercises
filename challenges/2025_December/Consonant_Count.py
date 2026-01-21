"""
Consonant Count
Given a string and a target number, determine whether the string contains exactly the target number of consonants.

Consonants are all alphabetic characters except "a", "e", "i", "o", and "u" in any case.
Ignore digits, punctuation, spaces, and other non-letter characters when counting.

1. has_consonant_count("helloworld", 7) should return True.
2. has_consonant_count("eieio", 5) should return False.
3. has_consonant_count("freeCodeCamp Rocks!", 11) should return True.
"""


def has_consonant_count(text, target):
    count = 0
    consonants = ["b","c","d","f","g","h","j","k","l","m","n","p", "q", "r","s","t","v","w","x","y","z"]
    for char in text:
        if char.lower() in consonants:
            count+=1
    return True if count == target else False

print(has_consonant_count("freeCodeCamp Rocks!", 11))