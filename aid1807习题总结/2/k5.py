class foo:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def detail(self):
        avi = "姓名:{0};\t年龄:{1};\t".\
            format(self.name, self.age)
        print(avi)
obj=foo('python3',99)
obj.detail()