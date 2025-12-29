"""
Message Validator
Given a message string and a validation string, determine if the message is valid.

A message is valid if each word in the message starts with the corresponding letter in the validation string, in order.
Letters are case-insensitive.
Words in the message are separated by single spaces.

1. is_valid_message("hello world", "hw") should return True.
2. is_valid_message("ALL CAPITAL LETTERS", "acl") should return True.
3. is_valid_message("Coding challenge are boring.", "cca") should return False.
"""


def is_valid_message(message, validation):
    letters_to_check = ""
    message_splitted = message.split()
    for word in message_splitted:
        letters_to_check += word[0].lower()
    return True if letters_to_check == validation.lower() else False


print(is_valid_message("Coding challenge are boring.", "cca"))
