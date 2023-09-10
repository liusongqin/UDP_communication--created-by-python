'''created by Liu Songqin'''
from socket import * 
ADDR = ('' , 21400) 
udpSerSock = socket(AF_INET,SOCK_DGRAM) 
udpSerSock.bind(ADDR)
clients = set()
while True:
    data, addr = udpSerSock.recvfrom(1024) 
    print addr
    print data
    clients.add(addr)
    for client in clients:
        udpSerSock.sendto(data, client)
udpSerSock.close()
