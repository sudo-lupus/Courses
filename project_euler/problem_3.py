'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

a = 600851475143
biggest_prime = 2

for i in range(2, a // 2):
    if(a % i == 0):
        for j in range(2, i // 2):
            print(j)
            if(j % i != 0):
                biggest_prime = j
                print(j)

print(biggest_prime)