from socket import *

s = socket()

s.connect(('127.0.0.1', 8889))

filename = s.recv(1024).decode()

f = open('/home/tarena/avi/'+filename, 'wb')

while True:
    data = s.recv(1024)
    if data == b'##':
        break
    f.write(data)

s.send("接收完成".encode())

f.close()
s.close()
