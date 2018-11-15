from socket import *
# 创建套接字
sockfd = socket(AF_INET, SOCK_STREAM)
# 绑定地址
sockfd.bind(('0.0.0.0', 3910))

# 设置监听

sockfd.listen(3)
# 等待客户端连接

print('Waiting for connect...')
connfd, addr = sockfd.accept()
print('Connect from', addr)
while True:
    # 消息收发
    data = connfd.recv(1024).decode()
    if data == '':
        break
    print("Receive:", data)
    # data = connfd.recv(1024)
    # if data == b'':
    #     break
    # print("Receive:", data.decode())
    n = connfd.send("Receive your message".encode())
    # n = connfd.send(b"Receive your message")
    print("send %d bytes" % n)
# 关闭套接字
connfd.close()
sockfd.close()


# from socket import *
# #创建套接字
# sockfd=socket(AF_INET,SOCK_STREAM)
# #绑定地址
# sockfd.bind(('0.0.0.0',3911))
# #设置监听
# sockfd.listen(5)
# #等待客户端连接
# while True:
#     print("Waiting for Connect...")
#     connfd,addr=sockfd.accept()
#     print("Connect from",addr)
#     #消息收发
#     while True:
#         data = connfd.recv(1024).decode()
#         if data == '':
#             break
#         print('Receive:',data)
#         n = connfd.send(b"The electric light of your fingertips is my everlasting faith. The solo super electromagnetic gun will last forever.")
#         print("send%d bytes"%n)
# #关闭套接字
#     connfd.close()
# sockfd.close()
