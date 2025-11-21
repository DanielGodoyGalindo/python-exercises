'''
Longest Word
Given a sentence string, return the longest word in the sentence.

Words are separated by a single space.
Only letters (a-z, case-insensitive) count toward the word's length.
If there are multiple words with the same length, return the first one that appears.
Return the word as it appears in the given string, with punctuation removed.
'''

def longest_word(sentence):
    for char in ["'","!","?","."]:
        if char in sentence:
            sentence = sentence.replace(char,"")
    splitted=sentence.split()
    longestLen=0
    longestWord=""
    for word in splitted:
        if len(word) > longestLen:
            longestWord = word
            longestLen = len(word)
    return longestWord

print(longest_word("Hello coding challenge."))