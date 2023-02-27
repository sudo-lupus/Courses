prime_count = 2
n = 3

while prime_count < 10_001:

    n += 2
    prime_count += 1

    print(f"{prime_count} : {n}")

print(n)