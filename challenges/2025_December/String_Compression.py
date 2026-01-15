"""
String Compression
Given a string sentence, return a compressed version of the sentence where consecutive duplicate words are replaced by the word followed with the number of times it repeats in parentheses.

Only consecutive duplicates are compressed.
Words are separated by single spaces.
For example, given "yes yes yes please", return "yes(3) please".

1. compress_string("yes yes yes please") should return "yes(3) please".
2. compress_string("I have have have apples") should return "I have(3) apples".
3. compress_string("one one three and to the the the the") should return "one(2) three and to the(4)".
4. compress_string("route route route route route route tee tee tee tee tee tee") should return "route(6) tee(6)".
"""


def compress_string(sentence):
    words = sentence.split()
    result = []

    current_word = words[0]
    count = 1

    for i in range(1, len(words)):
        if words[i] == current_word:
            count += 1
        else:
            if count > 1:
                result.append(f"{current_word}({count})")
            else:
                result.append(current_word)
            current_word = words[i]
            count = 1

    if count > 1:
        result.append(f"{current_word}({count})")
    else:
        result.append(current_word)

    return " ".join(result)


print(compress_string("one one three and to the the the the"))
