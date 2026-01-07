"""
Email Signature Generator
Given strings for a person's name, title, and company, return an email signature as a single string using the following rules:

The name should appear first, preceded by a prefix that depends on the first letter of the name. For names starting with (case-insensitive):
A-I: Use >> as the prefix.
J-R: Use -- as the prefix.
S-Z: Use :: as the prefix.
A comma and space (, ) should follow the name.
The title and company should follow the comma and space, separated by " at " (with spaces around it).
For example, given "Quinn Waverly", "Founder and CEO", and "TechCo" return "--Quinn Waverly, Founder and CEO at TechCo".
"""
import re

def generate_signature(name, title, company):
    output = ""
    # name
    if re.search(r"^[A-M]", name, re.I):
        output += ">>"
    elif re.search(r"^[J-R]", name, re.I):
        output += "--"
    elif re.search(r"^[S-Z]", name, re.I):
        output += "::"
    # title and company 
    output += name + ", " + title + " at " + company
    return output

print(generate_signature("Quinn Waverly","Founder and CEO","TechCo"))
