# Run-length encoding is a fast and simple method of encoding strings.
# The basic idea is to represent repeated successive characters as a single count and character.
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding.
# You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
# You can assume the string to be decoded is valid.


import sys
import unittest


def fn(string):
    count = 0
    prev = ""
    final = ""
    for char in string:
        if char == prev:
            count += 1
        else:
            if len(prev) != 0:
                final += (str(count) + prev)
            prev = char
            count = 1
    if len(prev) != 0:
        final += (str(count) + prev)
    return final


class TestRunLengthEncode(unittest.TestCase):

    def test1(self):
        self.assertEqual(fn("AAAABBBCCDAA"), "4A3B2C1D2A")

    def test2(self):
        self.assertEqual(fn("AAAAABBBCCDAA"), "5A3B2C1D2A")

    def test3(self):
        self.assertEqual(fn("ABC"), "1A1B1C")


if __name__ == '__main__':
    unittest.main()
