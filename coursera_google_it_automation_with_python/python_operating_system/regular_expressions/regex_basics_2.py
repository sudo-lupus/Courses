import re
# ^ 
print(re.search(r"^x", "xenon"))

# .
print(re.search(r"p.ng", r"penguin"))
print(re.search(r"p.ng", r"clapping"))
print(re.search(r"p.ng", r"sponge"))

# re.IGNORECASE
print(re.search(r"p.ng", r"Pangea", re.IGNORECASE))

# Character Classes
print(re.search(r"[Pp]ython", r"Python"))
