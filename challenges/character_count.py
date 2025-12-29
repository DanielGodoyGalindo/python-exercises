"""
Character Count
Given a sentence string, return an array with a count of each character in alphabetical order.

Treat upper and lowercase letters as the same letter when counting.
Ignore numbers, spaces, punctuation, etc.
Return the count and letter in the format "letter count". For instance, "a 3".
All returned letters should be lowercase.
Do not return a count of letters that are not in the given string.

count_characters("hello world") should return ["d 1", "e 1", "h 1", "l 3", "o 2", "r 1", "w 1"]

"""

import re


def count_characters(sentence):
    sentence = re.sub("[^A-Za-z]+", "", sentence).lower()
    letters = {} # dict to store letters as keys and count as value
    already_checked = [] # list to store already checked letters
    output = []
    for i in sentence:
        for j in sentence:
            if i.lower() == j.lower() and i not in already_checked:
                if i in letters:
                    letters[i] += 1
                else:
                    letters[i.lower()] = 1 # add letter to dict for the first time
        if i not in already_checked:
            already_checked.append(i.lower()) # append letter when is checked only the first time
    sorted_dict = dict(sorted(letters.items())) # sort dict
    for key, value in sorted_dict.items(): # create output list
        output.append(key + " " + str(value))
    return output


'''
Pythonic solution:

import re

def count_characters(sentence):
    sentence = re.sub("[^a-zA-Z]", "", sentence).lower()
    letters = {}

    for char in sentence:
        letters[char] = letters.get(char, 0) + 1

    return [f"{k} {v}" for k, v in sorted(letters.items())]
'''


print(count_characters("I love coding challenges!"))