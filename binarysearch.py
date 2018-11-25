
import math
lst = list(range(123012931))


def binary_search(lis, item):
    maximum_iterations = math.ceil(math.log(len(lis))) + 10
    minimum = 0
    maximum = len(lis) - 1
    for x in range(maximum_iterations):
        index = math.floor((minimum + maximum) / 2)
        print(lis[index], item, lis[index] < item)
        if lis[index] == item:
            print(lis[index], x)
            return True
        if lis[index] > item:
            maximum = index
        if lis[index] < item:
            minimum = index + 1


binary_search(lst, 47100123)
