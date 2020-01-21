# 创建课程对象
class Course(object):
    def __init__(self, name, issue):
        self.name = name
        self.issue = issue


# 创建学校对象
class School(Course):
    def __init__(self, address):
        super(School, self).__init__()
        self.address = address


# 实例化2门课程python 3期和Linux 1期
python = Course('python', 3)
Linux = Course('Linux', 1)

# 实例化北京校区的Python课程和成都校区的Linux 课程
beijing = School('北京校区')
chengdu = School('成都校区')


# 创建学生对象
class Student(School):
    def __init__(self, student_name, report=[]):
        super(Student, self).__init__()
        self.name = student_name
        self.report = report

    def search_course(self):
        print('{0}同学，你报了{1}第{2}期课程'.format(self.name, Course.name, Course.issue))


# 创建讲师对象
class Lecturer(Student):
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def teach(self, record_name):
        teach = TeacherRecord(record_name, self.name, Course.name, Course.issue)
        return teach

    def marking(self, student, score):
        Student.report.append(score)



# 创建课程实例对象
class TeacherRecord(object):
    def __init__(self, record_name, teacher, course_name, course_issue):
        self.record_name = record_name
        self.teacher = teacher
        self.course_name = course_name
        self.course_issue = course_issue


# 创建Admin对象
class Admin(object):
    def __init__(self, admin_name):
        self.name = admin_name

    def add_student(self, name, school, course):
        student = Student(name, school, course)
        print('已创建在{1}上{2}第{3}期课程的{0}学员'.format(name, school.address, course.name, course.issue))
        return student

    def add_lecture(self, name, course):
        lecture = Lecturer(name, course)
        print('已创建{0}讲师,并分配给{1}第{2}期课程'.format(name, course.name, course.issue))
        return lecture

# 对Admin进行实例化
admin = Admin('admin')

# 管理员创建了北京校区的学员小张，并将其分配在了Python 3期
xiaozhang = admin.add_student('小张', beijing, python)

# 管理员创建了讲师小周，并将其分配给了Python 3期
xiaozhou = admin.add_lecture('小周', python)






