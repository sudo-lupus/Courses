import re
my_string = ""

def is_allowed_specific_char(string):
    match = re.match("^[a-zA-Z0-9]*\Z", string)
    return True if match is not None else False

print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))