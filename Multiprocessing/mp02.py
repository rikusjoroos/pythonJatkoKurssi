# -*- coding: utf-8 -*-

import multiprocessing as mp



def compute_function(i, p2m_queue, m2p_queue):
    msg = m2p_queue.get()
    print(i, 'start', "msg = ", msg )
    
    j = 0
    
    for _ in range (10_000_000):
        j = j + 1
    
    print(i, "completed")
    
    p2m_queue.put("process " +str(i)+" completed")


if __name__=="__main__":
    ps_list=[]
    p2m_queue=mp.Queue()
    
    m2p_list=[]
    
    for i in range(10):
        m2p_queue = mp.Queue()
        m2p_list.append(m2p_queue)
        
        ps = mp.Process(target = compute_function, args = (i, p2m_queue, m2p_queue))
        m2p_queue.put("Main started process " + str(i))
        
        ps.start()
        ps_list.append(ps)
    
    for ps in ps_list:
        ps.join()
    while not p2m_queue.empty():
        print("main:" + p2m_queue.get())
        

