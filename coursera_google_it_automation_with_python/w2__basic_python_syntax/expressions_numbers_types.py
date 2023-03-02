from decimal import *
import math

# Implicit Conversion
a = int(7)
b = float(7.5)
c = a + b

# Interpreter automatically converts to float
print(f"{a} + {b} = {c}")
print(str(type(c)) + "\n")

# Combining strings and numbers
# 1.
base = 6
height = 3
area = (base * height) / 2
print("The area of the triangle is: " + str(area) + "\n")

# 2.
total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total / files
print("The average size is: " + str(average) + "\n")

# ZeroDivisionError
numerator = 7
denominator = 0
try:
    result = numerator / denominator
    print("Result: {result}")
except ZeroDivisionError:
    result = float("nan")
    print("You can not divide by 0")
    print(f"Result: {result}")

# NaN
# Assigning a NaN
my_nan1 = float("nan")
print(f"My float nan : {my_nan1}")
print(f"Type : {type(my_nan1)}\n")

my_nan2 = Decimal("Nan")
print(f"My Decimal NaN : {my_nan2}")
print(f"Type : {type(my_nan2)}\n")
# Check if a value is a NaN
print(math.isnan(my_nan1))
print(math.isnan(my_nan2))