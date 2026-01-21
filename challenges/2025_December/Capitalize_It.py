"""
Capitalize It
Given a string title, return a new string formatted in title case using the following rules:

Capitalize the first letter of each word.
Make all other letters in each word lowercase.
Words are always separated by a single space.

1. title_case("hello world") should return "Hello World".
2. title_case("the quick brown fox") should return "The Quick Brown Fox".
3. title_case("JAVASCRIPT AND PYTHON") should return "Javascript And Python".
4. title_case("AvOcAdO tOAst fOr brEAkfAst") should return "Avocado Toast For Breakfast".
"""


def title_case(title):
    output = []
    words = title.split()
    for word in words:
        output.append(word.capitalize())
    return " ".join(output)

print(title_case("AvOcAdO tOAst fOr brEAkfAst"))