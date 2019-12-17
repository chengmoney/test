"""
  我们在类中定义的方法都是对象方法，也就是说这些方法都是发送给对象的消息。
  实际上，我们写在类中的方法并不需要都是对象方法，例如我们定义一个“三角形”类，通过传入三条边长来构造三角形，并提供计算周长和面积的
方法，但是传入的三条边长未必能构造出三角形对象，因此我们可以先写一个方法来验证三条边长是否可以构成三角形，这个方法很显然就不是对象
方法，因为在调用这个方法时三角形对象尚未创建出来（因为都不知道三条边能不能构成三角形），所以这个方法是属于三角形类而并不属于三角形
对象的。我们可以使用静态方法来解决这类问题
"""
# 静态方法代码如下:


class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_triangle(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def perimeter(self):
        return self._a + self._b + self._c


# 主函数:判断给出的三边是否为三角形,并求出周长
def main(a, b, c):
    if Triangle.is_triangle(a, b, c):
        t = Triangle(a, b, c)
        print('你输入的三角形三边分别为%.2f,%.2f,%.2f' % (a, b, b))
        print('三角形的周长是{}'.format(t.perimeter()))
        print('三角形的周长是{}'.format(Triangle.perimeter(t)))
    else:
        print('你输入的三角形三边分别为%.2f,%.2f,%.2f' % (a, b, c))
        print('不能构成三角形')


if __name__ == '__main__':
    main(1.1, 2, 3.2)
    main(2, 2, 2)

"""
    和静态方法比较类似，Python还可以在类中定义类方法，类方法的第一个参数约定名为cls，它代表的是当前类相关的信息的对象（类本身也是一个对
象，有的地方也称之为类的元数据对象），通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象，代码如下所示。
"""
# 类方法:创建一个类方法,通过调用这个类方法创建一个当前时间对象
from time import time, localtime, sleep


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        t = localtime()
        return cls(t.tm_hour, t.tm_min, t.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()



