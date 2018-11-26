from functools import reduce
import unittest


def algo(arr):
    return_arr = []
    for i, ele in enumerate(arr):
        temp = list(arr)
        temp.pop(i)
        return_arr.append(reduce(lambda x, y: x * y, temp))
    return return_arr


class TestAlgo(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(algo([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
        self.assertEqual(algo([3, 2, 1]), [2, 3, 6])
        self.assertEqual(algo([]), [])


if __name__ == '__main__':
    unittest.main()
