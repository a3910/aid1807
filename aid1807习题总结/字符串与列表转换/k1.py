# 1. 打印 1 ~ 20 的整数,打印在一行内
#   1 2 3 4 5 6 .... 18 19 20
#   print(i, end=' ')
l = []
i = 1
while i <= 20:
    print(i, end=' ', sep='#')

    l.append(i)
    i += 1
else:
    print()  # 换行
print(l)
# s = ''.join(l)
# print(s)
b =",".join([str(i) for i in l])
print(b)
#     # print(end='\n')  # 换行
l=[1,2,3,4]
s =" ".join('%s' %id for id in l)
print(s)
# l=['a','b','c']
# s = ''.join(l)
# print(s)
# s = '1234'
# print(*s,sep='#')
# s='%20d'%1234
# print(s)
# s = '1234'
# print(s.center(20,'#'))
