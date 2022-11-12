# -*- coding: utf-8 -*-
import socket
import multiprocessing as mp
import threading as th

localIP = "127.0.0.1"
localPort = 20001
buffSize = 1024

def server_function(queue, client_address, UDPSocket, terminate_queue):
    while True:
        in_msg = queue.get()
        
        if in_msg == "terminate":
            terminate_queue.put(client_address)
            print("Terminating")
            return
        
        out_msg = 'Got message "%s"'%(in_msg)
        bytesToSend = str.encode(out_msg)
        UDPSocket.sendto(bytesToSend, client_address)

def terminate_thread():
    while True:
        a=terminate_queue.get()
        with client_lock:
            client_list.pop(a, None)
            print("Client " +str(a)+" removed")
        
if __name__ =="__main__":
    
    UDPSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
    UDPSocket.bind((localIP, localPort))
    client_list = {}
    client_lock = th.Lock()
    terminate_queue=mp.Queue()
    
    term_thread = th.Thread(target = terminate_thread, args = ())
    term_thread.start()
    
    print("UDP server up and listening!")
    
    while True:
        bytesAddressPair = UDPSocket.recvfrom(buffSize)
        message=bytesAddressPair[0]
        address=bytesAddressPair[1]
        print(address, ":", message.decode())
        with client_lock:
            if address not in client_list.keys():
                queue = mp.Queue()
                ps = mp.Process(target = server_function, args=(queue, address, UDPSocket, terminate_queue))
                client_list[address] = (queue, ps)
                ps.start()
                print("Client" +str(address)+ "added.")
                
        client_queue = client_list(address[0])
        client_queue.put(message.decode())