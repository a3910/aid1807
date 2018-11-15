from socket import *
# 创建数据报套接字
sockfd = socket(AF_INET, SOCK_DGRAM)
# 绑定地址
server_addr = ('0.0.0.0', 3916)
sockfd.bind(server_addr)
# 收发消息
while True:
    data, addr = sockfd.recvfrom(1000)
    print("Receive from %s:%s" % (addr, data.decode()))
    sockfd.sendto("谁敢与我大战300回合".encode(), addr)

sockfd.close()
# 奇策十二,可挽狂澜
# 富强民主文明和谐,自由平等公正法治,爱国敬业诚信友善
