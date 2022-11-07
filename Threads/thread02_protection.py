# -*- coding: utf-8 -*-

import threading

def thread_function(i):
    global count
    global lock_count
    
    with lock_count:
        count = count + 1
        print("Start thread", i, "count =", count)
        
    with lock_count
        count2 = count2 + count
    j=0
    for _ in range(1000000):
        j=j+1
        
    with lock_count:
        count = count - 1
        print("Completed thread", i, "count =", count)

thlist=[]
count = 0
count2 = 1234
N = 10
lock_count = threading.Lock()
for i in range(N):
    th = threading.Thread(target = thread_function, args = (i,))
    thlist.append(th)
    th.start()
    
    

print("Threads started")

for th in thlist:
    th.join()
    
print("All threads completed")

