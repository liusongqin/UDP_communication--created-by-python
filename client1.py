'''created by Liu Songqin'''
from socket import *
ADDR = ('8.130.135.22', 21405)
udpCliSock = socket(AF_INET, SOCK_DGRAM)
data = '有用户进入服务器'
udpCliSock.sendto(data, ADDR)
while True:
    data, addr = udpCliSock.recvfrom(2048)
    data, addr = udpCliSock.recvfrom(2048)
    print addr
    print data
    data = raw_input('> ')
    udpCliSock.sendto(data, ADDR)
udpCliSock.close()
