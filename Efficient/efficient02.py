# -*- coding: utf-8 -*-
from datetime import datetime

N  = 1000000
a = 0
b = 0

def f(N):
    global a
    
    for j in range(N):
        a = a+1

def g(N, b0):
    b = b0
    
    for j in range(N):
        b = b+1
    return b
        


t0 = datetime.now()
f(N)
t1 = datetime.now()
b = g(N,b)
t2 = datetime.now()
print((t1-t0).total_seconds()*1000)
print((t2-t1).total_seconds()*1000)
