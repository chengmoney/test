# Python是一门动态语言。通常，动态语言允许我们在程序运行时给对象绑定新的属性或方法，
# 当然也可以对已经绑定的属性和方法进行解绑定。
# 但是如果我们需要限定自定义类型的对象只能绑定某些属性，
# 可以通过在类中定义__slots__变量来进行限定。
# 需要注意的是__slots__的限定只对当前类的对象生效，对子类并不起任何作用。

# 如果不用__slots__限制绑定属性,可以绑定任何属性


class Student1(object):
    pass


student1 = Student1()
student1.name = 'chengyu'
student1.age = 29
student1.gender = '男'
student1.hello = True
student2 = Student1()
# student2.name 通过上面方式绑定的属性不能跨实例


class Student(object):
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def set_name(self, name):
        self._name = name


student = Student('chengyu', 29)
student._gender = '男'
# student.hello = 'True' 绑定不成功

