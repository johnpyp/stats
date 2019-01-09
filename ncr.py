import sys
import math


n = int(sys.argv[1])
r = int(sys.argv[2])

print(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))
