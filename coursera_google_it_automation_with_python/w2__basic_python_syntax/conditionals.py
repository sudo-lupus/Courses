print(10 > 1)
print("cat" == "dog")
print(1 != 2)

try:
    print(1 < "1")
except TypeError:
    print("Can't evaluate < > <= >= relations between strings and ints")

print(1 == "1") # False

print("Cat" > "bat")