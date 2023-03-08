with open("novel.txt", "w") as file:
    a = file.write("It was a dark and stormy night.")

with open("novel.txt", "r") as file:
    lines = file.readlines()

print(lines)
print(a)
