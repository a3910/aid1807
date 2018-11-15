# udp_client.py

from socket import *
import sys
if len(sys.argv)< 3:
    print('''
        argv is error!
        run as
        python3 udp_client.py 127.0.0.1 3914
        ''')
    raise
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)

#创建数据报套接字
sockfd=socket(AF_INET,SOCK_DGRAM)

#收发消息
while True:
    data = input('奇策十二,可挽狂澜:')
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    data,addr = sockfd.recvfrom(1000)
    print("富强民主文明和谐,自由平等公正法治,爱国敬业诚信友善",data.decode())

sockfd.close()