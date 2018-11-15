from student import Student
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

      L.append(Student(n, a, s))
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
        n, a, s = d.get_info()
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
      if n == d.del_xinxi():
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
      if n == d.check_xinxi():
          print('姓名:',d.name,'\n'
                '年龄:',d.age,'\n'#'\n'后如果不加逗号，
                '分数:',d.score)#假如后面跟的不是字符串，它会报错
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
      if n == d.amend_xinxi():
          d.score=int(score1)
          d.name=name1
          d.age=int(age1)#函数名不能被赋值，能被赋值的必须是一个变量，
          break #amend_xinxi()定义的是一个函数，        
                #amend_xinxi = 1 就像是print(1)= 3 不能成立
    else:
        print('信息不存在，请重新输入')
  print(L)   


def output_student_by_score_desc(L):
    def get_score(d):
        return d.get_score()
    L = sorted(L, key=get_score, reverse=True)
    output_student(L)
 
 
def output_student_by_score_asc(L):
    L = sorted(L, key=lambda d: d.get_score())
    output_student(L)

 
def output_student_by_age_desc(L):
    L = sorted(L, key=lambda d: d.get_age(),reverse=True)
    output_student(L)
 
 
def output_student_by_age_asc(L):
    L = sorted(L, key=lambda d: d.get_age())
    output_student(L)

def save_to_file(L, filename='si.txt'):
    try:    
        f = open(filename,'w')
        for student in L:
            student.save(f)
        f.close()
        print("保存成功")
    except OSError:
        print("写文件失败")

def read_from_file(filename='si.txt'):
    L = []
    try:
        f = open(filename)
        for line in f:
            n, a, s = line.strip().split(',')
            a = int(a)
            s = int(s)  # 转为整数

            L.append(Student(n, a, s))

        f.close()
    except OSError:
        print("读取文件失败")

    return L    
