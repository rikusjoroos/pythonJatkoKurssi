import socket
import sys
import threading
import random

localIP="127.0.0.1"
serverPort=7537
buffSize=1024
count = 0
count_lock = threading.Lock()
server_th = []

TCPServer = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
TCPServer.bind((localIP, serverPort))
TCPServer.listen()
print("TCP server up and listening!")

def server_main(conn, addr):
    global count
    print(f"Connected from{addr}")
    socket_open = True
    data = []
    while socket_open:

        number = conn.recv(buffSize)
        
        if not number:
            socket_open = False
        else:
            print("Got number", number.decode())
            data.append(int(number.decode()))
            total = sum(data)
            print("send data:", total)
            conn.sendall(str(total).encode())
    with count_lock:
        count = count + 1


#You can utilize following client for test purposes
def client_main():
    TCPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    TCPSocket.connect((localIP, serverPort))

    rnd=random.sample(range(-30, 30), 5)
    for r in rnd:
        msg=str(r)
        print('Send:', msg)
        bytesToSend=str.encode(msg)

        TCPSocket.send(bytesToSend)

        #print('Wait message')
        data=TCPSocket.recv(buffSize)
        data=data.decode()
        data=data.splitlines()
        msg1=data[0]
        print('Received:', msg1)

    print('Close socket')
    TCPSocket.close()

    print('Got sum:'+msg1+'. Value shall be '+str(sum(rnd))+', sent data='+str(rnd))
    
    assert int(msg1)==sum(rnd)
    print('Test passed!')

while count < 25:
    conn, addr = TCPServer.accept()
    th = threading.Thread(target=server_main, args = (conn, addr))
    server_th.append(th)
    th.start()
    
print("count: ",count)
#Set True to run the clients
run_client=False

if run_client:
    th_list=[]
    for i in range(20):
        th_list.append(threading.Thread(target=client_main))
        th_list[-1].start()

    for th in th_list:
        th.join()

    for i in range(5):
        th_list.append(threading.Thread(target=client_main))
        th_list[-1].start()

    for th in th_list:
        th.join()


    #After 25 clients the server shall exit
