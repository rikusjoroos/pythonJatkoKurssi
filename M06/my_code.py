import threading
import concurrent.futures as cf
import time


#heavy_computing for test purposes!
#You may modify the function if necessary
if __name__ == "__main__":
    def heavy_computing(idx):
        print('->heavy_computing('+str(idx)+')')
        time.sleep(10)
        print('<-heavy_computing('+str(idx)+')')
        return idx, idx*idx

def start_threads(f, N):
    future_list = []
    with cf.ThreadPoolExecutor() as executor:
        for i in range(N):
            fu = executor.submit(f, i)
            future_list.append(fu)
    return future_list

def wait_threads(th_list):
    result_list = []
    return_list = []
    for fu in cf.as_completed(th_list):
        result_list.append(fu.result())
    for j in range(len(result_list)):
        return_list.append(result_list[j][1])
    return_list.sort()
    return return_list
    
    

#Test software under this if        
if __name__ == "__main__":
    N=10

    print('None started')
    th_list=start_threads(heavy_computing, N)
    print('Wait...')
    ret=wait_threads(th_list)
    print('All futures completed')
    print(ret)
