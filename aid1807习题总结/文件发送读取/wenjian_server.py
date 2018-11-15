from socket import *
from time import sleep

s = socket()

s.bind(('0.0.0.0', 8889))
s.listen(5)

c, addr = s.accept()
print("Connect from ", addr)

f = open('timg.jpeg', 'rb')
# 将文件名称告知对方
c.send('timg.jpeg'.encode())
sleep(0.1)

while True:
    data = f.read(1024)
    if not data:
        break
    c.send(data)

sleep(0.1)
c.send('##'.encode())

data = c.recv(1024)
print(data.decode())

f.close()
c.close()
s.close()
