import re

result = re.search(r"[a-zA-Z]{5}", "a ghost")
print(result)

result = re.findall(r"[a-zA-Z]{5}", "a scary ghost appears")
print(result)

result = re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeard")
print(result)

result = re.findall(r"\w{5,}", "I really like strawberries")
print(result)