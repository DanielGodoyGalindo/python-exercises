'''
Markdown Italic Parser
Given a string that may include some italic text in Markdown, return the equivalent HTML string.

Italic text in Markdown is any text that starts and ends with a single asterisk (*) or a single underscore (_).
There cannot be any spaces between the text and the asterisk or underscore, but there can be spaces in the text itself.
Convert all italic occurrences to HTML i tags and return the string.
For example, given "*This is italic*", return "<i>This is italic</i>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.

1. parse_italics("*This is italic*") should return "<i>This is italic</i>".
2. parse_italics("_This is also italic_") should return "<i>This is also italic</i>".
3. parse_italics("*This is not italic *") should return "*This is not italic *".
4. parse_italics("_ This is also not italic_") should return "_ This is also not italic_".
'''

import re

def parse_italics(markdown):
    pattern = r'(?<!\S)(\*|_)([^\s].*?[^\s])\1(?!\S)'
    return re.sub(pattern, r'<i>\2</i>', markdown)

print(parse_italics("*This is italic*"))