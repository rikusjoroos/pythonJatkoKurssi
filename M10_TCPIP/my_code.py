import socket

def fetch_number(IP, p):
    bufferSize = 1024
    UDPSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
    msg = "Anna luku!"
    UDPSocket.sendto(msg.encode(), (IP, p))
    bytesAddressPair = UDPSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    number = int(message.decode())
    return number
    

if __name__=='__main__':
    pass
    #Write test code here

