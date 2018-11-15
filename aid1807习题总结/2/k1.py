
# 1、创建三个游戏人物，分别是：

# 安妮，女，18，初始战斗力1000
# 亚索，男，20，初始战斗力1800
# 赵信，男，19，初始战斗力2500

# 2、游戏场景，分别：
# 以下用使用事例方法完成

# 草丛战斗，英雄消耗200战斗力
# 自我修炼，英雄增长100战斗力
# 多人战斗，英雄消耗500战斗力

# 3、游戏结束一轮后显示各个英雄的信息

# 要求:使用类封装，各个方法要求使用''' '''进行备注，代码要简洁


class Game:
    """遊戲"""

    def __init__(self, name, sex, age, sword):
        self.__name = name  # 姓名
        self.__sex = sex  # 性別
        self.__age = age  # 年齡
        self.__sword = sword
        # print("__init__方法被调用")

    def grassland(self):
        """注释：草丛战斗，消耗200战斗力"""
        self.__sword = self.__sword - 200

    def practice(self):
        """注释：自我修炼，增长100战斗力"""
        self.__sword = self.__sword + 200

    def incest(self):
        '''注释：多人游戏，消耗500战斗力'''
        self.__sword = self.__sword - 500

    def detail(self):
        avi = "姓名:{0};\t性别:{1};\t年龄:{2};\t战斗力:{3}".\
            format(self.__name, self.__sex, self.__age, self.__sword)
        print(avi)
        print()
        # print(self.name)
        # print(self.sex)
        # print(self.age)
        # print(self.sword)

    # ##################### 开始游戏 #####################


lin = Game('琳', '女', 18, 1000)  # 创建琳角色
kaka = Game('卡卡西', '男', 20, 1800)  # 创建卡卡西角色
tu = Game('帶土', '女', 19, 2500)  # 创建波多多角色

lin.incest()  # 琳参加一次多人游戏
kaka.practice()  # 卡卡西自我修炼了一次
tu.grassland()  # 帶土参加一次草丛战斗

# 输出当前所有人的详细情况
lin.detail()
kaka.detail()
tu.detail()
print()

lin.incest()  # 琳又参加一次多人游戏
kaka.incest()  # 卡卡西也参加了一个多人游戏
tu.practice()  # 帶土自我修炼了一次

# 输出当前所有人的详细情况
lin.detail()
kaka.detail()
tu.detail()
print()

herolist = []


