"""
SCREAMING_SNAKE_CASE
Given a string representing a variable name, return the variable name converted to SCREAMING_SNAKE_CASE.

The given variable names will be written in one of the following formats:

camelCase
PascalCase
snake_case
kebab-case
In the above formats, words are separated by an underscore (_), a hyphen (-), or a new word starts with a capital letter.

To convert to SCREAMING_SNAKE_CASE:

Make all letters uppercase
Separate words with an underscore (_)

1. to_screaming_snake_case("userEmail") should return "USER_EMAIL".
2. to_screaming_snake_case("UserPassword") should return "USER_PASSWORD".
3. to_screaming_snake_case("user_id") should return "USER_ID".
4. to_screaming_snake_case("user-address") should return "USER_ADDRESS".
5. to_screaming_snake_case("username") should return "USERNAME".
"""


def to_screaming_snake_case(variable_name: str):
    output = variable_name
    upercases_idx = find_uppercases(variable_name)
    if upercases_idx:
        for idx in upercases_idx:
            if idx == 0:
                continue
            output = variable_name.replace(variable_name[idx], "_" + variable_name[idx])
    return output.replace("-", "_").upper()


def find_uppercases(input):
    output = []
    for idx, letter in enumerate(input):
        if letter.isupper():
            output.append(idx)
    return output


print(to_screaming_snake_case("username"))
