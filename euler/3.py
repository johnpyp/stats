# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
import math

val = 600851475143


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while (i**2) <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


ceil = math.ceil(math.sqrt(val))

count = ceil
while count > 0:
    if is_prime(count) and val % count == 0:
        break
    count -= 1

print(count)
