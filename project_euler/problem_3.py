'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

a = 600851475143

n = int(a // 2)
found_prime = False

while found_prime == False:
    if n % 2 == 0:
        n -= 1
    if(all(n % i != 0 for i in range(2, n))):
        break
    n -= 2

print(n)