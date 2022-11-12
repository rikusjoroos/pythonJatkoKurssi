# -*- coding: utf-8 -*-

import socket
import time

serverAddressPort = ("127.0.0.1", 20001)

bufferSize = 1024

UDPSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

for _ in range(10):
    msg = "Hello UDP server"
    bytesToSend = str.encode(msg)
    UDPSocket.sendto(bytesToSend, serverAddressPort)
    bytesAddressPair = UDPSocket.recvfrom(bufferSize)
    message=bytesAddressPair[0]
    address=bytesAddressPair[1]
    
    print(address, ":", message.decode())
    
    time.sleep(1.0)
msg = "terminate"
bytesToSend = str.encode(msg)
UDPSocket.sendto(bytesToSend, serverAddressPort)