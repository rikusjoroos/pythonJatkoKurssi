# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 16:52:07 2022

@author: riku.sjoroos
"""

from datetime import datetime

N = 1000000

l = ["aaa","bbbb","cccc", "dddd"]

t0 = datetime.now()
for i in range(N):
    res1 = ""
    for s in l:
        res1=res1+s

            

t1 = datetime.now()

for i in range(N):
    res2 = "".join(l)
    
t2 = datetime.now()
print((t1-t0).total_seconds()*1000)
print((t2-t1).total_seconds()*1000)
print(res1,res2)
