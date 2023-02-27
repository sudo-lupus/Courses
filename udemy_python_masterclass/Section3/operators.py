age = int(24)
pi = float(3.14)

### OPERATORS

a = 12
b = 3

print(a + b) # 15
print(a - b) # 9
print(a * b) # 36
print(a / b) # 4.0
print(a // b) # 4 Integer division, rounded down towards minus infinity
print(a % b) # 0 modulo: the remainder after integer division

print()

for i in range(1, a // b):
    print(i)

print()

bun_price = 2.40
money = 15

print(money // bun_price)

print("\n\n\nOperator Precedence\n--------------")

print(a + b / 3 - 4 * 12) # -35

d = "0123456789"
print(d[::5])
print(d[0:5])
print(d[:-2])
