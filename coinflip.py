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
total = 0
while total < inputNum:
    res = random.randint(0, 1)
    if res == 0:
        lis.append(counter)
        counter = 0
        total += 1
    else:
        counter += 1
if counter != 0:
    lis.append(counter)


freq = dict(collections.Counter(lis))
od = collections.OrderedDict(sorted(freq.items()))

print(od)
fig = plt.figure(figsize=(18, 5))
ax = fig.add_subplot(1, 1, 1)
ax.bar(od.keys(), od.values(), align='center')
for key in od.keys():
    ax.text(key, od[key], str(od[key]), color='red', fontweight='bold')

plt.show()
# ax.hist(lis, bins=range(min(lis), max(lis) + 1, 1))
# mpld3.show()

mpld3.save_html(fig, sys.argv[1] + '.html')
