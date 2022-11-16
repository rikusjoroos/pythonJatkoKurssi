# -*- coding: utf-8 -*-
import socket
import time

serverAddressPort = ("127.0.0.1", 7537)

bufferSize = 1024

TCPSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
TCPSocket.connect(serverAddressPort)
for _ in range(2):
    msg = "5"
    print("Send: ", msg)
    TCPSocket.send(msg.encode()) 
    
    print("wait message")
    
    data = TCPSocket.recv(bufferSize)
    data = data.decode()
    data = data.splitlines()
    msg1 = data[0]
    print("Received : " ,msg1)
    
    
print("Close Socket")
TCPSocket.close()
