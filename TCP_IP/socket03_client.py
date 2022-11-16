# -*- coding: utf-8 -*-
import socket
import time

serverAddressPort = ("127.0.0.1", 20001)

bufferSize = 1024

TCPSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
TCPSocket.connect(serverAddressPort)

msg = "Hello TCP server"
print("Send: ", msg)
TCPSocket.send(msg.encode()) 

print("wait message")

data = TCPSocket.recv(bufferSize)
data = data.decode()
data = data.splitlines()
msg1 = data[0]
print("Received : " ,msg1)

if len(data)>=2:
    msg2 = data[1]
else:
    data = TCPSocket.recv(bufferSize)
    msg2 = data.decode()

print("Received :", msg2)

print("Close Socket")
TCPSocket.close()
