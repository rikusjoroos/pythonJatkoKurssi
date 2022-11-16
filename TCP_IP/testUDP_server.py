# -*- coding: utf-8 -*-

import socket

localIP = "127.0.0.1"
localPort = 20001

buffSize = 1024

UDPSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
UDPSocket.bind((localIP, localPort))

print("UDP server up and listening!")

while True:
    bytesAddressPair = UDPSocket.recvfrom(buffSize)
    message=bytesAddressPair[0]
    address=bytesAddressPair[1]
    
    print(address, ":", message.decode())
    
    msg = "Hello UDP Client!"
    bytesToSend = str.encode(msg)
    UDPSocket.sendto(bytesToSend, address)