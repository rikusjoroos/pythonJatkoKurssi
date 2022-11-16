# -*- coding: utf-8 -*-
import socket

localIP = "127.0.0.1"
localPort = 20001

buffSize = 1024

TCPSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
TCPSocket.bind((localIP, localPort))

print("TCP server up and listening!")

while True:
    TCPSocket.listen()
    conn, addr = TCPSocket.accept()
    print(f"Connected from{addr}")
    
    socket_open = True
    while socket_open:
        data = conn.recv(buffSize)
        
        if not data:
            socket_open = False
        else:
            print("Got message: ", data.decode())
            msg = "Hello TCP client\n"
            print("Send : ", msg)
            conn.sendall(msg.encode())
            print("Send : ", data.decode())
            conn.sendall(data)
    