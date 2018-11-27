

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

import sys
import math
import time
num = int(sys.argv[1])


def algo(num):
    all_nums = range(num)
    filtered_nums = [x for x in all_nums if x % 3 == 0 or x % 5 == 0]
    return sum(filtered_nums)


def sum_all(n, y):
    x = math.ceil(n / y)
    return y*(x*(x-1)/2)


def algo2(num):
    return sum_all(num, 5) + sum_all(num, 3) - sum_all(num, 15)


# print(algo(num))
start = time.time()

print(algo2(num))
end = time.time()
print(end - start)

# solved: 233168
