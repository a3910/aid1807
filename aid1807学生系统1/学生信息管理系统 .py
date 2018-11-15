
def show_menu():
    print('+----------------------------------+')
    print('| 1)  添加学生信息                 |')
    print('| 2)  显示学生信息                 |')
    print('| 3)  删除学生信息                 |')
    print('| 4)  查询学生信息                 |')
    print('| 5)  修改学生信息                 |')
    print('| 6)  按学生成绩高-低显示学生信息　|')
    print('| 7)  按学生成绩低-高显示学生信息　|')
    print('| 8)  按学生年龄高-低显示学生信息　|')
    print('| 9)  按学生年龄低-高显示学生信息　|')          
    print('| q)  退出                         |')
    print('+----------------------------------+')
   
# s = input("请输入中英文混合的字符串:") 
# print('您输入的中文的字符个数是:', get_chinese_char_count(L))
def input_student():
  L = []  # 创建一个新的列表，用此列表准备保存学生信息
      # 录入学生信息
  while True:
      n = input("请输入姓名: ")
      if not n:
        break
      try:
          a = int(input("请输入年龄: "))
          s = int(input('请输入成绩: '))
      except:
          print('输入有误')
          continue
          # 创建一个新的字典，把学生的信息存入字典中
      d = {}  # 每一次都重新创建一个新的字典
      d['name'] = n
      d['age'] = a
      d['score'] = s
      L.append(d)
  return L  

def get_chinese_char_count(x):
    count = 0  # 先假设个数为0
    for ch in x:
        # 如果ch为中文字典,则count 做加一操作
        if ord(ch) > 127:
            count += 1
    return count

def output_student(L):
  print("+---------------+----------+----------+")
  print("|     name      |   age    |   score  |")
  print("+---------------+----------+----------+")

  for d in L:
      n = d['name']
      a = d['age']
      s = d['score']
      chinese_cnt = get_chinese_char_count(n)
      print('|%s|%s|%s|' % (n.center(15-chinese_cnt),
                              str(a).center(10),
                              str(s).center(10)
                            )
            )  
     

  # print("|    tarena     |    20    |     99   |")
  # print("|     name2     |    30    |     88   |")
  print("+---------------+----------+----------+")  

def delete_student(L):
  while True:
    n = input('查找名字:')
    print('正在删除',n)
    if n == '':
        break
    for d in L:
      if n == d['name']:
          L.remove(d)
          break        
    else:
        print('信息不存在，请重新输入')
  print(L)   

def check_student(L):
  while True:
    n = input('查找名字:')
    if n == '':
        break
    for d in L:
      if n == d['name']:
          print(d)
          break
    else:
      print('信息不存在，请重新输入')

def amend_student(L):
  while True:
    n = input('查找名字:')
    if n == '':
        break
    score1 = input('修改分数')
    age1 = input('修改年龄')
    name1 = input('修改名字:')        
    for d in L:
      if n in d['name']:
          d['score']=int(score1)
          d['name']=name1
          d['age']=int(age1)
          break        
    else:
        print('信息不存在，请重新输入')
  print(L)   


def output_student_by_score_desc(L):
    def k(d):
        return d['score']
    L = sorted(L, key=k, reverse=True)
    output_student(L)
 
 
def output_student_by_score_asc(L):
    L = sorted(L, key=lambda d: d['score'])
    output_student(L)

 
def output_student_by_age_desc(L):
    L = sorted(L, key=lambda d: d['age'],reverse=True)
    output_student(L)
 
 
def output_student_by_age_asc(L):
    L = sorted(L, key=lambda d: d['age'])
    output_student(L)
  




def main():
  L = []
  while True:
    show_menu()
        # 此处先显示菜单
    s = input("请选择: ")
    if s == 'q':
        break
    elif s == '1':
        L += input_student()
    elif s == '2':
        output_student(L)
    elif s == '3':
        delete_student(L)
    elif s == '4':
        check_student(L)
    elif s == '5':
        amend_student(L)
    elif s == '6':
        output_student_by_score_desc(L)
    elif s == '7':
        output_student_by_score_asc(L)
    elif s == '8':
        output_student_by_age_desc(L)
    elif s == '9':
        output_student_by_age_asc(L)
if __name__ == '__main__':
    main()
