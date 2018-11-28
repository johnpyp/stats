# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

a = 999
b = 999


def is_palindrome(num):
    string = str(num)
    return string[::-1] == string


def large_palindrome(a, b):
    current = 0
    c = 0
    d = 0
    for x in range(a, 0, -1):
        for y in range(b, x, -1):
            if is_palindrome(x * y):
                if x < c and y < d:
                    return current
                current = x * y
                c = x
                d = y


print(large_palindrome(a, b))
