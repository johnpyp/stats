import sys
import random
from itertools import groupby
import collections
import matplotlib.pyplot as plt
import mpld3
import json

inputNum = int(sys.argv[1])
lis = []
counter = 0
for flip in range(inputNum):
    res = random.randint(0, 1)
    if res == 0:
        lis.append(counter)
        counter = 0
    else:
        counter = counter + 1
if counter != 0:
    lis.append(counter)


freq = dict(collections.Counter(lis))
od = collections.OrderedDict(sorted(freq.items()))

print(od)
fig = plt.figure(figsize=(18, 5))
ax = fig.add_subplot(1, 1, 1)
ax.bar(od.keys(), od.values(), align='center')
for i, v in enumerate(od.values()):
    ax.text(i, v, str(v), color='red', fontweight='bold')

# ax.hist(lis, bins=range(min(lis), max(lis) + 1, 1))
# mpld3.show()
mpld3.save_html(fig, '10000000.html')
