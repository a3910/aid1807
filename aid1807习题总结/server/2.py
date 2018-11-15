# from socket import *
# from time import *
# # 创建套接字
# s = socket(AF_INET, SOCK_STREAM)
# # 绑定地址
# s.bind(('0.0.0.0', 3910))
# # 设置监听
# s.listen(5)

# # 等待客户端链接
# while True:
#     print("等待连接...")
#     c, addr = s.accept()
#     print('Connect from', addr)
# # 接收信息

#     while True:
#         data = c.recv(1024).decode()
#         if not data:
#             break
#         print("Receive from:", data)
#         n = c.send("beautiful".encode())
#         print("send %d bytes" % n)
#     c.close()
# s.close()


# from socket import *
# #创建套接字
# s = socket(AF_INET,SOCK_STREAM)
# #发起连接
# s.connect(('127.0.0.1',3910))
# while True:
#     #发送信息
#     try:
#         data = input('发送')
#         s.send(data.encode())
#         if not data:
#             break
#         data = s.recv(1024).decode()
#         print("Receive from",data)
#     except Exception as e:
#         print("find:",e)


# s.close()


# from socket import *
# import os,sys
# import signal

# #创建套接字
# HOST = "0.0.0.0"
# PORT = 8888
# ADDR = (HOST,PORT)

# def client_handler(c):
#     print("Connect from ",c.getpeername())
#     try:
#         while True:
#             data = c.recv(1024).decode()
#             if not data:
#                 break
#             print(data)
#             c.send(b"Receive your message")
#     except (KeyboardInterrupt,SystemExit):
#         sys.exit("退出进程")
#     except Exception as e:
#         print(e)
#     c.close()
#     sys.exit(0) #子进程结束


# s = socket()
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# s.bind(ADDR)
# s.listen(5)

# print("Parent process wait connect")
# #对僵尸进程处理
# signal.signal(signal.SIGCHLD,signal.SIG_IGN)

# while True:
#     try:
#         c,addr = s.accept()
#     except KeyboardInterrupt:
#         s.close()
#         sys.exit("服务器退出")
#     except Exception as e:
#         print(e)
#         continue
#     #创建子进程处理客户端请求
#     pid = os.fork()

#     if pid == 0:
#         s.close()
#         #处理客户端请求
#         client_handler(c)
#     else:
#         c.close()
#         continue

from socket import *
import sys
import time

# 实现各种功能请求


class TftpClient(object):
    def __init__(self, s):
        self.s = s

    def do_list(self):
        self.s.send(b'L')  # 发送请求类型
        # 接收服务器回应
        data = self.s.recv(1024).decode()
        if data == "OK":
            data = self.s.recv(4096).decode()
            files = data.split('#')
            for file in files:
                print(file)
            print("文件展示完毕")
        else:
            # 请求失败原因
            print(data)

    def do_get(self, filename):
        self.s.send(('G ' + filename).encode())
        data = self.s.recv(1024).decode()
        if data == 'OK':
            fd = open(filename, 'wb')
            while True:
                data = self.s.recv(1024)
                if data == b'##':
                    break
                fd.write(data)
            fd.close()
            print("%s 下载完成\n" % filename)
        else:
            print(data)

    def do_put(self, filename):
        try:
            fd = open(filename, 'rb')
        except:
            print("上传文件不存在")
            return
        self.s.send(("P "+filename).encode())
        data = self.s.recv(1024).decode()
        if data == 'OK':
            while True:
                data = fd.read(1024)
                if not data:
                    break
                self.s.send(data)
            fd.close()
            time.sleep(0.1)
            self.s.send(b'##')
            print("%s 上传完毕" % filename)
        else:
            print(data)

# 创建套接字建立连接


def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return
    host = sys.argv[1]
    port = int(sys.argv[2])
    ADDR = (host, port)

    s = socket()
    s.connect(ADDR)

    tftp = TftpClient(s)  # __init__是否需要传参

    while True:
        print("")
        print("==========命令选项===========")
        print("**********  list  *********")
        print("********** get file  ******")
        print("********** put file  ******")
        print("**********  quit  *********")
        print("=============================")

        cmd = input("输入命令>>")

        if cmd.strip() == "list":
            tftp.do_list()
        elif cmd[:3] == "get":
            filename = cmd.split(' ')[-1]
            tftp.do_get(filename)
        elif cmd[:3] == "put":
            filename = cmd.split(' ')[-1]
            tftp.do_put(filename)
        elif cmd.strip() == "quit":
            s.send(b'Q')
            s.close()
            sys.exit("欢迎使用")
        else:
            print("请输入正确命令！")


if __name__ == "__main__":
    main()
