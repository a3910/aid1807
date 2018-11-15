# k3.py

# 1、创建三个游戏人物，分别是：
# 要求:把每个人物信息存入字典，把每个字典添加入一个列表
         
# 安妮，女，18，初始战斗力1000
# 亚索，男，20，初始战斗力1800
# 赵信，男，19，初始战斗力2500

# 2、游戏场景：对上述列表进行for循环遍历和判断英雄

# 赵信：print(草丛战斗)，英雄消耗200战斗力
# 安妮：print(自我修炼)，英雄增长100战斗力
# 亚索：print(多人战斗)，英雄消耗500战斗力

# 3、游戏结束一轮后显示各个英雄的信息
# 使用函数，参数为含有英雄人物的字典

# 要求，本次练习不使用类，只是列表和字典，
# 函数的基本用法，代码要简洁，多使用备注

def Xinxi():
    l = []
    while True:
        n = input('输入姓名')
        if not n:
            break
        try:
            s = input('输入性别')
            a = int(input('输入年龄'))
            f = int(input('输入初始战斗力'))
        except:
            print('输入有误')
            continue
        l.append(dict(name=n,sex=s,age=a,fight=f))
    return l
# print(Xinxi())
l = Xinxi()

for d in l:
    if d['name']=='赵信':
        print('赵信-草丛战斗')
        d['fight'] -= 200
    if d['name']=='安妮':
        print('安妮-自我修炼')
        d['fight'] += 100
              
    if d['name']=='亚索':
        print('亚索-多人战斗')
        d['fight'] -=500



def show(d):
    avi = "姓名:{0};\t性别:{1};\t年龄:{2};\t战斗力:{3}".\
        format(d['name'],d['sex'],d['age'],d['fight'])
    print(avi)

for d in l:
    print(d)
    show(d)
#调用show(d)把每个英雄信息逐个打印出来




























# class Human:
#     pass
 
# human1 = Human()
# print(human1.__dict__)  # {}
# human1.sword = 1000
# human1.age = 18
# human1.sex = '女'
# human1.name = '赵信'
# print(human1.__dict__)

