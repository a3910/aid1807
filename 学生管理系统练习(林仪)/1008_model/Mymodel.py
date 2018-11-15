# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# flask是个处理后台逻辑的框架
from flask import Flask
from flask import request  # 用来接收前端页面提交的数据
from flask import redirect    # 返回重定向请求路径
from flask import render_template    # 用来渲染html模板

# 用来操作数据库的模型
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

# app创建一个面向框架的对象,
app = Flask(__name__)

# 配置数据库的信息，并创建一个能与数据库交互的对象db
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql://root:123456@localhost:3306/flask_db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

# 下面创建的类是用来绑定数据库的表的，前提要先在数据库手动创建一个数据库，如flask_db
# 程序执行的时候自动去数据库创建对应的表，如果表已经存在，就跳过创建

# 创建与学生表信息表student绑定关系的类，与课程表course是多对多关系
class Student(db.Model):
    __tablename__ = 'student'  # 表名
    # 表字段
    s_id = db.Column(db.Integer, primary_key=True)
    s_name = db.Column(db.String(10), nullable=False)
    s_age = db.Column(db.SmallInteger, nullable=False)
    # 建立与课程表course的关系
    courses = db.relationship("Course", secondary='student_course',
                              lazy='dynamic', backref=db.backref('students', lazy='dynamic'))
    def __init__(self, s_name, s_age):
        self.s_name = s_name
        self.s_age = s_age
    # 当输出打印表类具体对象时，方便查看
    def __repr__(self):
        return '<sName:%r>' % self.s_name

# 创建与与课程表course绑定关系的类
class Course(db.Model):
    __tablename__ = 'course'
    c_id = db.Column(db.Integer, primary_key=True)
    c_name = db.Column(db.String(50), nullable=False)
    teachers = db.relationship('Teacher', backref='course',
                               lazy='dynamic')
    def __init__(self, c_name):
        self.c_name = c_name

    def __repr__(self):
        return '<cName:%r>' % self.c_name

# 这个表是用来建立学生表与课程表的多对多关系的
student_course = db.Table(
    "student_course",
    db.Column('id', db.Integer, primary_key=True),
    db.Column('s_id', db.Integer, db.ForeignKey("student.s_id")),
    db.Column('c_id', db.Integer, db.ForeignKey("course.c_id"))
)

# 创建与与老师信息表teacher绑定关系的类，与course多对一关系
class Teacher(db.Model):
    __tablename__ = "teacher"
    t_id = db.Column(db.Integer, primary_key=True)
    t_name = db.Column(db.String(10), nullable=False)
    t_age = db.Column(db.SmallInteger, nullable=False)
    t_course = db.Column(db.Integer, db.ForeignKey('course.c_id'))
    wife = db.relationship('Wife', backref="teacher", uselist=False)

    def __init__(self, t_name, t_age):
        self.t_name = t_name
        self.t_age = t_age

    def __repr__(self):
        return "<tName:%r>" % self.t_name

