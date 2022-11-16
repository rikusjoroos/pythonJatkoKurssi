# -*- coding: utf-8 -*-

import socket
import time

serverAddressPort = ("127.0.0.1", 7538)

bufferSize = 1024

UDPSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

while True:
    msg = "20"
    bytesToSend = str.encode(msg)
    UDPSocket.sendto(bytesToSend, serverAddressPort)
    bytesAddressPair = UDPSocket.recvfrom(bufferSize)
    message=bytesAddressPair[0]
    address=bytesAddressPair[1]
    
    print(address, ":", message.decode())
    
    time.sleep(1.0)