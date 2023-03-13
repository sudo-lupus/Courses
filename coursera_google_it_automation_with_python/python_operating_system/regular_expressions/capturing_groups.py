import re

def rearrange_name(string):
    pattern = "^([A-Za-z]+), ([A-Za-z]+ ?[A-Z]?\.?)$"
    result = re.search(pattern, string)
    if result is None:
        return string
    firstname_lastname = f"{result} {result}"
    return firstname_lastname

names = []
names.append("Lovelace, Ada")
names.append("Kennedy, John F.")
names.append("Hopper, Grace M.")

for name in names:
    print(f"{name}\n{rearrange_name(name)}\n")