# num = 100


# class A:
#     def get_number():
#         count = num + 100
#         print(count)


# a = A()
# a.get_number()
# print(num)
from socket import *
import os
import sys

# 发送管理员信息


def do_child(s, addr):
    while True:
        msg = input('管理员信息：')
        msg = "C" + msg
        s.sendto(msg.encode(), addr)


# 用户登录
def do_login(s,user,name,addr):
    if (name in user) or name =="管理员":
        s.sendto









































































































































