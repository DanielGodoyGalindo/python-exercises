"""
Word Guesser
Given two strings of the same length, a secret word and a guess, compare the guess to the secret word using the following rules:

The secret word and guess will only consist of uppercase letters ("A" to "Z");
For each letter in the guess, replace it with a number according to how it matches the secret word:
"2" if the letter is in the secret word and in the correct position.
"1" if the letter is in the secret word but in the wrong position.
"0" if the letter is not in the secret word.
Each letter in the secret word can be used at most once.
Exact matches ("2") are assigned first, then partial matches ("1") are assigned from left to right for remaining letters.
If a letter occurs multiple times in the guess, it can only match as many times as it appears in the secret word.
For example, given a secret word of "APPLE" and a guess of "POPPA", return "10201":

The first "P" is not in the correct location ("1"), the "O" isn't in the secret word ("0"), the second "P" is in the correct location ("2"), the third "P" is a zero ("0") because the two "P"'s in the secret word have been used, and the "A" is not in the correct location ("1").

1. compare("APPLE", "POPPA") should return "10201".
2. compare("REACT", "TRACE") should return "11221".
3. compare("DEBUGS", "PYTHON") should return "000000".

"""

from collections import Counter

def compare(word, guess):
    if len(word) != len(guess):
        return None

    output = ["0"] * len(word) # initialize result with all zeros
    available = Counter(word) # count how many times each letter appears in the secret word

    # First pass: exact matches ("2")
    for i in range(len(word)):
        if guess[i] == word[i]:
            output[i] = "2"
            available[guess[i]] -= 1

    # Second pass: correct letter, wrong position ("1")
    for i in range(len(word)):
        if output[i] == "0" and available[guess[i]] > 0:
            output[i] = "1"
            available[guess[i]] -= 1

    return "".join(output)


print(compare("APPLE", "POPPA"))
