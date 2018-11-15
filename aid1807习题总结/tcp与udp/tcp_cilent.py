# 2.py
from socket import *
# 创建套接字
sockfd = socket(AF_INET, SOCK_STREAM)
# 发起连接
server_addr = ('127.0.0.1', 3910)
sockfd.connect(server_addr)
while True:
    # 消息发送接收
    data = input('发送>>')
    sockfd.send(data.encode())
    if data == '':
        break
    data = sockfd.recv(1024)
    print("接收到:", data.decode())

# 关闭套接字
sockfd.close()

# from socket import *
# #创建套接字
# sockfd = socket(AF_INET,SOCK_STREAM)
# #发起连接
# server_addr = ('127.0.0.1',3911)
# sockfd.connect(server_addr)
# #消息发送接收
# while True:
#     data = input('发送:')
#     if not data:
#         break
#     sockfd.sendall(data.encode())
#     data = sockfd.recv(1024)
#     print("接收到",data.decode())

# #关闭套接字
# sockfd.close()
