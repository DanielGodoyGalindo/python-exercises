"""
Snowflake Generator
Given a multi-line string that uses newline characters (\n) to represent a line break, return a new string where each line is mirrored horizontally and attached to the end of the original line.

Mirror a line by reversing all of its characters, including spaces.
For example, given "* \n *\n* ", which logs to the console as:

*
 *
*
Return "*  *\n ** \n*  *", which logs to the console as:

*  *
 **
*  *
Take careful note of the whitespaces in the given and returned strings. Be sure not to trim any of them.

1. generate_snowflake("* \n *\n* ") should return "*  *\n ** \n*  *".
2. generate_snowflake("X=~") should return "X=~~=X".
3. generate_snowflake(" X  \n  v \nX--=\n  ^ \n X  ") should return " X    X \n  v  v  \nX--==--X\n  ^  ^  \n X    X ".
"""


def generate_snowflake(crystals):
    lines = crystals.split("\n")
    output = []
    for line in lines:
        new_line = line + line[::-1]
        output.append(new_line)
    return "\n".join(output)


print(generate_snowflake(" X  \n  v \nX--=\n  ^ \n X  "))
