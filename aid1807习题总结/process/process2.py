# import multiprocessing as mp
# from time import ctime,sleep

# a=1
# def fun():
#     sleep(3)
#     global a
#     print("a=",a)
#     a=10000
#     print("子进程结束")


# #创建进程对象
# p=mp.Process(target=fun)
# #启动程序
# p.start()
# sleep(2)
# print("这是父进程")
# #回收进程

# p.join()
# # print("parent a = ",a)
# # while True:
# #     pass

import os
from multiprocessing import Process
from time import sleep


# size = os.path.getsize('while.py')
# pid = os.fork()
# if pid < 0:
#     print("不详动")
# elif pid == 0:
#     sleep(3)
#     n = size // 2
#     fw = open('child.py', 'w')
#     with open('while.py', 'r') as f:
#         while True:
#             if n < 64:
#                 data = f.read(n)
#                 fw.write(data)
#                 break
#             data = f.read(64)
#             fw.write(data)
#             n -= 64
#     f.close()

# else:
#     fw = open('parent.py', 'w')
#     with open("while.py", 'r') as f:
#         f.seek(size//2, 0)
#         while True:
#             data = f.read(64)
#             if not data:
#                 break
#             fw.write(data)
#     fw.close()


size = os.path.getsize('./timg.jpeg')
pid = os.fork()
if pid < 0:
    print("不详动")
elif pid == 0:
    sleep(3)
    n = size // 2
    fw = open('1.jpeg', 'wb')
    with open('./timg.jpeg', 'rb') as f:
        while True:
            if n < 1024:
                data = f.read(n)
                fw.write(data)
                break
            data = f.read(1024)
            fw.write(data)
            n -= 1024
    f.close()

else:
    fw = open('2.jpeg', 'wb')
    with open("./timg.jpeg", 'rb') as f:
        f.seek(size//2, 0)
        while True:
            data = f.read(1024)
            if not data:
                break
            fw.write(data)
    fw.close()
