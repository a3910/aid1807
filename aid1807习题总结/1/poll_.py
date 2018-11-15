from socket import *
from select import *

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 3910))
s.listen(5)

# 创建poll对象
p = poll()
# fileno ---> IO對象的字典
fdmap = {s.fileno(): s}
# 注冊關注的IO
p.register(s, POLLIN | POLLERR)


while True:
    # 進行IO監控
    events = p.poll()
    for fd, event in events:
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print("Connect from", addr)
            # 注册新的IO 维护地图
            p.register(c, POLLIN)
            fdmap[c.fileno()] = c
        else:
            data = fdmap[fd].recv(1024)
            if not data:
                p.unregister(fd)  # 从关注移除
                fdmap[fd].close()
                del fdmap[fd]  # 从地图删除
            else:
                print(data.decode())
                fdmap[fd].send(b'Receive')
