file = open("spider.txt")
print(file.readline())
print(file.readline())
print(file.read())

file.close()

with open("spider.txt") as file:
    print(file.readline())

with open("spider.txt") as file:
    contents = file.read()

print(contents)