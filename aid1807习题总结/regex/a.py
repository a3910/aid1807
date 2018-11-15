import re 
import sys 
 
def getAddress(port):
    f = open('./1.txt')
    
    while True:
        data = ''
        #获取每一段内容
        for line in f:
            if line != '\n':
                data += line
            else:
                break
        # print(data)
        #文件结尾跳出循环
        if not data:
            return "Not Found The port"
            # break
        #匹配到每段的首个单词
        try:
            PORT = re.match(r'\S+',data).group()
            # print(PORT)
        except Exception as e:
            print(e)
            continue
        #判断是否为目标段
        if PORT == port:
            pattern = r'address is (\w{4}\.\w{4}\.\w{4})'
            #(\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}/\d+|Unknown)
            addr = re.search(pattern,data).group(0)
            return addr
 
if __name__ == "__main__":
    port = sys.argv[1]
    print(getAddress(port))


