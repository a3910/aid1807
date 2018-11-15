# from collections import Iterable


# class MyList(object):
#     def __init__(self):
#         self.items = []
#         self.current = 0

#     def add(self, val):
#         self.items.append(val)

#     def __next__(self):
#         if self.current < len(self.items):
#             item = self.items[self.current]
#             self.current += 1
#             return item
#         else:
#             raise StopIteration

#     def __iter__(self):
#         return self  #可迭代对象本身就是一个迭代器


# if __name__ == '__main__':
#     mylist = MyList()
#     mylist.add(1)
#     mylist.add(2)
#     mylist.add(3)
#     mylist.add(4)
#     mylist.add(5)
# for num in mylist:
#     print(num)


# coding:utf-8
# class FibIterator(object):
#     def __init__(self, n):
#         self.n = n  # 需要遍历的元素个数
#         self.current = 0  # 当前遍历的元素个数
#         self.num1 = 0  # 第一个元素
#         self.num2 = 1  # 第二个元素

#     def __next__(self):
#         if self.current < self.n:
#             self.num1, self.num2 = self.num2, self.num1+self.num2
#             self.current += 1
#             return self.num1
#         else:
#             raise StopIteration

#     def __iter__(self):
#         return self


# if __name__ == '__main__':
#     fibiterator = FibIterator(100)
#     for num in fibiterator:
#         print(num)

# import re
# s = re.search(r"([A-Z])(\S+)", 'Hello World').group()
# print(s)
# b = re.search(r'(ab)+', "ababababab").group()
# print(b)
# c = re.search(r'\w+@\w+\.(com|cn)', 'try@163.com,try@qq.cn').group()
# print(c)
# K = re.split(r'\w+', 'hi #asaf @对方%asdf')
# print(K)
# m = re.sub(r'\s+', '#', 'Hello World    nihao', 1)
# print(m)
# n = re.subn(r'\s+', '#', 'Hello World    nihao')
# print(n)
# x = re.finditer(r"([A-Z])(\S+)", 'Hello World')
# print(x)
# for i in x:
#     print(i.group())
# k = re.match(r'foo', 'food on the table')
# print(k)
# fullmatch
# try:
#     obj = re.fullmatch(r'\w+', 'abcdef123')
#     print(obj.group())
# except AttributeError as e:
#     print(e)


# regex = re.compile(r'hello', re.I)

# L = regex.finditer('hello Hello')
# for i in L:
#     print(i.group())  # ['hello', 'Hello']

# regex = re.compile(r'(?P<dog>ab)cd(ef)', flags=re.I)
# print(regex.groups)
# print(regex.groupindex)
#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
import os

f = open("text.py", 'r')
for line in (f.readlines()):
    k = re.search(r'(MAC:)\w+', line)
    if k is not None:
        print(k.group())
f.close()


# import re
# pattern = r"(?P<dog>ab)cd(?P<pig>ef)"
# regex = re.compile(pattern)
# # 获取match对象
# match_obj = regex.search('abcdefghij', pos=0, endpos=7)
# print(match_obj.pos)  # 匹配目标字符串的开始位置
# print(match_obj.endpos)  # 匹配目标字符串的结束位置
# print(match_obj.re)  # 匹配正则表达式
# print(match_obj.string)  # 匹配字符串
# print(match_obj.lastgroup)  # 最后一组的排名
# print(match_obj.lastindex)  # 最后一组是第几组
# print("====================================\n")
# print(match_obj.span())   # 匹配到内容的起止位置
# print(match_obj.start())  # 匹配到内容的开始位置
# print(match_obj.end())    # 匹配到内容的结束位置
# print(match_obj.group())
# print(match_obj.group(2))
# print(match_obj.groups())  # 所有子组匹配内容
# print(match_obj.groupdict())  # 捕获组字典

# print('---------------------')

# import re


# s = '''hello world
# nihao Beijing'''

# obj = re.search(r"world$",s,re.M)
# print(obj.group())


# #匹配每一行的结尾或者开头

# obj = re.search(r"world",s).group()
# print(obj)


# import re

# regex = re.compile(r'hello',re.I)

# l = regex.findall('hello Hello')
# print(l)  #['hello', 'Hello']

# import re
# s ='hello world'
# pattern = r'Hello world'
# regex = re.compile(pattern, re.I)
# try:
#     s = regex.search(s).group()
# except:
#     print('wrong')
# else:
#     print(s)  # ['hello world']

# import re

# regex = re.compile(r'hello',re.I)


# s = '''hello world
# nihao Beijing'''

# l = re.findall(r'.+',s)
# print(l)
# l = re.findall(r'.+',s,re.S)
# print(l)


#['hello world', 'nihao Beijing']
#['hello world\nnihao Beijing']


import re

regex = re.compile(r'Hello')


pattern = r"""(?P<dog>\w+)  #dog组
\s+   #匹配任意多个空格
(\W+)  #匹配一些特殊字符
"""
# 添加注释同时忽略大小写
try:
    s = re.match(pattern, 'hello  %#@', re.X | re.I).group()
except:
    print('Wrong')
else:
    print(s)


# hello  %#@
