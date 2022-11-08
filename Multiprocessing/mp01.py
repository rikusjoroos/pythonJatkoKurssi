# -*- coding: utf-8 -*-

import multiprocessing as mp
import threading
from datetime import datetime


def compute_function(i, queue):
    msg = queue.get()
    print(i, 'start', "msg = ", msg )
    
    j = 0
    
    for _ in range (10_000_000):
        j = j + 1
    
    print(i, "completed")
    
    queue.put("process " +str(i)+" completed")


if __name__=="__main__":
    ps_list=[]
    queue=mp.Queue()
    
    for i in range(10):
        ps = mp.Process(target = compute_function, args = (i, queue))
        queue.put("Main started process " + str(i))
        ps.start()
        ps_list.append(ps)
    
    for ps in ps_list:
        ps.join()
        while not queue.empty():
            print("main:" + queue.get())
        

