# -*- coding: utf-8 -*-

from datetime import datetime

N = 1000000

t0 = datetime.now()

l = []

for i in range(N):
    if i%2 == 0:
        l.append(i)
        
t1 = datetime.now()
print((t1-t0).total_seconds()*1000)

del l, t0, t1

t0 = datetime.now()

l = [i for i in range(N) if i%2 == 0]

t1 = datetime.now()
print((t1-t0).total_seconds()*1000)


