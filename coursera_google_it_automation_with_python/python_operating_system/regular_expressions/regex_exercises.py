import re

# Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
def is_allowed_specific_char(string):
    match = re.match("^[a-zA-Z0-9]*\Z", string)
    return True if match is not None else False

print(is_allowed_specific_char("ABCDEFabcdef123450"))       # True
print(is_allowed_specific_char("*&%@#!}{"))                 # False