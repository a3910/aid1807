# # global2.py


# v = 100
# def fn():
#     v = 200  # 不建议在global之前来创建局部变量
#     print(v)

#     # global v
#     v = 300
#     print(v)


# fn()
# print('v=', v)  # 200
# static_method.py
 
#1 
class A:
    #@staticmethod
    def myadd(self,a,b):
        return a + b
 
a = A()  # 创建实例 
print(a.myadd(100, 200))  # 300
# a = A()  # 创建实例
print(a.myadd(300, 400))  # 700


#2
class A:
    #@staticmethod
    def myadd(a,b):
        return a + b


print(A.myadd(100, 200))  # 300

print(a.myadd(300, 400))  # 700
a = A()  # 创建实例
print(a.myadd(300, 400))  #报错
#TypeError: myadd() takes 2 positional 
#arguments but 3 were given
