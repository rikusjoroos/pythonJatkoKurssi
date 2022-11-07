# -*- coding: utf-8 -*-

import threading

def thread_function(i):
    global count
    count = count + 1
    print("Start thread", i, "count =", count)
    j=0
    for _ in range(1000000):
        j=j+1
    count = count -1
    print("Completed thread", i, "count =", count)

thlist=[]
N = 10
count = 0
for i in range(N):
    th = threading.Thread(target = thread_function, args = (i,))
    thlist.append(th)
    th.start()
    
    

print("Threads started")

for th in thlist:
    th.join()
    
print("All threads completed")

