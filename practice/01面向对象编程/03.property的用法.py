# @property的用法
class Student(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def get_name(self):
        return self._name

    @get_name.setter
    def set_name(self, name):
        self._name = name

    # @property
    def play(self):
        print('{} is playing'.format(self._name))


student = Student('chengyu', 30)
print(student.get_name)
# student.play
student.play()
student.set_name = 'cheng'
print(student.get_name)
# student.play 不能调用,不能显示结果 没有用@property
student.play()
