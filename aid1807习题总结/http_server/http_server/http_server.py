# coding=utf-8

from socket import *
import sys
import re
from threading import Thread
import time
from setting import *


class HTTPServer(object):
    def __init__(self,addr=('0.0.0.0',80)):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.addr = addr
        self.bind(addr)

    def bind(self,addr):
        self.ip = addr[0]
        self.port = addr[1]
        self.sockfd.bind(addr)
        # print(self.port)
    # HTTP服务器启动

    def serve_forever(self):
        self.sockfd.listen(10)
        print('Listen the port %d...' % self.port)
        while True:
            connfd, addr = self.sockfd.accept()
            print("Connect From", addr)
            handle_client = Thread(target=self.handle_request, args=(connfd,))
            handle_client.setDaemon(True)
            handle_client.start()

    def handle_request(self, connfd):
        # 接受浏览器请求
        request = connfd.recv(4096)
            # print(request)
        request_lines = request.splitlines()
        # 获取请求行
        request_line = request_lines[0].decode()

        # 正则提取请求方法和请求内容
        pattern = r'(?P<METHOD>[A-Z]+)\s+(?P<PATH>/\S*)'
        try:
            env = re.match(pattern,request_line).groupdict()
        except:
            response_headlers = 'HTTP/1.1 500 Server Error\r\n'
            response_headlers += '\r\n'
            response_body = "Server Error"
            response = response_headlers +response_body
            connfd.send(response.encode())
            return
            # 将请求发给frame 得到返回数据结果
        status,response_body=self.send_request(env['METHOD'],env['PATH'])
        # 根据响应码组织响应头内容
        response_headlers = self.get_headlers(status)
        #将结果组织为http response 发送给客户端
        response = response_headlers+response_body
        connfd.send(response.encode())
        connfd.close()

        # 和frame 交互，发送 request 获取response
    def send_request(self,method,path):
        s = socket()
        s.connect(frame_addr)
        # 向Webfame
        s.send(method.encode())
        time.sleep(0.1)
        s.send(path.encode())
        return '200','httpserver test'

    def get_headlers(self,status):
        if status == '200':
            response_headlers = 'HTTP/1.1 200 OK'
            response_headlers += '\r\n'
            response_body = "GOOD"


if __name__ == '__main__':
    httpd = HTTPServer(ADDR)
    httpd.serve_forever()
