"""
Markdown Heading Converter
Given a string representing a Markdown heading, return the equivalent HTML heading.

A valid Markdown heading must:

Start with zero or more spaces, followed by
1 to 6 hash characters (#) in a row, then
At least one space. And finally,
The heading text.
The number of hash symbols determines the heading level. For example, one hash symbol corresponds to an h1 tag, and six hash symbols correspond to an h6 tag.

If the given string doesn't have the exact format above, return "Invalid format".

For example, given "# My level 1 heading", return "<h1>My level 1 heading</h1>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.
"""

import re


def convert(heading):
    if re.search("^\s*#{1,6}\s+\w+", heading) is None:
        return "Invalid format"
    heading = heading.strip()
    splitted = heading.split(" ")
    hashes = splitted[0].count("#")
    text_start = heading.find("# ") + 1
    text = heading[text_start:]
    return "<h" + str(hashes) + ">" + text.strip() + "</h" + str(hashes) + ">"


print(convert("  ###  My level 3 heading"))

"""
def convert(heading):
    # Regex pattern:
    # ^\s*       → allow any number of leading spaces
    # (#{1,6})   → capture 1 to 6 hash symbols (this determines the heading level)
    # \s+        → require at least one space after the hashes
    # (.*\S)     → capture the heading text, ensuring it ends with a non-space character
    # \s*$       → allow trailing spaces until the end of the line
    pattern = r"^\s*(#{1,6})\s+(.*\S)\s*$"

    # Try to match the pattern against the input string
    match = re.match(pattern, heading)

    # If the string does NOT match the required Markdown heading format, return error
    if not match:
        return "Invalid format"

    # Extract the captured groups:
    # hashes → the sequence of # symbols
    # text   → the actual heading text
    hashes, text = match.groups()

    # Heading level is the number of # characters
    level = len(hashes)

    # Return the equivalent HTML heading using f-string formatting
    return f"<h{level}>{text}</h{level}>"
"""
