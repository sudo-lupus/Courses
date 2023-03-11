import re

def rearrange_name(string):
    pattern = "^([A-Za-z]+), ([A-Za-z]+ ?[A-Z]?\.?)$"
    string2 = re.search(pattern, string)
    firstname_lastname = f"{string2[2]} {string2[1]}"
    return firstname_lastname

names = []
names.append("Lovelace, Ada")
names.append("Kennedy, John F.")

for name in names:
    print(f"{name}\n{rearrange_name(name)}\n")