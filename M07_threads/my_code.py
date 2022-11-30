import threading
import concurrent.futures as cf
import time

count = 0
count_lock = threading.Lock()
def external_function():
    global count
    with count_lock:
        count = count + 1


def external_count():
    global count
    return count

#Sample function for test purposes
def computing5s(thr_id):
    time.sleep(5)
    external_function()
            
    return thr_id, thr_id*thr_id

def init_values(f):
    f_values={}
    future_list = []
    #Between BEGIN and END there is too slow solution.
    #Rewrite the solution to utilize parallelism
    #
    #BEGIN
    with cf.ThreadPoolExecutor(50) as executor:
        for i in range(50):
                fu = executor.submit(f,i)
                future_list.append(fu)
        for fu in cf.as_completed(future_list):
            idx, val=fu.result()
            f_values[idx]=val
    #END
    
    return f_values


#Test software under this if        
if __name__ == "__main__":
    ret=init_values(computing5s)
    print(count)
    print(ret)
