from socket import *
from time import *
import os
import sys
import signal


# 文件库路径
file_path = "/home/tarena/mkv/"
host = '0.0.0.0'
port = 8000
ADDR = (host, port)
# 定义类,将文件服务器功能写在类中


class TftpServer(object):
    def __init__(self, c):
        self.c = c

    def do_list(self):
        file_list = os.listdir(file_path)
        if not file_list:
            self.c.send("文件库为空")
            return
        else:
            self.c.send(b'OK')
            sleep(0.1)
        files = ''
        for file in file_list:
            if file[0] != '.' and \
                    os.path.isfile(file_path+file):
                files = files + file + '#'
        self.c.sendall(files.encode())

    def do_get(self, filename):
        try:
            fd = open(file_path+filename, 'rb')
        except:
            self.c.send('文件不存在'.encode())
            return
        self.c.send(b'OK')
        sleep(0.1)
        # 发送文件
        while True:
            data = fd.read(1024)
            if not data:
                sleep(0.1)
                self.c.send(b"##")
                break
            self.c.send(data)
            fd.close()
        print("文件发送完毕")


def main():
    # 创建套接字
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 绑定地址
    s.bind(ADDR)
    # 设置监听
    s.listen(5)

    # 对僵尸进程处理
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    print('Listen the port 8000...')

    # 等待客户端请求
    while True:
        try:
            print("等待链接...")
            c, addr = s.accept()
        except (KeyboardInterrupt, SystemExit):
            sys.exit("退出服务器")
        except Exception as e:
            print("服务器异常", e)
            continue
        print("客户端登录:", addr)

        pid = os.fork()

        if pid == 0:
            s.close()
            tftp = TftpServer(c)
            while True:
                data = c.recv(1024).decode()
                if data == "list":
                    tftp.do_list()
                elif data[0] == 'G':
                    filename = data.split(' ')[-1]
                    tftp.do_get(filename)                    
                    sys.exit(0)
        else:
            c.close()
            continue


if __name__ == "__main__":
    main()
