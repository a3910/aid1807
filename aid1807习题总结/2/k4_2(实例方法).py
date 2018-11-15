#定义一个母公司（阿里巴巴）的类
# 有下面的类属性：
# 1 员工人数  #1000
# 2 公司市值  #20000

# 类方法：
# 1 获取公司的人数：get_number()
# 2 市值增长：profit(*money) #要求传入四个参数分别代表四个季度的增值，计算总市值
# 3 获取公司的市值 get_value()

# 二：定义一个子公司（支付宝）的类，继承母公司
# 有下面的类属性：
# 1 员工人数  #100
# 2 公司市值  #3000

# 新增类方法：
# 1 公司裁员：set_people(num)  #要求传入裁员人数


# 练习实现如下：
# 1 获取子公司的人数：
# 2、子公司4季度增值是[12,13,11,14],获取市值增长后的公司市值
# 3、获取子公司裁员过后人数

# class Alibaba:
#     def __init__(self):       
#         self.per_count = 1000
#         self.per_value = 20000

#     def get_number(self):
#         return self.per_count

#     def profit(self, *money):
#         def mysum(n):
#             return sum(n)
#         self.per_value += mysum(*money)
#         return self.per_value


# class Zhifubao(Alibaba):
#     def __init__(self): 
#         self.per_count = 100
#         self.per_value = 3000
#         #super().__init__()#调用父类init 错误
#     def set_people(self,num):        
#         return self.per_count-num


# a = Alibaba()
# print("母公司员工有%d人"%a.get_number())
# print("公司市值是%d亿元"%a.profit([54, 43, 39, 62]))
# print()

# b = Zhifubao()
# print("子公司员工有%d人"% b.get_number())
# print("子公司市值是%d亿元"%b.profit([12, 13, 11, 14]))
# print("子公司裁员过后人数是%d人"%b.set_people(10))



per_count = 1000
per_value = 20000
class Alibaba:
    # def __init__(self):       
        # self.per_count = 1000
        # self.per_value = 20000

    def get_number(self):
        global per_count
        return per_count

    def profit(self, *money):
        def mysum(n):
            return sum(n)
        global per_value 
        per_value+= mysum(*money)
        return per_value

a = Alibaba()
print("母公司员工有%d人"%a.get_number())
print("公司市值是%d亿元"%a.profit([54, 43, 39, 62]))
print()



per_count = 100
per_value = 3000
class Zhifubao(Alibaba):
    # def __init__(self): 
    #     self.per_count = 100
    #     self.per_value = 3000
    
    def set_people(self,num):        
        global per_count
        return per_count -num


b = Zhifubao()
print("子公司员工有%d人"% b.get_number())
print("子公司市值是%d亿元"%b.profit([12, 13, 11, 14]))
print("子公司裁员过后人数是%d人"%b.set_people(10))