# 创建与老师配偶信息表wife绑定关系的类，与teacher一对一关系
class Wife(db.Model):
    __tablename__ = "wife"
    w_id = db.Column(db.Integer, primary_key=True)
    w_name = db.Column(db.String(20), nullable=False)
    w_age = db.Column(db.SmallInteger, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.t_id'))

    def __init__(self, w_name, w_age):
        self.w_name = w_name
        self.w_age = w_age

    def __repr__(self):
        return "<wName: %r>" % self.w_name
# 删除所有表
# db.drop_all()

# 直接创建所有表
db.create_all()


# 处理首界面的请求
@app.route('/school')
def School():
    return render_template('school.html')  # 返回请求的页面给浏览器


# 处理添加学生信息的请求,分'GET', 'POST'两种请求
@app.route('/add_student', methods=['GET', 'POST'])
def Insert_student():
    if request.method == "GET":
        course = Course.query.all()     #查询course表的数据
        # 把数据填入待返回的html模板中，然后把渲染过后的模板返回给浏览器
        return render_template('add_student.html', params=locals())
    else:
        #获取前端提交上来的数据
        stu_name = request.form.get('s_name')
        stu_age = request.form.get('s_age')
        course_id = request.form.getlist('course')
        student = Student(stu_name, stu_age)
        #插入数据
        for c in course_id:
            course = Course.query.filter_by(c_id=c).first()
            student.courses.append(course)
        db.session.add(student)
        return redirect("/query_student")   #重定向请求的路径


# 处理查看所有学生信息的请求
@app.route('/query_student', methods=['GET', 'POST'])
def Query_student():
    if request.method == "GET":
        std = db.session.query(Student).all()
        return render_template('query_student.html', params=locals())


# 通过id号查看学生信息的请求
@app.route('/query_one_student', methods=['GET', 'POST'])
def Query_one_student():
    id = request.args.get('id')
    std = db.session.query(Student).\
        filter_by(s_id=id).first()
    courses = std.courses.all()
    return render_template('query_one_student.html', params=locals())


# 删除学生信息
@app.route('/delete_student', methods=['GET', 'POST'])
def Delete_student():
    id = request.args.get('id')
    std = db.session.query(Student).\
        filter_by(s_id=id).first()
    db.session.delete(std)

    url = request.headers.get('referer', '/query_student')
    return redirect(url)

# 更新学生信息
@app.route('/update_student', methods=['GET', 'POST'])
def Update_student():
    if request.method == 'GET':
        id = request.args.get('id')
        std = db.session.query(Student).\
            filter_by(s_id=id).first()
        return render_template('update_student.html', params=locals())
    else:
        id = request.form.get('uid')
        name = request.form.get('uname')
        age = request.form.get('uage')

        std = db.session.query(Student).\
            filter_by(s_id=id).first()
        std.s_name = name
        std.s_age = age
        db.session.add(std)
        return redirect("/query_student")

# 查看老师信息
@app.route('/query_teacher', methods=['GET', 'POST'])
def Query_teacher():
    if request.method == "GET":
        teacher = Teacher.query.all()
        return render_template('query_teacher.html', params=locals())

# 查看老师信息——手工去查询
# @app.route('/query_teacher_hend', methods=['GET', 'POST'])
# def query_teacher_hend():
#     if request.method == "GET":
#         result = db.session.query(Teacher, Course).filter(
#             Teacher.c_course == Course.c_id).all()
#         response = ''
#         for r in result:
#             response += "姓名：%s 课程：%s \n" % (r.Teacher.t_name,
#                                             r.Course.c_name)
#         return response


# 添加老师信息
@app.route('/add_teacher', methods=['GET', 'POST'])
def Insert_teacher():
    if request.method == "GET":
        course = db.session.query(Course).all()
        return render_template('add_teacher.html', params=locals())
    else:
        t_name = request.form.get('uname')
        t_age = request.form.get('uage')
        course_id = request.form.get('c_id')
        teacher = Teacher(t_name, t_age)
        course = db.session.query(Course).filter_by(c_id=course_id).first()
        teacher.course = course
        db.session.add(teacher)
        return redirect("/query_teacher")


# 查看课程信息
@app.route('/query_course', methods=['GET', 'POST'])
def Query_course():
    if request.method == "GET":
        cour = db.session.query(Course).all()
        return render_template('query_course.html', params=locals())


# 添加课程信息
@app.route('/add_course', methods=['GET', 'POST'])
def Insert_course():
    if request.method == "GET":
        return render_template('add_course.html')
    else:
        cour_name = request.form.get('c_name')
        course = Course(cour_name)
        db.session.add(course)
        return redirect("/query_course")

# 查看老师配偶信息
@app.route('/query_wife', methods=['GET', 'POST'])
def Query_wife():
    if request.method == "GET":
        wife = Wife.query.all()
        return render_template('query_wife.html', params=locals())


# 添加老师配偶信息
@app.route('/add_wife', methods=['GET', 'POST'])
def Insert_wife():
    if request.method == "GET":
        flage = request.args.get('flage')
        if not flage:
            flage = 0
        teacher = db.session.query(Teacher).all()
        return render_template('add_wife.html', params=locals())
    else:
        w_name = request.form.get('uname')
        w_age = request.form.get('uage')
        t_id = request.form.get('t_id')
        wife = Wife.query.filter_by(teacher_id=t_id).first()
        if wife:
            return redirect("/add_wife?flage=1")

        wife = Wife(w_name, w_age)
        teacher = db.session.query(Teacher).filter_by(t_id=teacher_id).first()
        wife.teacher = teacher
        db.session.add(wife)
        return redirect("/query_wife")

# 运行web服务
if __name__ == '__main__':
    # app.run(debug=True)
    app.run('0.0.0.0',5000)
