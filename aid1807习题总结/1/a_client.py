
# sss.py
from socket import *

# 创建套接字
sockfd = socket()

# 发起连接
sockfd.connect(('127.0.0.1', 3911))

while True:
    # 消息收发
    try:
        msg = input("Msg>>")
        if not msg:
            break
        sockfd.sendall(msg.encode())
        data = sockfd.recv(1024)
        print(data.decode())
    except BrokenPipeError as a:
        print(a)
    except KeyboardInterrupt as e:
        print(e)
    except EOFError as d:
        print(d)
sockfd.close()
