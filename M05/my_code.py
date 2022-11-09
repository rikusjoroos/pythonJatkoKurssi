import threading
import time

N=10

#heavy_computing for test purposes!
#You may modify the function if necessary
if __name__ == "__main__":
    def heavy_computing(idx):
        print('->heavy_computing('+str(idx)+')')
        time.sleep(10)
        print('<-heavy_computing('+str(idx)+')')

def start_threads(f, N):
    th_list=[]
    for i in range(N):
        th = threading.Thread(target = f, args = (i,))
        th_list.append(th)
        th.start()
    return th_list
        
        
    

def wait_threads(th_list):
    for th in th_list:
        th.join()

#Test software under this if
if __name__ == "__main__":
    th_list=start_threads(heavy_computing, N)
    wait_threads(th_list)

