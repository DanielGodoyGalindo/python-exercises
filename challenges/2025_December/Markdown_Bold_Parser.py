"""
Markdown Bold Parser
Given a string that may include some bold text in Markdown, return the equivalent HTML string.

Bold text in Markdown is any text that starts and ends with two asterisks (**) or two underscores (__).
There cannot be any spaces between the text and the asterisks or underscores, but there can be spaces in the text itself.
Convert all bold occurrences to HTML b tags and return the string.
For example, given "**This is bold**", return "<b>This is bold</b>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.

1. parse_bold("**This is bold**") should return "<b>This is bold</b>".
2. parse_bold("__This is also bold__") should return "<b>This is also bold</b>".
3. parse_bold("**This is not bold **") should return "**This is not bold **".
"""


import re

def parse_bold(markdown):
    regex = r'(\*\*|__)(?=\S)(.*?)(?<=\S)(\*\*|__)'
    return re.sub(regex, r'<b>\2</b>', markdown)

print(parse_bold("**This is bold**"))
print(parse_bold("__This is also bold__"))
print(parse_bold("**This is not bold **"))