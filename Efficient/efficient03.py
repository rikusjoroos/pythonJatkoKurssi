# -*- coding: utf-8 -*-
from datetime import datetime
import random


N = 10000000

l=list()

for i in range(N) :
    l.append(random.randint(0, 10000000))


t0 = datetime.now()

largest0 = l[0]
for n in l:
    if n > largest0:
        largest0 = n

t1 = datetime.now()

largest1 = max(l)

t2 = datetime.now()
print((t1-t0).total_seconds()*1000)
print((t2-t1).total_seconds()*1000)
print(largest0, largest1)