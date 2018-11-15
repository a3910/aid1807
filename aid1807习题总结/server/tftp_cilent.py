from socket import *
import sys
from time import *


class TftpClient(object):
    def __init__(self, s):
        self.s = s

    def do_list(self):
        self.s.send(b'list')  # 发送请求
        # 等待回复
        data = self.s.recv(1024).decode()
        if data == 'OK':
            data = self.s.recv(4096).decode()
            files = data.split("#")
            for file in files:
                print(file)
            print("文件列表展示完毕\n")
        else:
            # 由服务器发送失败原因
            print(data)

    def do_get(self, filename):
        self.s.send(("G"+filename).encode())
        data = self.s.recv(1024).decode()
        if data == 'OK':
            fd = open(filename, 'wb')
            while True:
                data = self.s.recv(1024)
                if data == b'##':
                    break
                fd.write(data)
            fd.close()
            print("%s 下载完毕\n" % filename)
        else:
            print(data)

    def do_quit(self):
        self.sockfd.send(b'Q')


def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return
    host = sys.argv[1]
    port = int(sys.argv[2])
    ADDR = (host, port)

    s = socket(AF_INET, SOCK_STREAM)

    try:
        s.connect(ADDR)
    except:
        print("链接服务器失败")
        return

    tftp = TftpClient(s)  # __init__是否需要传参

    while True:
        print("")
        print("==========命令选项===========")
        print("**********  list  *********")
        print("********** get file  ******")
        print("********** put file  ******")
        print("**********  quit  *********")
        print("=============================")


        cmd = input("请输入命令")

        if cmd.strip() == "list":
            tftp.do_list()
        elif cmd[:3] == 'get':
            filename = cmd.split(' ')[-1]
            tftp.do_get(filename)
        else:
            print("请输入正确命令")
            continue


if __name__ == "__main__":
    main()
