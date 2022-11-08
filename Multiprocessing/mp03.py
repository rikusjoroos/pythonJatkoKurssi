# -*- coding: utf-8 -*-

import multiprocessing as mp

def inc_counter(counter):
    with counter.get_lock():
        counter.value+=1
        return counter.value

def dec_counter(counter):
    with counter.get_lock():
        counter.value-=1
        return counter.value
    

def compute_function(i, p2m_queue, m2p_queue, counter, active_process):
    c = inc_counter(counter)
    
    with active_process.get_lock():
        active_process[i]=1
        s=str(active_process[:])
    
    msg = m2p_queue.get()
    print(i, 'start', "msg = ", msg, ", counter= ",c, " active_process=", s)
    
    j = 0
    
    for _ in range (10_000_000):
        j = j + 1
    
    c = dec_counter(counter)
    with active_process.get_lock():
        active_process[i]=0
        s=str(active_process[:])
    print(i, "completed")
    
    p2m_queue.put("process " +str(i)+" completed" + ", counter= " + str(c) +" active_process=" + s)


if __name__=="__main__":
    ps_list=[]
    p2m_queue=mp.Queue()
    m2p_list=[]
    
    N = 10
    
    counter = mp.Value("i", 0)
    active_process = mp.Array("i", N)
    
    for i in range(10):
        m2p_queue = mp.Queue()
        m2p_list.append(m2p_queue)
        
        ps = mp.Process(target = compute_function, args = (i, p2m_queue, m2p_queue, counter, active_process))
        m2p_queue.put("Main started process " + str(i))
        
        ps.start()
        ps_list.append(ps)
    
    for ps in ps_list:
        ps.join()
    while not p2m_queue.empty():
        print("main:" + p2m_queue.get())
        

