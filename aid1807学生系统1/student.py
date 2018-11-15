class Student:
    def __init__(self,n,a,s=0):
        self.__name, self.__age, self.__score = n, a, s

    def get_info(self):
        '''此方法用来返回学生信息的元组'''
        return (self.__name, self.__age, self.__score)

    def del_xinxi(self):
        return self.__name

    def check_xinxi(self):
        return self.__name

    def amend_xinxi(self):
        return self.__name 

    def get_score(self):
        return self.__score

    def get_age(self):
        return self.__age

    def save(self, file):
        '''学生拿到文件后,自己来向文件里写东西'''
        file.write(self.__name)
        file.write(',')
        file.write(str(self.__age))
        file.write(',')
        file.write(str(self.__score))
        file.write('\n')

