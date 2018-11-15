import os
from multiprocessing import Process
from time import sleep
filename = "./timg.jpeg"
# 获取文件的大小
size = os.path.getsize(filename)
# 如果子进程使用父进程的对象，那么相互之间有偏移量的影响
# f = open(filename, 'rb')
# 复制前半部分


def copy1():
    f = open(filename, 'rb')
    # sleep(1)
    n = size // 2
    fw = open('1.jpeg', 'wb')

    while True:
        if n < 1024:
            data = f.read(n)
            fw.write(data)
            break
        data = f.read(1024)
        fw.write(data)
        n -= 1024

    f.close()
    fw.close()


# 复制后半部分
def copy2():
    f = open(filename, 'rb')
    fw = open('2.jpeg', 'wb')
    f.seek(size // 2, 0)
    while True:
        data = f.read(1024)
        if not data:
            break
        fw.write(data)
    fw.close()
    f.close()


p1 = Process(target=copy1)  # args=('timg.jpeg',)
p2 = Process(target=copy2)  # args=('timg.jpeg',))
p1.start()
p2.start()
p1.join()
p2.join()
