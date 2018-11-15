# class Student:
#     def __init__(self, n, a, s):
#         self.name, self.age, self.score = n, a, s

# docs = []  # 用来存储所有学生信息

# def add_student(lst):
#     s = Student('小张', 20, 100)
#     lst.append(s)
#     s = Student('小李', 18, 98)
#     lst.append(s)

# def get_student_count(lst):
#     return len(lst)

# def get_avg_score(lst):
#     ''' 获取所有学生的平均成绩'''
#     total = 0.0
#     for s in lst:
#         total += s.score
#     return total / len(lst)

# add_student(docs)  # 添加学生
# print('当前有%d个学生' % get_student_count(docs))
# print('当前学生的平均成绩是:', get_avg_score(docs))


# 此示例示意单继承的用法:
class Human:  # 人类的共性
    def say(self, what):
        print("say:", what)

    def walk(self, distance):  # 走路
        print("走了", distance, '公里')


class Student(Human):
    def study(self, subject):
        print("正在学习:", subject)


class Teacher(Student):
    '''说话,行走,教学'''

    def teach(self, subject):
        print("正在教:", subject)


h1 = Human()
h1.say('天气晴了')
h1.walk(5)
print('---------------')
s1 = Student()
s1.walk(4)
s1.say('感觉有点累')
s1.study('Python')
print('===============')
t1 = Teacher()
t1.walk(6)
t1.say('吃点啥好呢')
t1.teach('面向对象')
t1.study('转魔方')
